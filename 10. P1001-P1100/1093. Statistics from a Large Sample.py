# 超时版本
class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        result = []
        M = 0
        for i,x in enumerate(count):
            M = max(M,x)
            while x>0:
                result.append(i)
                x -=1
        length = len(result)
        Min,Max = result[0],result[-1]
        Mean = sum(result)/length
        Median = result[(length-1)//2] if length % 2!=0 else (result[length//2]+result[length//2-1])/2
        Mode = count.index(M)
        return [float(Min), float(Max), float(Mean), float(Median), float(Mode)]


# 较优解决方案
class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        n = sum(count)  # 多少个有效的数据
        mi = next(i for i in range(256) if count[i]) * 1.0
        ma = next(i for i in range(255, -1, -1) if count[i]) * 1.0
        mean = sum(i * v for i, v in enumerate(count)) * 1.0 / n
        mode = count.index(max(count)) * 1.0
        for i in range(255):
            count[i + 1] += count[i]
        median1 = bisect.bisect(count, (n - 1) // 2)
        median2 = bisect.bisect(count, n // 2)
        median = (median1 + median2) / 2.0
        return [mi, ma, mean, median, mode]
