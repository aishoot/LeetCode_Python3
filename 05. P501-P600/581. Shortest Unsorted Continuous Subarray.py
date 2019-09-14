class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sNums = sorted(nums)
        start = end = 0

        for i in range(len(nums)):
            if nums[i] != sNums[i]:
                start = i
                break

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] != sNums[i]:
                end = i
                break

        return end - start + 1 if end - start else 0

# 两行代码解决问题
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        diff = [i for i, (a, b) in enumerate(zip(nums, sorted(nums))) if a != b]
        return len(diff) and max(diff) - min(diff) + 1