#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 队列queue，基本操作如下：
Queue() 创建一个空的队列
enqueue(item) 往队列中添加一个item元素
dequeue() 从队列头部删除一个元素
is_empty() 判断一个队列是否为空
size() 返回队列的大小
"""

class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    # 进队列
    def enqueue(self, item):
        self.items.insert(0, item)

    # 出队列
    def dequeue(self):
        return self.items.pop()

    # 返回大小
    def size(self):
        return len(self.items)

if __name__ == "__main__":
    q = Queue()
    q.enqueue("hello")
    q.enqueue("world")
    q.enqueue("itcast")
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())