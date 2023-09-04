import datetime as dt
import numpy as np
from pyxu.operator.func import SquaredL2Norm
from {{cookiecutter.module_name}} import GradientDescent
from {{cookiecutter.module_name}} import Deadline

def test_stop():
    deadline = Deadline(
        t=dt.datetime(
            year=2023,
            month=2,
            day=29,
            hour=11,
            minute=59,
            second=59)
    )
    N = 10
    y = np.arange(N)
    sl2 = SquaredL2Norm(dim=N).asloss(y)
    gd = GradientDescent(f=sl2)
    gd.fit(x0=np.random.randn(N), acceleration=True, stop_crit=deadline)
    assert np.allclose(gd.solution(), y)