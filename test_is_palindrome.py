import pytest
from is_palindrome import is_palindrome
from Util import create_list_from_array


test_cases = (
    ([1, 2, 3, 4, 5], False),
    ([1, 2, 3, 2, 1], True),
    ([1, 2, 2, 1], True),
    ([1], True),
    ([1, 2], False)
)


@pytest.mark.parametrize(('input_arr', 'expected'), test_cases)
def test_is_palindrome(input_arr, expected):
    input_list = create_list_from_array(input_arr, -1)
    assert is_palindrome(input_list) == expected
