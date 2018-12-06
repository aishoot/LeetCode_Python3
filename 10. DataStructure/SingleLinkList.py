#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
单链表基本操作：
is_empty() 链表是否为空
length() 链表长度
travel() 遍历整个链表
add(item) 链表头部添加元素
append(item) 链表尾部添加元素
insert(pos, item) 指定位置添加元素
remove(item) 删除节点
search(item) 查找节点是否存在
"""

class SingleNode():
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList():
    def __init__(self):
        self._head = None

    # 判断链表是否为空
    def is_empty(self):
        return self._head == None

    # 计算链表长度
    def length(self):
        cur = self._head  # cur初始时指向头节点
        count = 0
        while cur != None:  # 尾节点指向None，当未到达尾部时
            count += 1
            # 将cur后移一个节点
            cur = cur.next

        return count

    # 遍历整个链表
    def travel(self):
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next

    # 头部添加元素
    def add(self, item):
        node = SingleNode(item)  # 先创建一个保存item值的节点
        node.next = self._head  # 将新节点的链接域next指向头节点，即_head指向的位置
        self._head = node  # 将链表的头_head指向新节点

    # 尾部插入元素
    def append(self, item):
        node = SingleNode(item)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_empty():
            self._head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    # 指定位置添加元素
    def insert(self, pos, item):
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(item)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length()-1):
            self.append(item)
        # 找到指定位置
        else:
            node = SingleNode(item)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self._head
            while count < (pos-1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

    # 删除节点
    def remove(self, item):
        cur = self._head
        pre = None
        while cur != None:  # 考虑到删除的不只是一个元素
            if cur.item == item:  # 找到了指定元素
                if not pre:  # 如果第一个就是删除的节点
                    self._head = cur.next  # 将头指针指向头节点的后一个节点
                else:
                    pre.next = cur.next  # 将删除位置前一个节点的next指向删除位置的后一个节点
                break
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next

    # 查找节点是否存在
    def search(self,item):
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


# 测试
if __name__ == "__main__":
    ll = SingleLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)

    print("length:",ll.length())
    ll.travel()
    print(ll.search(3))
    print(ll.search(5))
    ll.remove(1)
    print("length:",ll.length())
    ll.travel()
