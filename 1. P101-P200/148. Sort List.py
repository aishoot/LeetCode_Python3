# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 我的解法，使用堆排序
class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        import heapq
        heap = []
        while head:
            heapq.heappush(heap, head.val)
            head = head.next
        dummy = result = ListNode(0)
        while heap:
            node = ListNode(heapq.heappop(heap))
            result.next, result = node, result.next
        return dummy.next