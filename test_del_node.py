import pytest
from del_node import delete_node
from Util import create_list_from_array, convert_list_to_array


test_cases = (
    ([1, 2, 3, 4, 5], 3, [1, 2, 4, 5]),
    ([1, 2], 1, [2])
)


@pytest.mark.parametrize(('input_arr', 'delete_num', 'expected'), test_cases)
def test_delete_node(input_arr, delete_num, expected):
    input_list = create_list_from_array(input_arr, -1)
    node = input_list
    while node.val != delete_num:
        node = node.next

    delete_node(node)
    assert convert_list_to_array(input_list) == expected
