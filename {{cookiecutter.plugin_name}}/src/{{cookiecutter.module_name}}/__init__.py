{% if cookiecutter.use_git_tags_for_versioning == 'y' %}
try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"
{% else -%}
__version__ = "0.0.1"
{% endif -%}

{% if cookiecutter.include_math_plugin == 'y' %}
from ._math import my_math_func
{% endif %}{% if cookiecutter.include_operator_plugin == 'y' %}
from ._operator import MyLinOp, NullFunc
{% endif %}{% if cookiecutter.include_solver_plugin == 'y' -%}
from ._solver import MySolver
{% endif %}{% if cookiecutter.include_stop_plugin == 'y' -%}
from ._stop import MyStopCriterion
{% endif %}
__all__ = (
    {% if cookiecutter.include_math_plugin == 'y' -%}
    "my_math_func",
    {% endif %}{% if cookiecutter.include_operator_plugin == 'y' -%}
    "MyLinOp",
    "NullFunc",
    {% endif %}{% if cookiecutter.include_solver_plugin == 'y' -%}
    "MySolver",
    {% endif %}{% if cookiecutter.include_stop_plugin == 'y' -%}
    "MyStopCriterion",
{% endif -%}
)