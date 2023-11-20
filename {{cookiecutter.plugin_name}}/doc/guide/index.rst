User Guide
##########

Our User Guide is designed to give you an in-depth understanding of the core concepts of this package.

.. toctree::
   :maxdepth: 1
   :hidden:
{% if cookiecutter.include_math_plugin == 'y' -%}
   example_eigh.ipynb
{% endif %}{% if cookiecutter.include_operator_plugin == 'y' -%}
   example_flip.ipynb
{% endif %}{% if cookiecutter.include_solver_plugin == 'y' -%}
   example_gd.ipynb
{% endif %}{% if cookiecutter.include_stop_plugin == 'y' -%}
    example_deadline.ipynb
{% endif %}

