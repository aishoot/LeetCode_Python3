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

 # 另外的解法
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A, i = sorted(A), 0
        while A[i] <= 0 and K > 0:
            A[i] = -A[i]
            i += 1
            K -= 1
 
        if K == 0 or 0 in A or K % 2 == 0:
            return sum(A)
        else:
            A = sorted(A)
            return sum(A) - 2*A[0]
  
