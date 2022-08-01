import pytest
from string_to_int import my_atoi


test_cases = (
    ("1243", 1243),
    ("     -42", -42),
    ("4193 with words", 4193),
    ("   -54  fdfe 5421", -54),
    ("   2147483649    ", 2147483647),
    ("       fkmsafo -2147483649", -2147483648),
    ("0032", 32)
)


@pytest.mark.parametrize(('input_x', 'expected'), test_cases)
def test_my_atoi(input_x, expected):
    assert my_atoi(input_x) == expected
