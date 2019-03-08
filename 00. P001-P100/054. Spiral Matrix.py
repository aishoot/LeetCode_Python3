# 解法1-使用4个点记录，比较好理解
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if matrix == []:
            return result
         
        left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1
        while left <= right and top <= bottom:
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            for i in range(top + 1, bottom):
                result.append(matrix[i][right])
            for j in reversed(range(left, right + 1)):
                if top < bottom:
                    result.append(matrix[bottom][j])
            for i in reversed(range(top + 1, bottom)):
                if left < right:  # 如果left=right会重复遍历
                    result.append(matrix[i][left])
            left, right, top, bottom = left+1, right-1, top+1, bottom-1 
        return result

# 解法-线性时间复杂度-设置已经访问的标识
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return []
        i, j, di, dj = 0, 0, 0, 1  # 起点及初始增量
        m, n = len(matrix), len(matrix[0])  # 行、列
        for v in range(m * n):  # 所有数
            res.append(matrix[i][j])
            matrix[i][j] = ''
            if matrix[(i+di)%m][(j+dj)%n] == '':
                di, dj = dj, -di  # 每次转向
            i += di
            j += dj
        return res


# 一行代码解决问题-牛逼解法，每次将矩阵逆时针旋转90度后取第一行，matrix前加*相当于C语言的指针吧
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

