def bucket_sort(a):
    buckets = [0] * ((max(a) - min(a)) + 1)  # 初始化桶元素为0
    for i in range(len(a)):
        buckets[a[i] - min(a)] += 1  # 遍历数组a，在桶的相应位置累加值
    b = []
    for i in range(len(buckets)):
        if buckets[i] != 0:
            b += [i + min(a)] * buckets[i]
    return b

alist = [54,26,93,17,77,31,44,55,20]
print(bucket_sort(alist))