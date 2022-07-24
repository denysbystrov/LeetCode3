import pytest
from Excel_col_num import title_to_number


test_cases = (
    ('A', 1),
    ('AB', 28),
    ('ZY', 701)
)


@pytest.mark.parametrize(('input_x', 'expected'), test_cases)
def test_title_to_number(input_x, expected):
    assert title_to_number(input_x) == expected
