import math
def radix_sort(lists, radix=10):
    k = int(math.ceil(math.log(max(lists), radix)))
    bucket = [[] for i in range(radix)]
    for i in range(1, k+1):
        for j in lists:
            bucket[j // (radix ** (i-1)) % (radix ** i)].append(j)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
    return lists

alist = [54,26,93,17,77,31,44,55,20]
radix_sort(alist)
print(alist)