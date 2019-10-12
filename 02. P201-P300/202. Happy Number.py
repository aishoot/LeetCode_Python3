# 解法1-暴力破解
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def count_sum(num):  # num:int
            num_lst = [int(i) ** 2 for i in str(num)]
            return sum(num_lst)

        for i in range(10):
            n = count_sum(n)
            if n == 1:
                return True
        return False


# 解法2-修改return False的条件
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True




