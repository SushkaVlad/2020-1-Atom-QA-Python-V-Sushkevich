import pytest


@pytest.mark.regress
def test_string_type():
    a = '500'
    b = '5'
    assert type(a+b) == str


def test_string_slice(string_to_reverse):
    assert string_to_reverse[::-1] == ''.join(reversed(string_to_reverse))


class TestClassStrCount:
    a = '33'*5

    def test_str_count(self):
        assert self.a.count('3') == 10


params = [False, 5, None, 'trip']


@pytest.mark.parametrize('i', params)
def test_(i):
    assert type(str(i)) == str


@pytest.mark.regress
def test_string_format():
    a = 5
    b = "{0} is our digit".format(a)
    assert b == "5 is our digit"
