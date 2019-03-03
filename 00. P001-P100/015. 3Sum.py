# 解法1：找到第一个元素，其余两个从右边剩余的两边往中间逼近
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        length = len(nums)
        for i in range(length-2):
            if nums[i] > 0:
                break
            if i>0 and nums[i]==nums[i-1]:  # 因为在nums[i-1]这一轮已跑过
                continue

            l, r = i+1, length-1
            while l<r:
                total = nums[i]+nums[l]+nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res


# 解法2
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return list(map(list, res))