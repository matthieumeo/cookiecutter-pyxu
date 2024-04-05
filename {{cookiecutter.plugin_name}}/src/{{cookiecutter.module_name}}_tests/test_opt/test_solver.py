import numpy as np
import pytest
import pyxu.info.deps as pxd
import pyxu.runtime as pxrt
import pyxu.util as pxu
from pyxu.operator import SquaredL2Norm
from pyxu.opt.solver import GradientDescent


def allclose(x, y, xp):
    return xp.allclose(x, y)


@pytest.fixture(params=pxd.NDArrayInfo)
def ndi(request):
    ndi_ = request.param
    if ndi_.module() is None:
        pytest.skip(f"{ndi_} unsupported on this machine.")
    return ndi_


@pytest.fixture(params=pxrt.Width)
def width(request):
    return request.param


@pytest.fixture(
    params=[
        # dim,
        2,
        10,
        20,
    ]
)
def N(request):
    return request.param


@pytest.fixture(params=[True, False])
def accel(request):
    return request.param


@pytest.fixture(params=[True, False])
def tau(request):
    return request.param


@pytest.fixture(params=[0, 1, 2, 3, 4])
def seed(request):
    return request.param


@pytest.fixture
def data(N, ndi):
    #
    rng = np.random.default_rng(seed=0)
    x = rng.standard_normal(N)
    xp = ndi.module()
    return {"in_": xp.array(x), "out_gt": (xp.array(x))}


def test_gradient_descent(data, N):
    sl2 = SquaredL2Norm(dim_shape=N).argshift(-pxu.compute(data["in_"]))
    gd = GradientDescent(f=sl2)
    gd.fit(x0=np.random.randn(N), acceleration=True)
    assert np.allclose(gd.solution(), data["in_"])
