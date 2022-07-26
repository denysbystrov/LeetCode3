import pytest
from reverse_bits import reverse_bits


test_cases = (
    (43261596, 964176192),
    (4294967293, 3221225471),
    (4294967295, 4294967295),
    (1, 2147483648)
)


@pytest.mark.parametrize(('input_x', 'expected'), test_cases)
def test_reverse_bits(input_x, expected):
    assert reverse_bits(input_x) == expected
