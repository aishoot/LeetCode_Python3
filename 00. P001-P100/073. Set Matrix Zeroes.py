# 我的代码-96 ms, faster than 60.67% of Python3
# 时间复杂度是O(M*N)，空间复杂度O(M+N)，M和N是行和列
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, colomns = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    colomns.add(j)

        for i in range(len(matrix)):
            if i in rows:
                matrix[i] = [0] * len(matrix[0])
                continue
            for j in range(len(matrix[0])):
                if j in colomns:
                    matrix[i][j] = 0

# 空间复杂度优化到O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n, firstRowZero = len(matrix), len(matrix[0]), not all(matrix[0])
        # Use first row/column as marker, scan the matrix
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        # Set the zeros
        for i in range(1, m):
            for j in range(n - 1, -1, -1):  # 第一个元素必须最后处理
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # Set the zeros for the first row，第一行标志位必须最后处理
        if firstRowZero:
            matrix[0] = [0] * n

