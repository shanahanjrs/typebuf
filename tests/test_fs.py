from typebuf.fs import load_from_yaml


def test_load_from_yaml():
    filename = 'tests/test_yaml.yaml'
    cont = load_from_yaml(filename)
    assert cont
