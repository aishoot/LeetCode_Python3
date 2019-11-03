# My Code
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        from collections import Counter
        if len(s1) != len(s2):
            return -1
        s1_count = Counter(s1)
        s2_count = Counter(s2)
        if (s1_count['x'] + s2_count['x']) % 2 != 0 or (s1_count['y'] + s2_count['y']) % 2 != 0:
            return -1

        x_y, y_x = 0, 0
        for ii in range(len(s1)):
            if s1[ii] == 'x' and s2[ii] == 'y':
                x_y += 1
            if s1[ii] == 'y' and s2[ii] == 'x':
                y_x += 1

        return x_y // 2 + y_x // 2 + x_y % 2 + y_x % 2


# 优化
class Solution:
    def minimumSwap(self, s1: str, s2: str, xy: int = 0, yx: int = 0) -> int:
        for a, b in zip(s1, s2):
            xy += a == 'x' and b == 'y'
            yx += a == 'y' and b == 'x'
        return xy // 2 + xy % 2 + yx // 2 + yx % 2 if xy % 2 == yx % 2 else -1




