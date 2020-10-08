import pytest


@pytest.mark.smoke
def test_set_intersection():
    a = {i for i in range(1, 4)}
    b = {i for i in range(3, 5)}
    assert a.intersection(b) == {3}


class TestClassSymmetricDifference:
    a = {i for i in range(1, 4)}
    b = {i for i in range(3, 5)}

    def test_set_intersection(self):
        assert self.a.symmetric_difference(self.b) == {1, 2, 4}


params1 = [{'str'}, {True}, {5}, {None}]


@pytest.mark.parametrize('i', params1)
def test_set_union(i):
    a = set()
    assert a.union(i)


params2 = ['str', True, 5, None]


@pytest.mark.parametrize('i', params2)
def test_set_add(i):
    a = set()
    a.add(i)
    assert i in a


def test_set_clear():
    a = {1, 2, 3}
    a.clear()
    assert a == set()
