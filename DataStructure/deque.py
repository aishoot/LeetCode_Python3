#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 双端队列dequeue，基本操作如下：
Deque() 创建一个空的双端队列
add_front(item) 从队头加入一个item元素
add_rear(item) 从队尾加入一个item元素
remove_front() 从队头删除一个item元素
remove_rear() 从队尾删除一个item元素
is_empty() 判断双端队列是否为空
size() 返回队列的大小
"""

class Deque(object):
    def __init__(self):
        self.items = []

    # 判断队列是否为空
    def is_empty(self):
        return self.items == []

    # 在队头添加元素
    def add_front(self, item):
        self.items.insert(0, item)

    # 在队尾添加元素
    def add_rear(self, item):
        self.items.append(item)

    # 从队头删除元素
    def remove_front(self):
        return self.items.pop(0)

    # 从队尾删除元素
    def remove_rear(self):
        return self.items.pop()

    # 返回队列大小
    def size(self):
        return len(self.items)


if __name__ == "__main__":
    deque = Deque()
    deque.add_front(1)
    deque.add_front(2)
    deque.add_rear(3)
    deque.add_rear(4)
    print(deque.size())
    print(deque.remove_front())
    print(deque.remove_front())
    print(deque.remove_rear())
    print(deque.remove_rear())