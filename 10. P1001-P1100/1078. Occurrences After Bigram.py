# My Solution
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        text_split = text.split()
        if len(text_split) <= 2:
            return res
        for index in range(len(text_split)-2):
            if text_split[index] == first and text_split[index+1] == second:
                res.append(text_split[index+2])
        return res

# 优化
def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
    ws = text.split()
    return [ws[i + 2] for i in range(len(ws) - 2) if ws[i] == first and ws[i + 1] == second]