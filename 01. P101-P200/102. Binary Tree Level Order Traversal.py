# 我的代码，使用计数器记录每层的个数，BFS用队列实现
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result, queue = [], []
        if not root:
            return []
        cur_layer_num, next_layer_num = 1, 0
        queue.append(root)
        while queue:
            cur_layer = []
            for i in range(cur_layer_num):
                cur = queue.pop(0)
                cur_layer.append(cur.val)

                if cur.left != None:
                    queue.append(cur.left)
                    next_layer_num += 1
                if cur.right != None:
                    queue.append(cur.right)
                    next_layer_num += 1
            result.append(cur_layer)
            cur_layer_num = next_layer_num
            next_layer_num = 0
        return result

# 简化代码，size可以len(queue)，而不必每次都单独计算
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        ans = []
        while queue:
            level = []
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level)
        return ans

# 进一步简化
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return ans
