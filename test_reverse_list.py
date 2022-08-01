import pytest
from reverse_list import reverse_list
from Util import create_list_from_array, convert_list_to_array

test_cases = (
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([1, 2], [2, 1]),
    ([1], [1]),
    ([], [])
)


@pytest.mark.parametrize(('input_arr', 'expected_arr'), test_cases)
def test_reverse_list(input_arr, expected_arr):
    input_list = create_list_from_array(input_arr, -1)
    expected_list = create_list_from_array(expected_arr, -1)
    assert convert_list_to_array(reverse_list(input_list)) == convert_list_to_array(expected_list)
