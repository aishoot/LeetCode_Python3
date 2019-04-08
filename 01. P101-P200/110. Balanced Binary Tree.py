# 根据深度遍历每个节点-时间复杂度较高，为NlogN
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def get_height(root):
            if root == None:
                return 0
            return 1 + max(get_height(root.left), get_height(root.right))

        if root == None:
            return True
        diff = abs(get_height(root.left) - get_height(root.right))
        if diff > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

"""
上面那个方法正确但不是很高效，因为每一个点都会被上面的点计算深度时访问一次，我们可以进行优化。
方法是如果我们发现子树不平衡，则不计算具体的深度，而是直接返回-1。
那么优化后的方法为：对于每一个节点，我们通过checkDepth方法递归获得左右子树的深度，
如果子树是平衡的，则返回真实的深度，若不平衡，直接返回-1，此方法时间复杂度O(N)，空间复杂度O(H)
"""


# 优化1
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return True if self.dfs(root) != -1 else False

    def dfs(self, root):
        if root is None:
            return 0
        lh = self.dfs(root.left)
        rh = self.dfs(root.right)
        if lh == -1 or rh == -1:
            return -1
        if abs(lh - rh) > 1:
            return -1
        return max(lh, rh) + 1

# 优化后
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root):
            if root is None:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1
