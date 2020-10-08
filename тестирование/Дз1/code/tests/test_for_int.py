import pytest


def test_int_without_params():
    a = int()
    assert a == 0


params1 = [3.145, 5 + 2j]


@pytest.mark.parametrize('i', params1)
def test_convert_to_int(i):
    if type(i) == complex:
        with pytest.raises(TypeError):
            assert isinstance(int(i), int)
    else:
        assert isinstance(int(i), int)


params2 = [-1, 0, 1]


@pytest.mark.parametrize('j', params2)
class TestIntConvertBool:

    def test_convert_int_to_bool(self, j):
        if j != 0:
            assert bool(j) is True
        else:
            assert bool(j) is False


def test_int_pow():
    a = 5
    b = 3
    assert a**b == 125


def test_randint_type(random_key):
    assert isinstance(random_key, int)
