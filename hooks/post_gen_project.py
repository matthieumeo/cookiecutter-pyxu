#!/usr/bin/env python

import logging
import os
import shutil
import subprocess
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("post_gen_project")

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
ALL_TEMP_FOLDERS = ["licenses"]



def remove_files(filepath):
    if os.path.exists(filepath):
        if os.path.isdir(filepath):
            shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath), ignore_errors=True)
        elif os.path.isfile(filepath):
            os.remove(filepath)

def remove_temp_folders(temp_folders):
    for folder in temp_folders:
        logger.debug("Remove temporary folder: %s", folder)
        shutil.rmtree(folder, ignore_errors=True)


def remove_unrequested_plugin_examples():
    module = "{{ cookiecutter.module_name }}"
    opt_list = []
    {% for key, value in cookiecutter.items() %}
    {% if key.startswith('include_') and key.endswith("_plugin") and value != 'y' %}
    name = "{{ key }}".replace("include_", "").replace("_plugin", "")
    if name == "contrib":
        remove_files(f"src/{module}/contrib")
        remove_files(f"src/{module}_tests/test_contrib")
    elif name == "operator":
        remove_files(f"src/{module}/operator")
        remove_files(f"src/{module}_tests/test_operator")
    elif name in ["stop", "solver"]:
        remove_files(f"src/{module}/opt/{name}")
        remove_files(f"src/{module}_tests/test_opt/test_{name}.py")
        remove_files(f"doc/examples/example_gd.ipynb")
        opt_list.append(name)
        if set(opt_list) == {"stop", "solver"}:
            remove_files(f"src/{module}/opt")
            remove_files(f"src/{module}_tests/test_opt")
    else:
        remove_files(f"src/{module}/{name}")
        remove_files(f"src/{module}_tests/test_{name}.py")
    
    logger.debug(f"removing {module}/{name}.py")
    {% endif %}
    {% endfor %}

    if os.path.exists(f"doc/examples/example_gd.ipynb"):
        remove_files(f"doc/examples/placeholder.ipynb")

if __name__ == "__main__":
    remove_temp_folders(ALL_TEMP_FOLDERS)
    remove_unrequested_plugin_examples()
    msg = ''
    # try to run git init
    try:
        subprocess.run(["git", "init", "-q"])
        subprocess.run(["git", "checkout", "-b", "main"])
    except Exception:
        pass
{% if cookiecutter.install_precommit == 'y' %}
    # try to install and update pre-commit
    try:
        print("install pre-commit ...")
        subprocess.run(["pip", "install", "pre-commit"], stdout=subprocess.DEVNULL)
        print("updating pre-commit...")
        subprocess.run(["pre-commit", "autoupdate"], stdout=subprocess.DEVNULL)
        subprocess.run(["git", "add", "."])
        subprocess.run(["pre-commit", "run", "black", "-a"], capture_output=True)
    except Exception:
        pass
{% endif %}
    try:
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-q", "-m", "initial commit"])
    except Exception:
        msg += """
Your plugin template is ready!  Next steps:

1. `cd` into your new directory and initialize a git repo
   (this is also important for version control!)

     cd {{ cookiecutter.plugin_name }}
     git init -b main
     git add .
     git commit -m 'initial commit'

     # you probably want to install your new package into your environment
     
     my_env=<CONDA ENVIRONMENT NAME>
     conda create --name "${my_env}" python=3.11
     conda activate "${my_env}"
     python -m pip install -e ."""
    else:
        msg +="""
Your plugin template is ready!  Next steps:

1. `cd` into your new directory

     cd {{ cookiecutter.plugin_name }}
     # you probably want to install your new package into your environment
     
     my_env=<CONDA ENVIRONMENT NAME>
     conda create --name "${my_env}" python=3.11
     conda activate "${my_env}"
     python -m pip install -e ."""

{% if cookiecutter.install_precommit == 'y' %}
    # try to install and update pre-commit
    try:
        print("install pre-commit hook...")
        subprocess.run(["pre-commit", "install"])
    except Exception:
        pass
{% endif %}

{% if cookiecutter.github_repository_url != 'provide later' %}
    msg += """
2. Create a github repository with the name '{{ cookiecutter.plugin_name }}':
   https://github.com/{{ cookiecutter.github_username_or_organization }}/{{ cookiecutter.plugin_name }}.git

3. Add your newly created github repo as a remote and push:

     git remote add origin https://github.com/{{ cookiecutter.github_username_or_organization }}/{{ cookiecutter.plugin_name }}.git
     git push -u origin main

    """

{% else %}
    msg += """
2. Create a github repository for your plugin:
   https://github.com/new

3. Add your newly created github repo as a remote and push:

     git remote add origin https://github.com/your-repo-username/your-repo-name.git
     git push -u origin main
"""
{% endif %}
    msg += """
4. Read the README for more info: https://github.com/pyxu-org/cookiecutter-pyxu

5. We've provided a template description for your plugin page at `.pyxu-fair/DESCRIPTION.md`.
   You'll likely want to edit this before you publish your plugin to the Pyxu-FAIR (https://pyxu-org.github.io/fair/index.html).
"""

    print(msg)