import pytest
from move_zeros import move_zeroes


test_cases = (
    ([1, 2, 3, 0, 4, 0, 5], [1, 2, 3, 4, 5, 0, 0]),
    ([0], [0]),
    ([1], [1]),
    ([1, 2, 3], [1, 2, 3]),
    ([0, 0, 0], [0, 0, 0])
)


@pytest.mark.parametrize(('input_x', 'expected'), test_cases)
def test_move_zeroes(input_x, expected):
    move_zeroes(input_x)
    assert input_x == expected
