# 使用递归解法，3 condition:
# '?10' or '?20' this can only divide into '10' or '20', f(n) = f(n-2)
# '?26' this can divide into '6' or '26', f(n) = f(n-2)+f(n-1)
# '?09', '?27' this can only divide into '9' or '7', f(n) = f(n-1)
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s.startswith('0'):
            return 0
        stack = [1, 1]
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] == '0' or s[i-1] > '2':  # only '10', '20' is valid
                    return 0
                stack.append(stack[-2])
            elif 9 < int(s[i-1:i+1]) < 27:   # '01 - 09' is not allowed
                stack.append(stack[-2]+stack[-1])
            else:  # other case '01, 09, 27'
                stack.append(stack[-1])
        return stack[-1]


# 动态规划比较快
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        len_s = len(s)
        dp = [1] + [0] * len_s
        for i in range(1, len_s + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if i >= 2 and 10 <= int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[len_s]
