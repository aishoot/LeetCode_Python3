# 题目出的太烂了
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ii = -1
        while ii >= -len(nums2):
            nums1[ii] = nums2[ii]
            ii -= 1

        nums1.sort()

# 解法2-一行代码解决问题
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2)[:]