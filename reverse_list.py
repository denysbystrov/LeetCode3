"""Number 206: Reverse Linked List"""
from Util import ListNode
from Util import create_list_from_array


def reverse_list(head: ListNode) -> ListNode:
    current_node = head
    prev_node = None
    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    return prev_node


input_list = create_list_from_array([1, 2, 3, 4, 5], -1)
expected_list = create_list_from_array([5, 4, 3, 2, 1], -1)

print(reverse_list(input_list) == expected_list)
