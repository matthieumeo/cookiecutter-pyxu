import numpy as np
from pyxu.operator.func import SquaredL2Norm
from {{cookiecutter.module_name}} import GradientDescent

def test_something():
    N = 10
    y = np.arange(N)
    sl2 = SquaredL2Norm(dim=N).asloss(y)
    gd = GradientDescent(f=sl2)
    gd.fit(x0=np.random.randn(N), acceleration=True)
    assert np.allclose(gd.solution(), y)