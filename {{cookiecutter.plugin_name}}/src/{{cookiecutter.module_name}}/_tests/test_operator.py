import numpy as np

from {{cookiecutter.module_name}} import MyLinop, NullFunc


def test_linop():
    """An example of how you might test your plugin."""
    rng = np.random.default_rng(seed=1)
    N = 5
    x = rng.normal(N)
    linop = MyLinop(N)
    assert np.allclose(linop(x), np.flipud(x))

def test_nullfunc():
    assert NullFunc() is None
