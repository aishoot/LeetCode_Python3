# 最基础的思想 - 超时
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        for query in queries:
            res0 = arr[query[0]]
            for index in range(query[0] + 1, query[1] + 1):
                res0 = res0 ^ arr[index]
            res.append(res0)
        return res


# 解决方案1 -  Xor[i, j] = Xor[0, j] ^ Xor[0, i]
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]
        for i, j in queries:
            ans.append(arr[j] ^ arr[i - 1] if i > 0 else arr[j])
        return ans


# 解决方案2
class Solution:
    def xorQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(len(A) - 1):
            A[i + 1] ^= A[i]
        return [A[j] ^ A[i - 1] if i else A[j] for i, j in queries]


"""
Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8] 
"""