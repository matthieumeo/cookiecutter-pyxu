import collections.abc as cabc
import types

import numpy as np

import pycsou.abc.operator as pyco
import pycsou.runtime as pycrt
import pycsou.util.ptype as pyct


__all__ = ["MyLinOp", "NullFunc"]

class MyLinOp(pyco.LinOp):
    def __init__(self, arg_shape: pyct.NDArrayShape, axis: pyct.NDArrayAxis = None) -> pyct.OpT:
        r"""
        Flip axis

        Parameters
        ----------
        arg_shape: pyct.NDArrayShape
            Shape of the data to be flipped.
        axis: pyct.NDArrayAxis
            Axis or axes along which the input array is flipped.
            The default, axis=None, will flip all the in all the axis of the input array.
            If axis is negative it counts from the last to the first axis.
        """

        def as_array(obj) -> np.ndarray:
            if isinstance(obj, cabc.Sequence):
                pass
            else:
                obj = [obj]
            return np.array(obj, dtype=int)

        arg_shape = as_array(arg_shape)
        assert np.all(arg_shape > 0)
        dim = np.prod(arg_shape).item()
        N_dim = len(arg_shape)

        if axis is None:
            axis = np.arange(N_dim)
        axis = np.unique(as_array(axis))  # drop potential duplicates
        assert np.all((-N_dim <= axis) & (axis < N_dim))  # all axes in valid range
        self.axis = (axis + N_dim) % N_dim  # get rid of negative axes

        super().__init__(shape=(dim, dim))

    @pycrt.enforce_precision(i="arr")
    def apply(self, arr: pyct.NDArray) -> pyct.NDArray:
        sh = arr.shape[:-1]
        arr = arr.reshape(*sh, *self._arg_shape)
        out = arr.copy(deep=True)

        for ax in self.axis:
            out = np.flip(out, axis=ax)

        out = out.reshape(*sh, self.codim)
        return out

    @pycrt.enforce_precision(i="arr")
    def adjoint(self, arr: pyct.NDArray) -> pyct.NDArray:
        return self.apply(arr)


def NullFunc():
    print("This just prints")