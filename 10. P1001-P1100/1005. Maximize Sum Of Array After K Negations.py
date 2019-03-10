# 最有解法是使用堆
import heapq
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)
        for i in range(K):
            p = heapq.heappop(A)
            if p == 0:  # 证明所有数都是非负数，可直接求和
                break
            heapq.heappush(A, -p)
        return sum(A)

# 我的代码-常规思路-时间很短
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        n = 0  # 负数个数
        for val in A:
            if val < 0:
                n += 1
        A.sort()  # 从小到大排列
        if n >= K:
            for i in range(K):
                A[i] = -A[i]
            return sum(A)
        else:
            for i in range(n):
                A[i] = -A[i]
            re = K - n
            if re % 2 == 0:  # 偶数
                return sum(A)
            else:
                return sum(A) - 2 * min(A)

# 进一步优化
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        n = len([i for i in A if i < 0])  # 负数个数
        A.sort()  # 从小到大排列
        for i in range(min(K, n)):
            A[i] = -A[i]
        if n >= K:
            return sum(A)
        else:
            if (K - n) % 2 == 0:  # 偶数
                return sum(A)
            else:
                return sum(A) - 2 * min(A)
