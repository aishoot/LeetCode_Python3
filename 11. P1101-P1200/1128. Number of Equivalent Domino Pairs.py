# My Solution
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res = 0
        if len(dominoes) < 2:
            return res
        new_lst = []
        for lst in dominoes:
            new_lst.append(str(sorted(lst)))
        counters = collections.Counter(new_lst)
        for key in counters:
            if counters[key] == 1:
                continue
            res = res + sum(range(counters[key]))
        return res

# 优化后的代码
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = dict()
        for domino in dominoes:
            a, b = sorted(domino)
            if (a, b) not in counter:
                counter[(a, b)] = 1
            else:
                counter[(a, b)] += 1
        rtn = 0
        for k, v in counter.items():  # 直接用公式求和
            rtn += (v * (v - 1)) // 2
        return rtn

# 一行代码解决问题，返回的数不能是浮点数，必须转成整型
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        return sum(v * (v - 1) // 2 for v in collections.Counter(tuple(sorted(x)) for x in dominoes).values())
