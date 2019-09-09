# 解法1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, total: int) -> int:
        if not root:
            return 0

        stack = [(root, [root.val])]
        num = 0

        while stack:
            node, totals = stack.pop()
            num += totals.count(total)

            if node.left:
                stack.append((node.left, [x + node.left.val for x in totals] + [node.left.val]))
            if node.right:
                stack.append((node.right, [x + node.right.val for x in totals] + [node.right.val]))
        return num


# 解法2-时间更短
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        from collections import defaultdict
        count = 0
        running_sums = defaultdict(int)
        running_sums[0] = 1
        running = 0

        def traverse(node):
            nonlocal count, running, running_sums
            if node:
                running += node.val
                count += running_sums[running - sum]
                running_sums[running] += 1

                traverse(node.left)
                traverse(node.right)

                running_sums[running] -= 1
                running -= node.val

        traverse(root)
        return count
