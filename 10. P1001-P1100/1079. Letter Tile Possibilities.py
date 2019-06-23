# My Solution
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter = 0
        for num in range(1, len(tiles)+1):
            res = []
            for i in itertools.permutations(tiles, num):
                 res.append(i)
            counter += len(set(res))
        return counter


# 优化
from itertools import permutations
class Solution(object):
    def numTilePossibilities(self, tiles):
        return sum([len(set(permutations(tiles, i))) for i in range(1, len(tiles)+1)])

# 优化
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        permus = set()
        for i in range(1, len(tiles) + 1):
            permus |= set(itertools.permutations(tiles, i))
        return len(permus)

# DFS + HashSet
def numTilePossibilities(self, tiles):
    memo = set()  # avoid repeated combinations

    def helper(cur, eles):
        if cur in memo:
            return
        if cur not in memo or not eles:
            memo.add(cur)
        for i in range(len(eles)):
            helper(cur + eles[i], eles[:i] + eles[i + 1:])
        return

    helper('', tiles)
    return len(memo) - 1  # remove empty string in memo