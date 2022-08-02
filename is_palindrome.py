"""Number 234: Palindrome Linked List"""
from Util import ListNode
import math


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

    def find_len_list(node):
        count = 0
        while node:
            count += 1
            node = node.next

        return count

    middle_point = math.ceil(find_len_list(head)/2)

    counter = 1
    second_list_head = head
    while counter <= middle_point and second_list_head:
        second_list_head = second_list_head.next
        counter += 1

    second_list_head = reverse_list(second_list_head)

    while second_list_head and head:
        if second_list_head.val != head.val:
            return False
        second_list_head = second_list_head.next
        head = head.next

    return True





