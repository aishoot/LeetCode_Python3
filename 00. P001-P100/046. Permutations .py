"""
全排列算法，此部分可以见笔记
"""
# 1。 我的代码-两行代码解决问题
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        return [seq for seq in permutations(nums)]

# 2. 字典序生成-需要修改

# 3. 递归思想
def permutations(arr, position, end):
    if position == end:
        print(arr)
    else:
        for index in range(position, end):
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position + 1, end)
            arr[index], arr[position] = arr[position], arr[index]

arr = [1, 2, 3]
permutations(arr, 0, len(arr))

## 4. 深度优先算法
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)

## 5. 递归-take any number as first. Take any number as the first number and
# append any permutation of the other numbers.
def permute(self, nums):
    return [[n] + p
            for i, n in enumerate(nums)
            for p in self.permute(nums[:i] + nums[i+1:])] or [[]]

## 6. 递归-insert first number anywhere. Insert the first number anywhere in
# any permutation of the remaining numbers.
def permute(self, nums):
    return nums and [p[:i] + [nums[0]] + p[i:]
                     for p in self.permute(nums[1:])
                     for i in range(len(nums))] or [[]]

# Reduce, insert next number anywhere
def permute(self, nums):
    return reduce(lambda P, n: [p[:i] + [n] + p[i:]
            for p in P for i in range(len(p)+1)], nums, [[]])





