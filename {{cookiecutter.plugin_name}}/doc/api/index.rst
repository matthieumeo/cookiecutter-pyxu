API Reference
=============

Welcome to the for {{cookiecutter.module_name}}. This API documentation is intended to serve as a comprehensive guide to the
library's extended contributions, providing you with detailed descriptions of each component's role, relations, assumptions, and behavior.
Please note that this API reference is not designed to be a tutorial; it's a technical resource aimed at users who are
already familiar with the `Pyxu <https://pyxu-org.github.io/>`_ framework and wish to dive deeper into the novel functionalities
provided in this extension.

.. contents:: Table of Contents
   :local:
   :depth: 2

.. The goal of this page is to provide an alphabetical listing of all objects exposed to users.  This is achieved
.. via the `autosummary` extension.  While `autosummary` understands `automodule`-documented packages, explicitly
.. listing a module's contents is  required.

Subpackages
-----------

.. autosummary::

{% if cookiecutter.include_math_plugin == 'y' -%}
pyxu.math
^^^^^^^^^
   ~pyxu.math.eigh

.. toctree::
   :maxdepth: 2
   :hidden:

   math
{% endif %}{% if cookiecutter.include_operator_plugin == 'y' -%}
pyxu.operator
^^^^^^^^^^^^^

   ~pyxu.operator.linop.Flip
   ~pyxu.operator.func.NullFunc

.. toctree::
   :maxdepth: 2
   :hidden:

   operator.func
   operator.linop

{% endif %}{% if cookiecutter.include_solver_plugin == 'y' -%}
pyxu.opt.solver
^^^^^^^^^^^^^^^
   ~pyxu.opt.solver.GradientDescent


.. toctree::
   :maxdepth: 2
   :hidden:

   opt.solver
   ../references
{% endif %}{% if cookiecutter.include_stop_plugin == 'y' -%}
pyxu.opt.stop
^^^^^^^^^^^^^

   ~pyxu.opt.stop.Deadline

.. toctree::
   :maxdepth: 2
   :hidden:

   opt.stop
{% endif %}
