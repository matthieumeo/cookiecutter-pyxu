# Pyxu Plugin Prompt Reference

When you run Pyxu's cookiecutter for the first time to build a Pyxu plugin,
you will be asked for some configuration options. The answers to these questions
will be used to configure certain aspects of your plugin package, such as defining
its name and license, or including preferred hooks or example components, for instance.

This document describes in detail each of the prompts, and how your answer will affect
your plugin. If you're planning on publishing your plugin to PyPI (and by extension, the
[Pyxu-FAIR](https://pyxu-org.github.io/fair/index.html)) this document provides detailed documentation
on customizing your listing.

## full_name

Name of the main author(s) of this plugin. This will appear in the `pyproject.toml` file. If you
publish your plugin to PyPI, the full_name will also be listed in the author metadata field.
If multiple names are provided, separate by comas.

## email

This is your preferred contact email address(es) and will appear in your `pyproject.toml`
file. If you publish your plugin to PyPI, this contact email address wil be
listed next to the author's name(s).
If multiple emails are provided, separate by comas.

## github_username_or_organization

This is the GitHub username under whose account the GitHub repository for the
plugin will be hosted. This username will be used to create the GitHub url
for this plugin and will appear as part of the `url` field in `pyproject.toml`.

This username could be your personal username or the organization under which
you plan to host the plugin on GitHub. If you do not wish to provide a username,
simply press `Enter` at this prompt, and choose `provide later` at the
`github_repository_url` prompt - this will omit the `url` field in `pyproject.toml`
entirely, and you may add it later if you wish.

## plugin_name

This is the desired name for your Pyxu plugin, and will also be the name
of the Python package directory we create for you. The plugin name you choose
will be listed in `pyproject.toml` under the `name` field, as well as under
`[options.entry_points]`. If you publish your package to PyPI, users will be able
to install your package using

```
pip install plugin_name
```

The convention for these packages is that they should have short, all-lowercase
names, with hyphens preferred over underscores for separating words. Note that
for user-facing text, Pyxu and the Pyxu-FAIR will use the `display_name` (below).

## github_repository_url

This will be the code repository link that is stored in the `url` field in
`pyproject.toml`. The default option is generated using your `github_username_or_organization` and `plugin_name`.

Choose `provide later` at this prompt if the default generated url is incorrect,
or if you do not wish to provide a url at all. You can then add this link to your
`setup.cfg` later, under the `url` field.

## display_name

User-facing text to display as the name of this plugin. For example, this will be
used by the Pyxu-FAIR. It should be 3-40 characters long. 

## short_description

This should be a short description of what your plugin does. It will be listed
in `pyproject.toml` under the `description` field. If you publish your plugin to PyPI,
this description will also be listed alongside your package name in search results.

## include_operator_plugin

Choosing `"y"` for this prompt will create an example reader implementation
inside your plugin's module in the file `_operator.py`. You can then edit the code in this
file to write your mathematical operator. For more information on Linear operators see the
[specification reference][reader-spec].


This will install [pre-commit](https://pre-commit.com) for you. 

## license

This prompt allows you to choose from a variety of open source licensing options
for your plugin. Choosing any of the options will lead to a boilerplate `LICENSE`
file being added to the root of your plugin directory, as well as the [SPDX identifier](https://spdx.org/licenses/)
for that license being listed in your `pyproject.toml` under the `license` field.

License options include: [BSD-3], [MIT], [MPL v2.0], [Apache v2.0], [GNU GPL v3.0], or [GNU LGPL v3.0]

[glob pattern]: https://en.wikipedia.org/wiki/Glob_(programming)
[mit]: http://opensource.org/licenses/MIT
[mpl v2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[bsd-3]: http://opensource.org/licenses/BSD-3-Clause
[gnu gpl v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[gnu lgpl v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[apache v2.0]: http://www.apache.org/licenses/LICENSE-2.0

