# Simplest Python3 Code
from copy import deepcopy
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        return deepcopy(head)

# 正常解法
# 一种是按照原链表next的顺序依次创建节点，并处理好新链表的next指针，
# 同时把原节点与新节点的对应关系保存到一个hash_map中，然后第二次循环将random指针处理好。
# 这种方法的时间复杂度是O(n)，空间复杂度也是O(n)

# 第二种方法则是在原链表的每个节点之后插入一个新的节点，这样原节点与新节点的对应关系就已经明确了，
# 因此不需要用hash_map保存，但是需要第三次循环将整个链表拆分成两个。
# 这种方法的时间复杂度是O(n)，空间复杂度是O(1)

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dic = dict()
        m = n = head
        while m:
            dic[m] = RandomListNode(m.label)
            m = m.next
        while n:
            dic[n].next = dic.get(n.next)
            dic[n].random = dic.get(n.random)
            n = n.next
        return dic.get(head)
