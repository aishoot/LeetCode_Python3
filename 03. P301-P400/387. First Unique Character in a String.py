# 解法1
class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        count_s = Counter(s)
        for index,val in enumerate(s):
            if count_s[val] == 1:
                return index
        return -1

# 解法2-稍微慢点
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for x in s:
            if s.find(x) == s.rfind(x):
                return s.find(x)
        return -1