# 解法1
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = collections.defaultdict(int)
        count[0] = 1
        curC, ans = 0, 0
        for n in nums:
            if n % 2:
                curC += 1
            ans += count[curC - k]
            count[curC] += 1
        return ans


# 解法2
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        lst = [-1]
        for i in range(len(nums)):
            if nums[i] % 2:
                lst.append(i)
        lst.append(len(nums))
        res = 0
        for i in range(1, len(lst) - k):
            res += (lst[i] - lst[i-1]) * (lst[i+k] - lst[i+k-1])
        return res




