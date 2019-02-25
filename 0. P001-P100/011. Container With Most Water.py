class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        p, q = 0, len(height) - 1
        res = min(height[p], height[q]) * (q - p)
        t = max(height)

        while p != q and t * (q - p) > res:
            if height[p] >= height[q]:
                q -= 1
            else:
                p += 1
            res = max(res, min(height[p], height[q]) * (q - p))
        return res