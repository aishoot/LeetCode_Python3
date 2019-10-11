class Solution:
    def titleToNumber(self, s: str) -> int:
        num = len(s)
        summ = 0
        for index, val in enumerate(s):
            value = (ord(val) - ord('A') + 1) * 26 ** (num - index - 1)
            summ += value
        return summ


# 进一步优化
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for i in s:
            res = res * 26 + ord(i) - ord('A') + 1
        return res
