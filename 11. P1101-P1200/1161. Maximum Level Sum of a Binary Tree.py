# My Solutions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        max_index, max_value = 1, root.val
        level, summ = 0, 0
        queue = []

        queue.append(root)
        queue.append(0)
        while queue:  # BFS
            cur = queue.pop(0)
            if cur == 0:
                level += 1
                if summ > max_value:
                    max_value = summ
                    max_index = level
                summ = 0
                continue
            else:
                summ += cur.val
            if cur.left != None:
                queue.append(cur.left)
            if cur.right != None:
                queue.append(cur.right)
            if queue[0] == 0:
                queue.append(0)

        return max_index



# 解法二
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        from collections import deque
        if not root:
            return []
        queue, res = deque([root]), []

        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            res.append(cur_level)
        res = [sum(i) for i in res]

        return res.index(max(res)) + 1
