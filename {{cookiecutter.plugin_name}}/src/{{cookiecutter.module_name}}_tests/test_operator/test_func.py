from {{cookiecutter.module_name}} import NullFunc


def test_nullfunc():
    assert NullFunc(1)._name == "ModifiedNullFunc"
