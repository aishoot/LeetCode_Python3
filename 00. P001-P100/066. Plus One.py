# 解法1-我的最初代码-直接从末位依次相加
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = len(digits) - 1

        if digits[idx] < 9:
            digits[idx] += 1
            return digits

        digits[idx] = 0
        idx -= 1

        while idx > -1:
            digits[idx] = digits[idx] + 1
            if digits[idx] < 10:
                return digits
            else:
                digits[idx] = 0
            idx -= 1

        if digits[0] == 0:
            digits.insert(0, 1)

        return digits

# 解法2-以字符串为中间量求解
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join([str(i) for i in digits])) + 1
        return [int(i) for i in str(num)]


# 解法3-使用高级函数map
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int, str(int(''.join(map(str, digits)))+1)))


