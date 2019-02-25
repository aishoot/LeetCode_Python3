# Manacher算法(时间复杂度是O(N))
class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n - 1):
            P[i] = (R > i) and min(R - i, P[2 * C - i])
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            if i + P[i] > R:
                C, R = i, i + P[i]

        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]

# 我的代码
class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        length = len(s)  # 5
        if length == 0 or length == 1:
            return s

        max_str = ""
        for ll in range(length - 1, -1, -1):  # 4
            for ii in range(length - ll):  # 1
                strs = s[ii:ii + ll + 1]
                if strs == strs[::-1]:
                    return strs

# 动态规划-C++版，参考https://www.jianshu.com/p/c82cada7e5b0
#include <iostream>
#include <cstring>
using namespace std;

string longestPalindrome(string s)
{
    const int n = s.size();
    bool dp[n][n];
    memset(dp, 0, sizeof(dp));

    int maxlen = 1;     //保存最长回文子串长度
    int start = 0;      //保存最长回文子串起点
    for(int i = 0; i < n; ++i)
    {
        for(int j = 0; j <= i; ++j)
        {
            if(i - j < 2)
            {
                dp[j][i] = (s[i] == s[j]);
            }
            else
            {
                dp[j][i] = (s[i] == s[j] && dp[j + 1][i - 1]);
            }

            if(dp[j][i] && maxlen < i - j + 1)
            {
                maxlen = i - j + 1;
                start = j;
            }
        }
    }

    return s.substr(start, maxlen);
}

int main()
{
    string s;
    cout << "Input source string: ";
    cin >> s;
    cout << "The longest palindrome: " << longestPalindrome(s);
    return 0;
}
