# 直接求解，超时
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        res = 0

        def is_prime(num):
            stop_num = math.sqrt(num)
            for i in range(2, int(stop_num) + 1):
                if num % i == 0:
                    return False
            return True

        for i in range(2, n):
            if is_prime(i):
                res += 1

        return res

# 改进-利用求素数中的筛选法
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        res = [True] * n
        res[0] = res[1] = False
        for i in range(2, n):
            if res[i] == True:
                for j in range(2, (n-1)//i+1):
                    res[i*j] = False
        return sum(res)


# 进一步简化
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        prime = [1] * n
        for i in range(2, n // 2 + 1):
            prime[i * i:n:i] = [0] * len(prime[i * i:n:i])

        return sum(prime) - 2
