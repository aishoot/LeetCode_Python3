# 使用Python排列组合库-可以缩成一行代码
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        res = []
        for j in range(len(nums) + 1):
            for i in itertools.combinations(nums, j):
                res.append(list(i))
        return res


# 直接求解，很牛逼
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result


# 解法3-递归DFS版
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        else:
            nums.sort()
            pre_subsets = self.subsets(nums[1:])
            return pre_subsets + [[nums[0]] + elem for elem in pre_subsets]

# 解法4-使用bit mask
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(2**len(nums)):
            bit = bin(i)[2:].zfill(len(nums))  # '001'
            temp = [nums[i] for i,val in enumerate(bit) if val == '1']
            res.append(temp)
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [[nums[i] for i in range(len(nums)) if mask >> i & 1]
            for mask in range(2 ** len(nums))]
