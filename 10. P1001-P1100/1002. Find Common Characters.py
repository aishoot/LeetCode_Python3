# 解法一:使用计数器
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        import collections
        res = collections.Counter(A[0])
        for a in A:
            res &= collections.Counter(a)
        return list(res.elements())

# 一行代码解决
def commonChars(self, A):
    return list(reduce(collections.Counter.__and__, map(collections.Counter, A)).elements())