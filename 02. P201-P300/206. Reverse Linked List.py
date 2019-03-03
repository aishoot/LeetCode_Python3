# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        new_head = None
        while head:
            node = ListNode(head.val)
            node.next = new_head
            new_head, head = node, head.next
        return new_head

# 另一个版本，不增加额外空间，直接在原head上修改指针(原地反转链表)
def reverseList(self, head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev

# 在上面的基础上我的另一个版本(不采用)
def reverseList(self, head):
    cur = head.next if head else None
    if head:
        head.next = None  # 断开不然会成环使程序超内存限制
    while cur:
        prev = cur
        cur = cur.next
        prev.next = head
        head = prev
    return head

# 解法2：递归版本
class Solution(object):
    def reverseList(self, head, last = None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return last
        next = head.next
        head.next = last
        return self.reverseList(next, head)
