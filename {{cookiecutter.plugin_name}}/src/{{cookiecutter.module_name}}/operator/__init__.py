{% if cookiecutter.include_operator_plugin == 'y' %}
from .linop import Flip
from .func import NullFunc
__all__ = [
    "Flip",
    "NullFunc"
]
{% endif %}
