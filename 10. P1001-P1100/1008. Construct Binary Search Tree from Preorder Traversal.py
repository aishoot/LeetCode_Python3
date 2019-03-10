# 我的代码-递归求解
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return
        head = TreeNode(preorder[0])
        left = [i for i in preorder if i < preorder[0]]
        right = [i for i in preorder if i > preorder[0]]
        # 另外解法1：或者先找到分界点i，再[:i]和[i:]分割
        #while i < len(p) and p[i] < p[0]:
        #    i += 1
        # 另外解法2：i = bisect.bisect(A, A[0])
        head.left = self.bstFromPreorder(left)
        head.right = self.bstFromPreorder(right)

        return head

