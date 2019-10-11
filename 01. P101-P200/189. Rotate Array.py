# My solution
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            val = nums.pop()
            nums.insert(0, val)
            k -= 1

# 解法2-整体交换位置
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:k], nums[k:] = nums[len(nums) - k:], nums[:len(nums) - k]

