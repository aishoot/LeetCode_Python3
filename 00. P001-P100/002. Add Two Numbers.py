# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = newLink = ListNode(None)
        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            carry, value = divmod((l1_val + l2_val + carry), 10)
            newLink.next = ListNode(value)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            newLink = newLink.next

        return head.next
