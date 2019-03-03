# 简洁解法一
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        chars = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        def combs(prefixes, i): # combinations
            return combs([p+c for p in prefixes for c in chars[digits[i]]], i+1) if i < len(digits) else prefixes
        return combs([''], 0) if digits else []

# 简洁解法二
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        from itertools import product
        chars = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        return [''.join(tup) for tup in product(*[chars[d] for d in digits])] if digits else []
