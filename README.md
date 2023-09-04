# cookiecutter-pyxu

[Cookiecutter] template for authoring [pyxu] plugins.

**NOTE: This repo is not meant to be cloned/forked directly! Please read "Getting Started" below**

## Getting Started

### Create your plugin package

Install [Cookiecutter] and generate a new Pyxu plugin project:

```bash
pip install cookiecutter
cookiecutter https://github.com/matthieumeo/cookiecutter-pyxu
```

Cookiecutter prompts you for information regarding your plugin
(A new folder will be created in your current working directory):

```bash
full_name [Pyxu Developer]: Isaac Newton
email [yourname@example.com]: inewton@trinity.uk
github_username_or_organization [githubuser]: sirisaac
# NOTE: for packages whose primary purpose is to be a Pyxu plugin, we
# recommend using the 'pyxu-' prefix in the package name.
# If your package provides functionality outside of Pyxu, you may
# choose to leave Pyxu out of the name.
plugin_name [pyxu-foobar]: pyxu-gradient-descent
Select github_repository_url:
1 - https://github.com/sirisaac/pyxu-gradient-descent
2 - provide later
Choose from 1, 2 [1]:
module_name [pyxu_gradient_descent]:
display_name [Pyxu FooBar Collection]: Gradient Descent
short_description [A simple plugin to use the FooBar collection within Pyxu]: A simple gradient descent solver for Pyxu 
# you can select from various plugin template examples
include_math_plugin [y]: n
include_operator_plugin [n]: 
include_solver_plugin [n]:y
include_stop_plugin [n]: n
include_contrib_plugin [n]: n
use_git_tags_for_versioning [n]:
install_precommit [n]: 
Select license:
1 - BSD-3
2 - MIT
3 - Mozilla Public License 2.0
4 - Apache Software License 2.0
5 - GNU LGPL v3.0
6 - GNU GPL v3.0
Choose from 1, 2, 3, 4, 5, 6 [1]:

```

You just created a minimal Pyxu plugin, complete with tests
and ready for automatic deployment!

For more detailed information on each prompt see the [prompts reference](./PROMPTS.md).

```no-highlight
pyxu-gradient-descent/
├── .git
├── .github
│         └── workflows
│             └── test_and_deploy.yml
├── .gitignore
├── __init__.py
├── LICENSE
├── MANIFEST.in
├── .pre-commit-config.yaml
├── .pyxu-fair
│         ├── config.yml
│         └── DESCRIPTION.md
├── pyproject.toml
├── README.md
├── setup.cfg
├── src
│         ├── __init__.py
│         ├── pyxu_gradient_descent
│         │       ├── __init__.py
│         │       └── opt
│         │           ├── __init__.py
│         │           └── solver
│         │               └── __init__.py
│         └── pyxu_gradient_descent_tests
│             ├── __init__.py
│             └── test_opt
│                 ├── __init__.py
│                 └── test_solver.py
└── tox.ini

```

### Initialize a git repository in your package

