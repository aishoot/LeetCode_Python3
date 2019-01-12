# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路1:取出每组元素后加入到一个列表后排序再加入返回链表
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lst = []
        for _, linked_list in enumerate(lists):
            while linked_list:
                lst.append(linked_list.val)
                linked_list = linked_list.next
        lst.sort()
        head = result = ListNode(None)
        for elem in lst:
            head.next = ListNode(elem)
            head = head.next
        return result.next

# 思路2: 分治算法(利用归并排序的思想，利用递归和分治法将链表数组划分成为越来越小的半链表数组，
# 再对半链表数组排序，最后再用递归步骤将排好序的半链表数组合并成为越来越大的有序链表)
# Time: O(nklogk), Space: O(logk)
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
    def mergeKLists(self, lists):
        def mergeTwoLists(l1, l2):
            curr = dummy = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next, l1 = l1, l1.next
                else:
                    curr.next, l2 = l2, l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

        def mergeKListsHelper(lists, begin, end):
            if begin > end:
                return None
            if begin == end:
                return lists[begin]
            return mergeTwoLists(mergeKListsHelper(lists, begin, (begin + end) // 2),
                                 mergeKListsHelper(lists, (begin + end) // 2 + 1, end))

        return mergeKListsHelper(lists, 0, len(lists) - 1)


# 思路3: 利用最小堆方法, Time: O(nklogk), Space: O(k)
import heapq
from random import random
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current = dummy

        heap = []
        for sorted_list in lists:
            if sorted_list:
                # 加入第2个数的原因是Python3对tuple排序时若第一个元素相同，会看第2个元素，
                # 但第2个元素是ListNode类型不支持排序，所以加入一个随机数
                heapq.heappush(heap, (sorted_list.val, random(), sorted_list))

        while heap:
            smallest = heapq.heappop(heap)[2]
            current.next = smallest
            current = current.next
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, random(), smallest.next))

        return dummy.next
