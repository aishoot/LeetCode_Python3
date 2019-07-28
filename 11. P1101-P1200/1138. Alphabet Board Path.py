# 解法1
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        m = {c: [i / 5, i % 5] for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        x0, y0 = 0, 0
        res = []
        for c in target:
            x, y = m[c]
            if y < y0: res.append('L' * (y0 - y))
            if x < x0: res.append('U' * (x0 - x))
            if x > x0: res.append('D' * (x - x0))
            if y > y0: res.append('R' * (y - y0))
            res.append('!')
            x0, y0 = x, y
        return "".join(res)


# 解法2
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        r, c = 0, 0
        ret = ""
        for char in target:
            idx = ord(char) - ord('a')
            rr, cc = idx/5, idx%5
            ret += 'U'*max(0, r-rr)
            ret += 'L'*max(0, c-cc)
            ret += 'D'*max(0, rr-r)
            ret += 'R'*max(0, cc-c)
            r, c = rr, cc
            ret += '!'
        return ret
