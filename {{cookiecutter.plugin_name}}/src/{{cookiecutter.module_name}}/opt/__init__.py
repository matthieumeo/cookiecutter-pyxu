
{% if cookiecutter.include_solver_plugin == 'y' -%}
from .solver import GradientDescent
{% endif %}{% if cookiecutter.include_stop_plugin == 'y' -%}
from .stop import Deadline
{% endif %}
__all__ = (
    {% if cookiecutter.include_solver_plugin == 'y' -%}
    "GradientDescent",
    {% endif %}{% if cookiecutter.include_stop_plugin == 'y' -%}
    "Deadline",
{% endif -%}
)