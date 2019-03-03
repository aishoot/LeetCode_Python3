# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 我的解法1-开辟一个新的数组，但不满足空间复杂度O(1)
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return True if result == result[::-1] else False

# 解法2步骤: 
# 1. 先找到链表中点: 用fast和slow两个指针，每次快指针走两步，慢指针走一步，等快指针走完时，慢指针的位置就是中点
# 2. 将链表后半段原地翻转，再将前半段、后半段依次比较，判断是否相等

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next

        prev = None  # head2第2段开始结点
        while head2:
            curr = head2
            head2 = head2.next
            curr.next = prev
            prev = curr

        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True