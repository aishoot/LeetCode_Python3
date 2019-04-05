# 递归版本
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, lower, upper):
            if not node:
                return True
            if lower is not None and node.val <= lower:
                return False
            if upper is not None and node.val >= upper:
                return False
            return valid(node.left, lower, node.val) and valid(node.right, node.val, upper)
        return valid(root, None, None)

# 迭代版
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = [None]
        prev = -float("inf")
        while stack:
            while root:
                stack.append(root)
                root = root.left
            x = stack.pop()
            if x:
                if x.val <= prev:
                    return False
                prev = x.val
                root = x.right
        return True

# 中序遍历
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        result = []
        def inorder(root, result) :
            if root :
                inorder(root.left, result)
                result.append(root.val)
                inorder(root.right, result)
        inorder(root, result)
        return sorted(list(set(result))) == result  # 可能出现[1,1]这种树