# 我的代码
class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for ii in range(1, N+1):
            substr = bin(ii)[2:]
            if substr not in S:
                return False
        return True

# 优化后一行代码解决问题
class Solution:
    def queryString(self, S: str, N: int) -> bool:
        return all(S.find(bin(i)[2:]) != -1 for i in range(1, N + 1))

# 可进一步优化为
class Solution:
    def queryString(self, S: str, N: int) -> bool:
        return all(bin(i)[2:] in S for i in range(N // 2, N + 1))