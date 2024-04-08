Example Gallery
###############

.. nblinkgallery::
   :name: rst-link-gallery
   
   {% if cookiecutter.include_solver_plugin == 'y' -%}
      example_gd
   {% else %}
      placeholder
   {% endif %}