# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 给的这个node前后是原链表(函数中未给出)中的, 含地址
        # 题目中给定node不是尾结点, 说明node.next肯定是存在的
        # 可以把要删除的节点，用该节点的后面节点进行覆盖，然后删掉后面那个节点就好了
        # 如ABCDE，删除C，可先用D占C的位置，变成ABDDE，再把后面的D删除，就可以得到ABDE

        node.val = node.next.val
        node.next = node.next.next
