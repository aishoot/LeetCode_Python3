# 我的代码-一行代码解决问题
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return [] if root == None else self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)