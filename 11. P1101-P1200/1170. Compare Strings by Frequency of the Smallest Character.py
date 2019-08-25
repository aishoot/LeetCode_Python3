# My Solution
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        from collections import Counter
        def smallest_cha(strs):
            a = Counter(strs)
            return sorted([(a[val], val) for val in a], key=lambda x:x[1])[0]

        res = []
        queries2 = [smallest_cha(val) for val in queries]
        words2 = [smallest_cha(val) for val in words]
        for val in queries2:
            res.append(len([xx for xx in words2 if xx[0] > val[0]]))

        return res

# 优化1
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        freq = []
        for i in words:
            freq.append(i.count(sorted(i)[0]))  # 用min函数更好
        def get_count(test_list, k):
            return sum([i>k for i in test_list])
        ans = []
        for i in queries:
            k = i.count(sorted(i)[0])
            ans.append((get_count(freq, k)))
        return (ans)



# 优化2
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        words_score = [word.count(min(word)) for word in words]
        queries_score = [word.count(min(word)) for word in queries]
        answer = [sum(q < w for w in words_score) for q in queries_score]

        return answer



# 使用二分搜索, 时间更短
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            return collections.Counter(s)[min(s)]
        arr = []
        for word in words:
            arr.append(f(word))
        arr = sorted(arr)
        res = []
        for q in queries:
            res.append(len(arr) - bisect.bisect_right(arr, f(q)))
        return res


