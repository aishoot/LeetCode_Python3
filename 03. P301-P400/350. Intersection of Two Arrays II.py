# 使用Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        result = []
        for n in c1:
            if n in c2:
                result += [n] * min(c1[n], c2[n])
        return result

# 进一步简化
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        return [*(Counter(nums1) & Counter(nums2)).elements()]


# 解法2
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                nums2.remove(nums1[i])  # 将元素删除，解法确实妙
                result.append(nums1[i])
        return result
