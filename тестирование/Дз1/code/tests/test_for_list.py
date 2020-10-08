import pytest


def test_list_generator():
    a = [i ** 2 for i in range(1, 4)]
    assert a == [1, 4, 9]


def test_list_sort():
    a = [1, 0, -1]
    a.sort()
    assert a == [-1, 0, 1]


params = [['sf'], [5], [True], [None]]


@pytest.mark.parametrize('i', params)
def test_list_extend(i):
    a = []
    a.extend(i)
    assert a


class TestClassInsertIndex:

    def test_list_insert(self):
        a = [-1, 0, 1]
        index = 1
        value = 'str'
        a.insert(index, value)
        assert a == [-1, 'str', 0, 1]

    def test_list_index(self):
        a = [-1, 0, 1]
        value = -1
        assert a.index(value) == 0
