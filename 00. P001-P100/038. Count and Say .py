# 题意是n=1时输出字符串1；n=2时，数上次字符串中的数值个数，
# 因为上次字符串有1个1，所以输出11；n=3时，由于上次字符是11，有2个1，
# 所以输出21；n=4时，由于上次字符串是21，有1个2和1个1，所以输出1211。
# 依次类推，写个countAndSay(n)函数返回字符串
class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for i in range(1, n):  # 递推到n
            j, n = 0, len(res)
            n_res = ""
            while j < n:
                count = 1
                while j<n-1 and res[j]==res[j+1]:
                    count += 1
                    j += 1
                n_res += str(count) + res[j]
                j += 1
            res = n_res
        return res