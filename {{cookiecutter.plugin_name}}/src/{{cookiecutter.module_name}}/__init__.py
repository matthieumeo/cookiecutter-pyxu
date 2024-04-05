import importlib.metadata

try:
    __version__ = importlib.metadata.version("pyxu_eigh")
except ImportError:
    __version__ = "unknown"

{% if cookiecutter.include_math_plugin == 'y' %}
from .math import eigh
{% endif %}{% if cookiecutter.include_operator_plugin == 'y' %}
from .operator import Flip, NullFunc
{% endif %}{% if cookiecutter.include_solver_plugin == 'y' -%}
from .opt import GradientDescent
{% endif %}{% if cookiecutter.include_stop_plugin == 'y' -%}
from .opt import Deadline
{% endif %}

__all__ = (
    {% if cookiecutter.include_math_plugin == 'y' -%}
    "eigh",
    {% endif %}{% if cookiecutter.include_operator_plugin == 'y' -%}
    "Flip",
    "NullFunc",
    {% endif %}{% if cookiecutter.include_solver_plugin == 'y' -%}
    "GradientDescent",
    {% endif %}{% if cookiecutter.include_stop_plugin == 'y' -%}
    "Deadline",
{% endif -%}
)