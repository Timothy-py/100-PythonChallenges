# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# SOLUTION
# This problem is similar to the "Two Sum" problem, but instead of using an array to store the numbers,
# the numbers are represented as linked lists. Here is one way to solve the problem:

# - Create a new linked list to store the sum of the two numbers.
# - Loop through both linked lists and add the values of the current nodes to each other. If the sum is greater than 9, carry the extra digit over to the next digit.
# - Create a new node in the sum linked list for each digit in the sum of the two numbers.
# - Return the sum linked list.
# Here is an example of the solution in code:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    sum_list = ListNode()
    current_node = sum_list
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        current_node.next = ListNode(carry % 10)
        current_node = current_node.next
        carry //= 10
    return sum_list.next

# This solution has a time complexity of O(n) because it loops through both linked lists only once to find the sum.
# The space complexity is O(n) because a new linked list is created to store the sum.

# l1 = [2,4,3]
# l2 = [5,6,4]
# Output = [7,0,8]
