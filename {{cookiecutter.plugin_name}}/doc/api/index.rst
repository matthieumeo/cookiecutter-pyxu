API Reference
=============


.. The goal of this page is to provide an alphabetical listing of all {{cookiecutter.plugin_name}} objects exposed to users.
.. This is achieved via the `autosummary` extension.
.. While `autosummary` understands `automodule`-documented packages, explicitly listing a module's contents is required.

Welcome to the official API reference for {{cookiecutter.plugin_name}}.
This API documentation is intended to serve as a comprehensive guide to the library's various modules, classes, functions, and interfaces.
It provides detailed descriptions of each component's role, relations, assumptions, and behavior.

Please note that this API reference is not designed to be a tutorial;
it is a technical resource aimed at users who are already familiar with Pyxu.

Subpackages
-----------

{% if cookiecutter.include_math_plugin == 'y' -%}
pyxu.math
^^^^^^^^^

.. autosummary::

   ~pyxu.math.eigh

.. toctree::
   :maxdepth: 2
   :hidden:

   math

{% endif %}{% if cookiecutter.include_operator_plugin == 'y' -%}
pyxu.operator
^^^^^^^^^^^^^

.. autosummary::

   ~pyxu.operator.Flip
   ~pyxu.operator.NullFunc

.. toctree::
   :maxdepth: 2
   :hidden:

   operator

{% endif %}{% if cookiecutter.include_solver_plugin == 'y' -%}
pyxu.opt.solver
^^^^^^^^^^^^^^^
.. autosummary::

   ~pyxu.opt.solver.GradientDescent


.. toctree::
   :maxdepth: 2
   :hidden:

   opt.solver
   ../references

{% endif %}{% if cookiecutter.include_stop_plugin == 'y' -%}

pyxu.opt.stop
^^^^^^^^^^^^^

.. autosummary::

   ~pyxu.opt.stop.Deadline

.. toctree::
   :maxdepth: 2
   :hidden:

   opt.stop
{% endif %}
