import numpy as np
import dask.array as da
import numba

import pycsou.util as pycu
import pycsou.util.ptype as pyct
import pycsou.util.deps as pycd
if pycd.CUPY_ENABLED:
    import cupy as cp

__all__ = ["eigh"]

def eigh(arr: pyct.NDArray, arg_shape: pyct.NDArrayShape):
    r"""
    Batch computation of the eigenvalues and eigenvectors of a batch (:math:`\mathcal{N}`-shaped, where
    :math:`\mathcal{N} = (N_{1}, \cdots, N_{k})`) of complex Hermitian (conjugate symmetric) or a real symmetric
    matrices.

    This function leverages Numba's GUVectorize to improve performance.

    Returns two objects, an :math:`\mathcal{N}`-shaped batch of 1-D arrays containing the eigenvalues, and an
    :math:`\mathcal{N}`-shaped batch of 2-D square matrices of the corresponding eigenvectors (in columns).

    Note
    ----
    In the current version only works for CPU (due to known issue with GPU https://github.com/numba/numba/issues/6256)

    Parameters
    ----------
    arr: (…, M, M) pyct.NDArray
    arg_shape: pyct.NDArrayShape

    Returns
    -------
    w: (…, M) pyct.NDArray
        The eigenvalues in ascending order, each repeated according to its multiplicity.
    v: (…, M, M) pyct.NDArray
        The column v[..., i] is the normalized eigenvector corresponding to the eigenvalue w[..., i].
    """
    assert len(np.unique(arg_shape))
    st_sh = arr.shape[:-1]
    st_size = np.prod(st_sh)
    arr = arr.reshape(st_size, *arg_shape)

    xp = pycu.get_array_module(arr)

    w = xp.zeros_like(arr[..., 0])
    v = xp.zeros_like(arr)

    eigh_dispatcher(arr, w, v)
    w = w.reshape((*st_sh, arg_shape[0]))
    v = v.reshape((*st_sh, -1))
    return w, v

@numba.guvectorize(
    [(numba.float32[:, :], numba.float32[:], numba.float32[:, :]),
     (numba.float64[:, :], numba.float64[:], numba.float64[:, :])],
    '(m, m) -> (m), (m, m)'
)
def eigh_cpu(arr, w, v):
    w[:], v[:] = np.linalg.eigh(arr)

# #Can't use eigh_gpu because guvectorize with target=`cuda` doesn't support multiple outputs yet
# @numba.guvectorize(
#     [(numba.float32[:, :], numba.float32[:], numba.float32[:, :]),
#      (numba.float64[:, :], numba.float64[:], numba.float64[:, :])],
#     '(m, m) -> (m), (m, m)',
#     target="cuda"
# )
# def eigh_gpu(arr, w, v):
#     w, v = cp.linalg.eigh(arr)

# #Can't use eigh_dask because map_blocks doesn't support multiple outputs yet
# def eigh_dask(arr, w, v):
#     # w, v = da.apply_gufunc(eigh_dispatcher, '(n, m, m),(n, m),(n, m, m)->(n, m),(n, m, m)', arr , w, v)
#     w, v = da.map_blocks(eigh_dispatcher, arr, w, v)
#     return w, v

def eigh_dispatcher(arr, w, v):
    #can't use redirect because @numba.guvectorize doesn't accept keyword args, only positional args.

    xp = pycu.get_array_module(arr)
    if xp == np:
        w, v = eigh_cpu(arr, w, v)
    # elif xp == cp:
    #     w, v = eigh_gpu(arr, w, v)
    # elif xp == da:
    #     w, v = eigh_dask(arr, w, v)
    else:
        raise NotImplementedError
    return w, v
