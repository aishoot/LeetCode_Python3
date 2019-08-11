# My Solution
class Solution:
    def dayOfYear(self, date: str) -> int:
        def is_leap_year(year):  # year: int
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                if year % 4 == 0:
                    return True
                else:
                    return False

        year_num = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30,
                    '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}
        year = date[0:4]
        if is_leap_year(int(year)):
            year_num['02'] = 29
        month, day = date[5:7], date[8:10]
        res = 0
        for val in year_num:
            if val == month:
                break
            res += year_num[val]
        res += int(day)

        return res


# 较优解法
import datetime as dt

class Solution:
    def dayOfYear(self, date: str) -> int:
        return dt.date(*[
            int(i) for i in date.split('-')
        ]).timetuple().tm_yday

