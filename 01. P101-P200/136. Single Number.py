# 最容易想到的基础解法
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dicts = {}
        for val in nums:
            if val not in dicts:
                dicts[val] = 1
            else:
                dicts[val] += 1

        for val in dicts:
            if dicts[val] == 1:
                return val

# 优化-使用Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = [k for k, v in c.items() if v == 1]
        return res[0]


# 最优解法1 - 相减
class Solution(object):
    def singleNumber(self, nums):
        return sum(list(set(nums)))*2 - sum(nums)


# 最优解法2 - 利用异或的结合律
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        return res
