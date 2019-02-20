# 解法一：
class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        lengths = []
        i = j = 0
        while j < len(s):
            if s[j] in s[i:j]:
                lengths.append(j-i)
                i += 1
            else:
                j += 1
        lengths.append(j - i)
        return max(lengths) if lengths else len(s)

# 解法二
class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        maxLen = 0
        hmap = {}
        last = 0

        for i in range(len(s)):
            if s[i] in hmap:
                last = max(last, hmap[s[i]]+1)
            hmap[s[i]] = i
            maxLen = max(maxLen, i - last + 1)
        return maxLen