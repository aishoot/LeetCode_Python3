# 我的解法-利用一个字典完成对列的提取
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        from collections import defaultdict
        if not matrix:
            return []
        colomns = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                colomns[j].insert(0, matrix[i][j])
        matrix.clear()
        for i in colomns:
            matrix.append(colomns[i])

# 一行代码解决问题-逆序后利用zip解包。牛逼，大神，我顶礼膜拜
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = zip(*matrix[::-1])
        # 注意不能写成 matrix = zip(*matrix[::-1])，不然返回的是最开始的matrix


# 一行代码解决问题
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[::] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix[0]))]