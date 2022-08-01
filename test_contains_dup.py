import pytest
from contains_dup import contains_duplicate


test_cases = (
    ([1, 1, 2, 4, 5, 6], True),
    ([1, 2, 1], True),
    ([1, 2, 3, 4, 5], False),
    ([], False),
    ([1, 1], True)
)


@pytest.mark.parametrize(('input_x', 'expected'), test_cases)
def test_contains_duplicate(input_x, expected):
    assert contains_duplicate(input_x) == expected
