# My Solution
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        from collections import defaultdict
        invalid_tran = []
        tran_dict = defaultdict(list)

        for tran in transactions:
            tran = tran.split(',')
            if int(tran[2]) > 1000:
                invalid_tran.append(','.join(tran))
            tran_dict[tran[0]].append(tran)

        for tran in transactions:
            tran = tran.split(',')
            flag = False
            for val in tran_dict[tran[0]]:
                if abs(int(tran[1]) - int(val[1])) <= 60 and tran[3] != val[3]:
                    flag = True
            if flag:
                invalid_tran.append(','.join(tran))

        return list(set(invalid_tran))

# 优化后
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ts = []
        for t in transactions:
            name, stamp, amount, city = t.split(',')
            stamp, amount = int(stamp), int(amount)
            ts.append([name, stamp, amount, city, t])
        ans = set()
        for t in ts:
            if t[2] > 1000:
                ans.add(t[4])
            for o in ts:
                if t[0] == o[0] and abs(t[1] - o[1]) <= 60 and t[3] != o[3]:
                    ans.add(t[4])
        return list(ans)
