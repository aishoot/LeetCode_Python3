# 我的代码
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if len(A) == 3:
            return True if A[0] == A[1] and A[1] == A[2] else False
        if sum(A) % 3 != 0:
            return False
        oneSum = sum(A) // 3
        summary = []
        value = 0
        for val in A:
            value += val
            summary.append(value)
        if oneSum in summary and oneSum * 2 in summary:
            fisrt_index = summary.index(oneSum)
            for ii in range(len(summary)):
                if summary[ii] == oneSum * 2 and ii > fisrt_index:
                    return True
        return False

# 优化版本
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total % 3 != 0:
            return False
        count, cumsum, target = 0, 0, total // 3
        for num in A:
            cumsum += num
            if cumsum == target:
                cumsum = 0
                count += 1
        return count == 3