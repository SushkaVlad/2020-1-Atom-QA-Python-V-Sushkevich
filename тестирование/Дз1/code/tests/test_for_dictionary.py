import pytest


@pytest.mark.smoke
def test_dict_initialize():
    a = {}
    assert isinstance(a, dict)


class TestDictGet:
    a = {1: 'a', 2: 'b', 3: 'c'}
    key_value = 1

    def test_dict_get(self):
        assert self.a.get(1) == 'a'


def test_dict_keys(random_key):
    a = {1: 'a', 2: 'b', 3: 'c'}
    a[random_key] = 'd'
    assert random_key in a.keys()


params = [{1: 'a'}, {'a': 2}, {None: 1}, {1: 1, 2: 3}]


@pytest.mark.parametrize('i', params)
def test_set_clear(i):
    i.clear()
    assert i == {}


def test_dict_del():
    a = {1: 'a', 2: 'b', 3: 'c'}
    del a[1]
    assert 'a' not in a.values()
