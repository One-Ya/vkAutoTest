import pytest

strings = [
    ['1', '2', '12'],
    ['', '', ''],
    ['\n', '\n', '\n\n']]

tuples = [
    (
        (1, 2, 3), 3
    ),
    (
        (1,), 1
    ),
    (
        (), 0
    )
]


@pytest.mark.parametrize('string', strings)
def test_str_concat(string):
    assert string[0] + string[1] == string[2]


@pytest.mark.xfail
def test_str_type():
    string = 1
    assert type(string) == type(str(string))


def test_str_exist():
    assert "s" in "string"


@pytest.mark.parametrize('tuple_iter', tuples)
def test_turple_len(tuple_iter):
    assert len(tuple_iter[0]) == tuple_iter[1]


def test_turple_edit():
    tupl = (1, 2, 3)
    try:
        tupl[1] = 2
    except TypeError:
        pass


def test_turple():
    assert (1, 2, 3) + (1, 2, 3) == (1, 2, 3, 1, 2, 3)