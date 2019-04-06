# 我的解法
class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        for stri in s:
            if ('a' <= stri <= 'z') or ('0' <= stri <= '9'):
                temp.append(stri)
            elif 'A' <= stri <= 'Z':
                temp.append(stri.lower())
        return temp == temp[::-1]


# 使用正则表达式
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'\W+', '', s).lower()
        return s == s[::-1]

# 另外的解法
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanlist = [c for c in s.lower() if c.isalnum()]
        return cleanlist == cleanlist[::-1]

# 或者如下：
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = list(filter(lambda x: x.isalnum(), s.lower()))
        return l == l[::-1]

# 或者如下，时间好像长点
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c.lower() for c in s if c.isalnum()])
        return s == s[::-1]