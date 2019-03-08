# 我的代码
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        if not intervals:
            return []
        result = []
        intervals.sort(key=lambda x: x.start)
        for ii in range(1, len(intervals)):
            if intervals[ii-1].end >= intervals[ii].end:
                intervals[ii].start = intervals[ii-1].start
                intervals[ii].end = intervals[ii-1].end
            elif intervals[ii-1].end >= intervals[ii].start:
                intervals[ii].start = intervals[ii-1].start
            else:
                result.append(intervals[ii-1])
        result.append(intervals[-1])
        return result


# 优化代码
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)
        merged = []
        for interval in intervals:
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)
        return merged
