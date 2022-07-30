import pytest
from hamming_weight import hamming_weight


test_cases = (
    (10, 2),
    (4, 1),
    (1, 1),
    (0, 0)
)


@pytest.mark.parametrize(('input_x', 'expected'), test_cases)
def test_hamming_weight(input_x, expected):
    assert hamming_weight(input_x, expected)
