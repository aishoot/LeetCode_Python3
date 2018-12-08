#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 双向链表，基本操作如下：
is_empty() 链表是否为空
length() 链表长度
travel() 遍历链表
add(item) 链表头部添加
append(item) 链表尾部添加
insert(pos, item) 指定位置添加
remove(item) 删除节点
search(item) 查找节点是否存在
"""

class Node():
    def __init__(self, item):
        self.item = item
        self.next = None
        self.pre = None

# 双向链表
class DLinkList(object):
    def __init__(self):
        self._head = None

    # 判断链表是否为空
    def is_empty(self):
        return self._head == None

    # 返回链表的长度
    def length(self):
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    # 遍历链表
    def travel(self):
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next

    # 头部插入元素
    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node  # 如果是空链表，将_head指向node
        else:
            node.next = self._head  # 将node的next指向_head的头节点
            self._head.prev = node  # 将_head的头节点的prev指向node
            self._head = node  # 将_head 指向node

    # 尾部插入元素
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node  # 如果是空链表，将_head指向node
        else:
            cur = self._head  # 移动到链表尾部
            while cur.next != None:
                cur = cur.next
            cur.next = node  # 将尾节点cur的next指向node
            node.prev = cur  # 将node的prev指向cur


    # 查找元素是否存在
    def search(self, item):
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    # 在指定位置添加节点
    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            # 移动到指定位置的前一个位置
            while count < (pos-1):
                count += 1
                cur = cur.next

            node.prev = cur  # 将node的prev指向cur
            node.next = cur.next  # 将node的next指向cur的下一个节点
            cur.next.prev = node  # 将cur的下一个节点的prev指向node
            cur.next = node  # 将cur的next指向node

    # 删除元素
    def remove(self, item):
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur.item == item:
                if cur.next == None:  # 如果首节点的元素即是要删除的元素
                    self._head = None  # 如果链表只有这一个节点
                else:
                    cur.next.prev = None  # 将第二个节点的prev设置为None
                    self._head = cur.next  # 将_head指向第二个节点
                return
            while cur != None:
                if cur.item == item:
                    cur.prev.next = cur.next  # 将cur的前一个节点的next指向cur的后一个节点
                    cur.next.prev = cur.prev  # 将cur的后一个节点的prev指向cur的前一个节点
                    break
                cur = cur.next

if __name__ == "__main__":
    ll = DLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print("length:",ll.length())
    ll.travel()
    print(ll.search(3))
    print(ll.search(4))
    ll.remove(1)
    print("length:",ll.length())
    ll.travel()
