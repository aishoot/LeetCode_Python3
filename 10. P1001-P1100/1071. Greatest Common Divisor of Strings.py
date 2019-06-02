# My solution
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        max_str = ""
        for index1 in range(len(str1)):
            strs = str1[:(index1+1)]
            if strs * int(len(str1)/len(strs)) == str1 and strs * int(len(str2)/len(strs))== str2:
                max_str = strs
        return max_str

# Another solution
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        rtn = 0
        n1 = len(str1)
        n2 = len(str2)
        for i in range(1, min(n1, n2) + 1):
            if n1 % i == 0 and n2 % i == 0 and str1 == str1[:i] * (n1 // i) and str2 == str1[:i] * (n2 // i):
                rtn = i
        return str1[:rtn]