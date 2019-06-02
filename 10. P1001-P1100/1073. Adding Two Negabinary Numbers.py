# My solution-大数时出现错误
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def bi2dec(arrs):  # 负二进制转换为十进制
            res = 0
            for index in range(len(arrs)):
                res += arrs[len(arrs) - 1 - index] * ((-2) ** index)
            return res

        def dec2bi(num):  # 十进制转化为负二进制，这部分有问题；十进制转化为-2进制可参考题目 1017.Convert to Base -2
            res = []
            if num == 0:
                return [0]
            while num != 0:
                yu = num % 2
                res.append(int(yu))
                #shang = (num - yu) / (-2)   # 问题在这个地方
                shang = (num - yu) // (-2)
                num = shang
            return res[::-1]

        return dec2bi(bi2dec(arr1) + bi2dec(arr2))

# 优化后没问题
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def conv1(arr):
            cur = 1
            ans = 0
            arr.reverse()
            for i in arr:
                ans += cur * i
                cur *= -2
            return ans

        def conv2(n):
            out = []
            if n == 0:
                return [0]
            while n != 0:
                n, rem = divmod(n, -2)
                if rem < 0:
                    n += 1
                    rem -= -2
                out.append(rem)
            return out[::-1]

        return conv2(conv1(arr1) + conv1(arr2))


#
class Solution(object):
    def addNegabinary(self, arr1, arr2):
        count = [0] * 2000
        n1 = len(arr1)
        n2 = len(arr2)
        for i, x in enumerate(arr1):
            actual = n1 - i - 1
            if x:
                count[actual] += 1
        for i, x in enumerate(arr2):
            actual = n2 - i - 1
            if x:
                count[actual] += 1
        for i in range(1500):
            while count[i] > 1:
                if count[i + 1]:
                    count[i] -= 2
                    count[i + 1] -= 1
                else:
                    count[i] -= 2
                    count[i + 1] += 1
                    count[i + 2] += 1
        count.reverse()
        if 1 not in count:
            return [0]
        return count[count.index(1):]

