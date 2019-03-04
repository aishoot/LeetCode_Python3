# 解法1
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        first = 1
        store = {}
        for i in range(0, len(nums)):
            if nums[i] > 0:
                store[nums[i]] = True
                if nums[i] == first:
                    while first in store:
                        first += 1
        return first

# 解法2-我的代码
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums or max(nums) <= 0:
            return 1
        for ii in range(1, int(max(nums))+2):
            if ii not in nums:
                return ii