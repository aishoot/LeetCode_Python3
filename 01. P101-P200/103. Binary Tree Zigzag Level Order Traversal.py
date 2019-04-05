# 在题102的基础山修改代码
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        ans, queue = [], [root]
        layer_num = 1
        while queue:
            level, size = [], len(queue)
            for i in range(size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 以下为增加的代码
            if layer_num % 2 == 1:
                ans.append(level)
            else:
                ans.append(level[::-1])
            layer_num += 1
        return ans

# 或者如下：
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans, level, layer_num = [], [root], 1
        while root and level:
            if layer_num % 2 == 1:
                ans.append([node.val for node in level])
            else:
                ans.append([node.val for node in level][::-1])
            level = [kid for n in level for kid in (n.left, n.right) if kid]
            layer_num += 1
        return ans