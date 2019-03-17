# 我的代码
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binstr = bin(N)[2:]
        comstr = ''
        for i in binstr:
            comstr += str(1-int(i))
        return int(comstr, 2)

# 优化版本
def bitwiseComplement(self, N: int) -> int:
    return int(''.join(str(1-int(c)) for c in bin(N)[2:]), 2)
