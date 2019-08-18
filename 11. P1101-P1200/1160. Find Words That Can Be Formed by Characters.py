# Solution 1
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        import copy
        from collections import Counter

        res_len = 0
        chars_dict = Counter(chars)
        for strs in words:
            a = copy.copy(chars_dict)
            flag = True
            for letter in strs:
                if letter in a and a[letter] >= 1:
                    a[letter] -= 1
                else:
                    flag = False
                    break
            if flag:
                res_len += len(strs)
        return res_len


# 简化
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter
        res = 0
        main_count = Counter(chars)
        for i in words:
            if Counter(i) & main_count == Counter(i):  # 集合求交集
                res += len(i)
        return res


# 另一种解法
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        return len(''.join(filter(lambda x : len(Counter(x) - Counter(chars)) == 0, words)))
