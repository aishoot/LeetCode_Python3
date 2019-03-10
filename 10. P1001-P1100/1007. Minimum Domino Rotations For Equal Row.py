# 解法1-使用计数器Counter
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        a = collections.Counter(A)
        b = collections.Counter(B)
        c = a + b
        m = c.most_common(1)[0]  # 出现次数最多的数，如(2, 7次)
        if m[1] < n:
            return -1
        cand = m[0]  # 2
        ac, bc = 0, 0
        for i in range(n):
            if cand != A[i]:
                if cand != B[i]:
                    return -1
                ac += 1
            elif cand != B[i]:
                bc += 1
        return min(ac, bc)


# 解法2-正常解法
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        for x in range(1, 7):
            ca = cb = 0
            for i in range(len(A)):
                if A[i] != x and B[i] != x:
                    break
            else:
                for i in range(len(A)):
                    if A[i] != x:
                        ca += 1
                    if B[i] != x:
                        cb += 1
                return min(ca, cb)
        return -1
