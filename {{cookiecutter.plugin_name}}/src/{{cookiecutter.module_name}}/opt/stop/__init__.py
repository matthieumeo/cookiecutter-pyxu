import collections.abc as cabc
import datetime as dt

import pyxu.abc as pxa

__all__ = ["Deadline"]

class Deadline(pxa.StoppingCriterion):
    """
    Stop iterative solver at a specified date and time.
    """

    def __init__(self, t: dt.datetime):
        """
        Parameters
        ----------
        t: dt.datetime
            Deadline in the future.
        """
        try:
            assert t > dt.datetime.now()
            self._t_deadline = t
        except:
            raise ValueError(f"t: expected future deadline, got {t}.")
        self._t_start = dt.datetime.now()
        self._t_now = self._t_start

    def stop(self, state: cabc.Mapping) -> bool:
        self._t_now = dt.datetime.now()
        return self._t_now > self._t_deadline

    def info(self) -> cabc.Mapping[str, float]:
        d = (self._t_now - self._t_start).total_seconds()
        return dict(duration=d)

    def clear(self):
        self._t_start = dt.datetime.now()
        self._t_now = self._t_start