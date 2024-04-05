import numpy as np
import pytest
import pyxu.info.deps as pxd
import pyxu.runtime as pxrt

from pyxu.math import eigh


def allclose(x, y, xp, sign_matters=True):
    if sign_matters:
        return xp.allclose(x, y)
    else:
        return xp.allclose(xp.abs(x), xp.abs(y))


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
        # dim, #scheme
        (2, "FULL"),
        (2, "DIAG"),
        (3, "FULL"),
        (3, "DIAG"),
        (5, "FULL"),
    ]
)
def params(request):
    return request.param


@pytest.fixture
def dim_shape(params):
    return params[0], params[0]


@pytest.fixture
def scheme(params):
    return params[1]


@pytest.fixture
def batch_shape():
    return 3, 2


@pytest.fixture(params=[0, 1, 2, 3, 4])
def seed(request):
    return request.param


@pytest.fixture
def data(dim_shape, batch_shape, seed, ndi, scheme):
    # Make a batch of real & symmetric input matrices (PSD)
    rng = np.random.default_rng(seed=seed)
    input_shape = batch_shape + dim_shape
    if scheme == "FULL":
        x = rng.normal(size=input_shape)
        x += x.swapaxes(2, 3)
    elif scheme == "DIAG":
        x = rng.normal(size=input_shape)
        mask = np.tile((np.eye(dim_shape[0])), [*batch_shape, 1, 1])
        x *= mask

    w_np, v_np = np.linalg.eigh(x)
    if scheme == "DIAG":
        v_np = mask

    xp = ndi.module()
    return {"in_": xp.array(x), "out_gt": (xp.array(w_np), xp.array(v_np))}


def test_math(data, dim_shape, ndi):
    x = data["in_"]
    w_np, v_np = data["out_gt"]
    w, v = eigh(x, dim_shape=dim_shape)
    xp = ndi.module()
    assert allclose(v, v_np, xp, False)
    assert allclose(w, w_np, xp)