NOTE: This is important not only for version management, but also if you want to
pip install your package locally for testing with `pip install -e .`. (because
the version of your package is managed using git tags,
[see below](#automatic-deployment-and-version-management))

```bash
cd pyxu-gradient-descent
git init
git add .
git commit -m 'initial commit'
```

### Upload it to GitHub

1. Create a [new github repository] with the name `github_repository_url` you indicated.

2. Add your newly created GitHub repo as a remote and push:

   ```bash
   # here, continuing with the example above...
   # but replace with your own username and repo name

   git remote add origin https://github.com/sirisaac/pyxu-gradient-descent.git
   git push -u origin main
   ```
   
### Setup a local environment

It is recommended to set up a local Python environment to develop and test your plugin. With [conda], you can use:
   ```bash
   my_env=<CONDA ENVIRONMENT NAME>
   conda create --name "${my_env}" python=3.11
   conda activate "${my_env}"
   python -m pip install -e .

   ```
You will probably want to install your new package into this environment. ``Pyxu`` is already set as a dependency,
simply add the other required dependencies in the ``setup.cfg`` file and run the following commands.
   ```bash
   cd <your-repo-name>
   python -m pip install -e .
   ```

## Develop new features

The cookiecutter offers a predefined hierarchy of classes and functions to aid novice Pyxu developers in creating 
novel features. At this point, the developer can create new functionalities following the [pyxu_dev_notes] and 
structure predefined by the cookiecutter.

## Continuous Integration

This Pyxu-plugin generator repository provides you with already-parametrized continuous integration tools.

### Pre-commit

This template includes a default yaml configuration for [pre-commit](https://pre-commit.com/).
Among other things, it includes checks for best practices in Pyxu plugins.
You may edit the config at `.pre-commit-config.yaml`

To use it run:

```bash
pip install pre-commit
pre-commit install
```

You can also have these checks run automatically for you when you push to GitHub
by installing [pre-commit ci](https://pre-commit.ci/) on your repository.


### Running tests locally

You can run your tests locally with [tox] and [pytest].
You'll need to make sure that your package is installed in your environment,
along with testing requirements (specified in the setup.cfg `extras_require` section):

   ```bash
   tox run
   ```

### Monitor testing and coverage

The repository is already setup to run your tests automatically each time you push an
update (configuration is in `.github/workflows/test_and_deploy.yml`). You can
monitor them in the "Actions" tab of your GitHub repository. If you're
following along, go have a look... they should be running right now!

When the tests are done, test coverage will be viewable at
[codecov.io](https://codecov.io/) (assuming your repository is public):
`https://codecov.io/gh/<your-github-username>/<your-package-name>`

### Set up automatic deployments

Your new package is also nearly ready to automatically deploy to [PyPI]
(whenever you create a tagged release), so that your users can simply `pip install` your package. To do so, you just need to create an [API token to authenticate
with PyPi](https://pypi.org/help/#apitoken), and then add it to your GitHub
repository:

1. If you don't already have one, [create an account](https://pypi.org/account/register/) at [PyPI]
2. Verify your email address with PyPI, (if you haven't already)
3. Generate an [API token](https://pypi.org/help/#apitoken) at PyPi: In your
   [account settings](https://pypi.org/manage/account/) go to the API tokens
   section and select "Add API token". Make sure to copy it somewhere safe!
4. [Create a new encrypted
   secret](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets#creating-encrypted-secrets)
   in your GitHub repository with the name "TWINE_API_KEY", and paste in your
   API token.

You are now setup for automatic deployment!

### Automatic deployment and version management

Each time you want to deploy a new version, you just need to create a tagged
commit, and push it to your main branch on GitHub. Your package is set up to
use [setuptools_scm](https://github.com/pypa/setuptools_scm) for version
management, meaning you don't need to hard-code your version anywhere in your
package. It will be inferred from the tag each time you release. The deployment 
is also handled with the [github actions] using the same workflow file `.github/workflows/test_and_deploy.yml`.

```bash
# the tag will be used as the version string for your package
# make it meaningful: https://semver.org/
git tag -a v0.1.0 -m "v0.1.0"

# make sure to use follow-tags so that the tag also gets pushed to github
git push --follow-tags
```

> Note: as of git 2.4.1, you can set `follow-tags` as default with
> `git config --global push.followTags true`

Monitor the "actions" tab on your GitHub repo for progress... and when the
"deploy" step is finished, your new version should be visible on pypi:

`https://pypi.org/project/<your-package-name>/`

and available for pip install with:

```bash
# for example
pip install pyxu-gradient-descent
```

### Create your documentation

The documentation generation is generated with [Sphinx], based on the [Pydata-Sphinx-Theme].
You can edit the `docs/index.rst` file to add your own documentation.

## Summary of the features

- Installable [PyPI] package
- [tox] test suite, testing various python versions and platforms.
- `README.md` file that contains useful information about your plugin
- Continuous integration configuration for [github actions] that handles testing
  and deployment of tagged releases
- git-tag-based version management with [setuptools_scm]
- Optional documentation with either [Sphinx] or [MkDocs]
- Choose from several licenses, including [BSD-3], [MIT], [MPL v2.0], [Apache
  v2.0], [GNU GPL v3.0], or [GNU LGPL v3.0]

## Resources

Please consult the [pyxu plugin docs](https://pyxu-org.github.io/fair/contribute.html) for more information on how to create a plugin.

Details on why this plugin template is using the `src` layout can be found [here](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure) and [here](https://hynek.me/articles/testing-packaging/)

## Issues

If you encounter any problems with this cookiecutter template, please [file an
issue] along with a detailed description.

## License

Distributed under the terms of the [BSD-3] license, `cookiecutter-pyxu`
is free and open source software.

[pyxu organization]: https://github.com/matthieumeo/pyxu/
[documentation]: https://pyxu-org.github.io/fair/contribute.html "Documentation"
[cookiecutter]: https://github.com/audreyr/cookiecutter
[pyxu]: https://github.com/matthieumeo/pyxu
[pyxu_dev_notes]: https://pyxu-org.github.io/fair/dev_notes.html
[pypi]: https://pypi.org/
[tox]: https://tox.readthedocs.io/en/latest/
[pytest]: https://docs.pytest.org/en/7.1.x/
[file an issue]: https://github.com/pyxu/cookiecutter-pyxu/issues
[sphinx]: https://www.sphinx-doc.org/en/master/usage/quickstart.html
[Pydata-Sphinx-Theme]: https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html
[mit]: http://opensource.org/licenses/MIT
[mpl v2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[bsd-3]: http://opensource.org/licenses/BSD-3-Clause
[gnu gpl v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[gnu lgpl v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[apache v2.0]: http://www.apache.org/licenses/LICENSE-2.0
[github actions]: https://github.com/features/actions
[new github repository]: https://help.github.com/en/github/getting-started-with-github/create-a-repo
[setuptools_scm]: https://github.com/pypa/setuptools_scm
[conda]: https://docs.conda.io/en/latest/
