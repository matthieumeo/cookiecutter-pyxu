import numpy as np
import pycsou.operator.linop as pycl
from phantominator import shepp_logan
from phantominator.traj import radial


__all__ = ["SheppLogan"]
class PycsouData:
    pass
class SheppLogan(PycsouData):
    def __init__(self, modality="MR", param1=288, param2=72, nx=128, ny=128, sampling="radial"):

        if modality == "MR":

            k = self.sample_kspace(param1=param1, param2=param2, sampling=sampling)
            self.nx, self.ny = nx, ny
            self.forward = pycl.nufft.NUFFT.type2(
                x=k,
                N=(nx, ny),
                isign=-1,
                eps=1e-4,
                real=True
            )

        else:
            raise NotImplementedError
    def sample_kspace(self, param1, param2, sampling="radial", seed=0):

        if sampling == "uniform":

            kx, ky = np.meshgrid(
                np.linspace(-1, 1, int(np.sqrt(param1))) * np.pi,
                np.linspace(-1, 1, int(np.sqrt(param2))) * np.pi,
            )

        elif sampling == "random":
            rng = np.random.default_rng(seed=seed)
            kx, ky = rng.uniform(low=-np.pi, high=np.pi, size=(param1, 2)).T

        elif sampling == "radial":
            sx, spokes = param1, param2
            kx, ky = radial(sx, spokes)
            kx, ky = kx / sx * 2 * np.pi, ky / sx * 2 * np.pi

        else:
            raise NotImplementedError

        return np.concatenate([kx.reshape(-1, 1), ky.reshape(-1, 1)], axis=1)

    def load_data(self, which="M0"):
        M0, T1, T2 = shepp_logan((self.nx, self.ny, 1), MR=True, zlims=(-.25, .25))
        M0, T1, T2 = M0[..., 0], T1[..., 0], T2[..., 0]

        y = {"M0": M0, "T1": T1, "T2": T2}[which]
        x = self.forward(y)

        return x, y, self.forward
