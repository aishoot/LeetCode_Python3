#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 栈Stack，基本操作如下：
Stack() 创建一个新的空栈
push(item) 添加一个新的元素item到栈顶
pop() 弹出栈顶元素
peek() 返回栈顶元素
is_empty() 判断栈是否为空
size() 返回栈的元素个数
"""

class Stack():
    def __init__(self):
        self.items = []

    # 添加元素得到栈顶
    def push(self, item):
        self.items.append(item)

    # 弹出栈顶元素
    def pop(self):
        self.items.pop()

    # 返回栈顶元素
    def peek(self):
        return self.items[-1]

    # 判断栈是否为空
    def is_empty(self):
        return len(self.items) == 0

    # 返回栈中元素个数
    def size(self):
        return len(self.items)
        # return self.items == []

if __name__ == "__main__":
    stack = Stack()
    stack.push("hello")
    stack.push("world")
    stack.push("itcast")
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())