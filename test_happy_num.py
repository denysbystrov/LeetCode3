import pytest
from happy_num import is_happy


test_cases = (
    (19, True),
    (10, True),
    (2, False),
    (0, False)
)


@pytest.mark.parametrize(('input_x', 'expected'), test_cases)
def test_is_happy(input_x, expected):
    assert is_happy(input_x) == expected
