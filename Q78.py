# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: ListNode) -> ListNode:
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head


# This solution iterates through the linked list and checks if the current node and the next node have the same value.
# If they do, it removes the next node by updating the next pointer of the current node to skip the next node.
# If the current node and the next node have different values, it moves on to the next node.
# This solution has a time complexity of O(n) because it visits each node in the linked list once.
# The space complexity is O(1) because it only uses a constant amount of space regardless of the size of the linked list.
