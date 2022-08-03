"""Number 234: Palindrome Linked List"""
from Util import ListNode, create_list_from_array


def is_palindrome(head: ListNode) -> bool:

    def reverse_list(node: ListNode) -> ListNode:
        if not node:
            return None

        new_head = node
        if node.next:
            new_head = reverse_list(node.next)
            node.next.next = node
        node.next = None
        return new_head

    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    second_list = slow
    second_list = reverse_list(second_list)
    while head and second_list:
        if second_list.val != head.val:
            return False
        head = head.next
        second_list = second_list.next

    return True


input_list = create_list_from_array([1, 2], -1)
print(is_palindrome(input_list))


