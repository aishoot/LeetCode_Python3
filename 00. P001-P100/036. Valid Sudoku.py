#  我的思维比较直，先读取出所有元素，再用Counter判断；下面的方法巧用了数据结构-字典
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        N = len(board)
        row_cache = defaultdict(set)
        column_cache = defaultdict(set)
        grid_cache = defaultdict(set)

        for y in range(N):  # 0,1,...,8
            for x in range(N):  # 0,1,..,8
                num = board[y][x]

                if num == '.':
                    continue

                if num in column_cache[x]:
                    return False
                else:
                    column_cache[x].add(num)

                if num in row_cache[y]:
                    return False
                else:
                    row_cache[y].add(num)

                i = (y // 3) * 3 + x // 3
                if num in grid_cache[i]:
                    return False
                else:
                    grid_cache[i].add(num)
        return True
