# 方案1-使用哈希表
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c = collections.Counter()
        res = 0
        for t in time:
            res += c[-t % 60]
            c[t % 60] += 1
        return res

# 或者下面的写法
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        memo = collections.Counter()
        res = 0
        for t in time:
            t %= 60
            res += memo[(60-t)%60]
            memo[t] += 1
        return res





