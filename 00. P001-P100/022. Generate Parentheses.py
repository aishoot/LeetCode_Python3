# 解法1：DFS回溯法
"""
分析：
使用回溯法，在生成的有效的字符串过程中，左括号 '(' 在前且个数大于右括号 ')' 的个数。
也就是优先生成左括号 '('，不能生成的时候就回溯到前一个位置去生成右括号 ')' ，
在生成的过程分别用 left、right 记录左右括号的个数，直至结束
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def trackback(S="", left=0, right=0):
            if len(S) == 2 * n:  # 若当前字符串的长度等于2n则字符串存入列表中
                result.append(S)
            if left < n:  # 一直添加左括号
                trackback(S + '(', left + 1, right)
            if right < left:  # 保证左括号的个数大于右括号的情况下，才能添加右括号
                trackback(S + ')', left, right + 1)
        trackback()
        return result

# 解法2：
class Solution:
    def __init__(self):
        self.dp = dict(zip((0, 1), ([''], ['()'])))

    def generateParenthesis(self, n: int) -> List[str]:
        if n not in self.dp:
            self.dp[n] = ['(' + sl + ')' + sr for m in range(n) for sl in self.generateParenthesis(m)
                          for sr in self.generateParenthesis((n - 1) - m)]
        return self.dp[n]