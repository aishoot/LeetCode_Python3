# 二分法求解
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            if nums[lo] > target or nums[hi] < target:
                return [-1, -1]
            if nums[lo] == target and nums[hi] == target:
                return [lo, hi]
            mid = lo + (hi - lo)//2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid
                while lo >= 1 and nums[lo-1] == target:
                    lo -= 1
                hi = mid
                while hi < len(nums)-1 and nums[hi+1] == target:
                    hi += 1
                return [lo, hi]
        return [-1, -1]

# 一行代码解决问题
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [nums.index(target), len(nums)-nums[::-1].index(target)-1] if target in nums else [-1,-1]