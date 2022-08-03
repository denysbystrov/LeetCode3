"""Number 237: Delete Node in Linked List"""
from Util import ListNode


def delete_node(node: ListNode) -> None:
    while node.next.next:
        node.val = node.next.val
        node = node.next

    node.val = node.next.val
    node.next = None
