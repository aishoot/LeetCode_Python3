# DFS，最容易理解，时间224ms
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(index,row,col):
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return False
            if word[index] == board[row][col]:
                board[row][col] = '#'  # 防止下一次搜索时检索到了上次相同的
                if index == len(word)-1 or \
                    dfs(index+1,row+1,col) or dfs(index+1,row-1,col) or \
                    dfs(index+1,row,col+1) or dfs(index+1,row,col-1) :
                    return True
                board[row][col] = word[index]
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(0, i, j):
                        return True
        return False


# 时间非常快-72ms, faster than 98%
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0] or not word:
            return False

        bcnts = collections.Counter(c for x in board for c in x)

        for c, cnt in collections.Counter(word).items():
            if c not in bcnts or cnt > bcnts[c]:
                return False

        m, n = len(board), len(board[0])

        def dfs(i, x, y):
            if i >= len(word):
                return True

            c = board[x][y]
            board[x][y] = ''

            if x > 0 and board[x - 1][y] == word[i] and dfs(i + 1, x - 1, y):
                return True
            if x + 1 < m and board[x + 1][y] == word[i] and dfs(i + 1, x + 1, y):
                return True
            if y > 0 and board[x][y - 1] == word[i] and dfs(i + 1, x, y - 1):
                return True
            if y + 1 < n and board[x][y + 1] == word[i] and dfs(i + 1, x, y + 1):
                return True

            board[x][y] = c
            return False

        return any(dfs(1, x, y) for x in range(m) for y in range(n) if board[x][y] == word[0])
