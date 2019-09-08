# My Solution
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = []
        for index, val in enumerate(nums):
            if val == 0:
                zero_index.append(index)
        for num, val in enumerate(zero_index):
            cur = nums.pop(val - num)
            nums.append(cur)


# One line Python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:]=[x for x in nums if x!=0 ] + [i for i in nums if i==0]
