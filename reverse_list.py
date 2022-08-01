"""Number 206: Reverse Linked List"""
from Util import ListNode
from Util import create_list_from_array


def reverse_list(head: ListNode) -> ListNode:
    if not head:
        return None

    new_head = head
    if head.next:
        new_head = reverse_list(head.next)
        head.next.next = head
    head.next = None
    return new_head


input_list = create_list_from_array([1, 2, 3, 4, 5], -1)
expected_list = create_list_from_array([5, 4, 3, 2, 1], -1)

print(reverse_list(input_list) == expected_list)
