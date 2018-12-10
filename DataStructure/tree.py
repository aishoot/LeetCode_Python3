#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
二叉树的节点表示以及树的创建
"""

# 通过使用Node类中定义三个属性，分别为elem本身的值，还有lchild左孩子和rchild右孩子
class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

# 树的创建,创建一个树的类，并给一个root根节点，一开始为空，随后添加节点
class Tree(object):
    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        #如果树是空的，则对根节点赋值
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            #对已有的节点进行层次遍历
            while queue:
                #弹出队列的第一个元素
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    #如果左右子树都不为空，加入队列继续判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    # 递归实现先序遍历
    def preorder(self, root):
        if root == None:
            return []
        result = [root.elem]
        left_item = self.preorder(root.lchild)
        right_item = self.preorder(root.rchild)
        return result + left_item + right_item

    # 递归实现中序遍历
    def inorder(self, root):
        if root == None:
            return []
        result = [root.elem]
        left_item = self.inorder(root.lchild)
        right_item = self.inorder(root.rchild)
        return left_item + result + right_item

    # 递归实现后序遍历
    def postorder(self, root):
        if root == None:
            return []
        result = [root.elem]
        left_item = self.postorder(root.lchild)
        right_item = self.postorder(root.rchild)
        return left_item + right_item + result

    # 利用队列实现树的层次遍历
    def breadth_travel(self, root):
        if root == None:
            return
        queue = []
        queue.append(root)
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.elem)
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)
        return result

if __name__ == "__main__":
    t = Tree()
    for i in range(10):
        t.add(i)
    print('层次遍历:', t.breadth_travel(t.root))
    print('先序遍历:', t.preorder(t.root))
    print('中序遍历:', t.inorder(t.root))
    print('后序遍历:', t.postorder(t.root))
