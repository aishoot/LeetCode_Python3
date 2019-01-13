# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 我的解法，利用了一个额外数据结构
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        counter = set()
        while head:
            if head in counter:
                return True
            else:
                counter.add(head)
            head = head.next

        return False

# 递归版本, 没有利用任何额外空间
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        if head.val == "visited":
            return True
        head.val = "visited"
        return self.hasCycle(head.next)

# 直接跑
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while fast and fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True
        return False