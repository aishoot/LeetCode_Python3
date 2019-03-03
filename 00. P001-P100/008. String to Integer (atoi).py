class Solution:
    def myAtoi(self, strstr: str) -> int:
        sample = re.search((r'^\s*[\+,\-]?[0-9]+'), strstr)
        if sample:
            result = int(str(sample.group(0)))
            if abs(result) > 2**31-1:
                return int(-2**31) if result<0 else (2**31-1)
            else:
                return result
        else:
            return 0