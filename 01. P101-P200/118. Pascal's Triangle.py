# 我的代码
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        res = [[1],[1,1]]
        for i in range(2, numRows):  # 2
            level = [1]
            for j in range(1, i):  # 1
                level.append(res[i-1][j-1] + res[i-1][j])
            level.append(1)
            res.append(level)
        return res

# 优化后
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            level = [1]
            for j in range(1, i):
                level.append(res[i-1][j-1] + res[i-1][j])
            level.append(1)
            res.append(level)
        return res

# 另一种解法
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal

# 