# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
注意原题中
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
为什么输出的是8而不是1 ？
原因是从图中的表示可以看出这两个链表中的1是不同的地址，后面的8,4,5地址则相同
"""

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        find_map = set()

        while headA:
            find_map.add(headA)  # 注意add的是headA而不是headA.val
            headA = headA.next

        while headB:
            if headB in find_map:
                return headB
            headB = headB.next

        return None

# 解法2: 技巧是把两个单链表看作是两段线段，以两条线段相加的和不变这个条件，两个指针一起来走,走过的路程是一样的
# 最后遇到的内存地址一样的就停止

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None

        A_pointer = headA
        B_pointer = headB

        while A_pointer != B_pointer:
            A_pointer = headB if A_pointer == None else A_pointer.next
            B_pointer = headA if B_pointer == None else B_pointer.next

        return A_pointer
