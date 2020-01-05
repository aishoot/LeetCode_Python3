# My solution
class Solution:
    def freqAlphabets(self, s: str) -> str:
        no, res = 0, ''
        stop = len(s)
        while no < stop:
            if no + 2 < stop and s[no + 2] == '#':
                res = res + chr(int(s[no:no + 2]) - 1 + ord('a'))
                no += 3
            else:
                res = res + chr(int(s[no]) - 1 + ord('a'))
                no += 1
        return res


# Solution 2 - 使用正则表达式
class Solution:
    def freqAlphabets(self, s: str) -> str:
        import re
        return ''.join(chr(int(i[:2]) + 96) for i in re.findall(r'\d\d#|\d', s))


# Solution 3
class Solution:
    def freqAlphabets(self, s: str) -> str:
        for i in range(26, 0, -1):
            s = s.replace(str(i) + '#' * (i > 9), chr(96 + i))
        return s
