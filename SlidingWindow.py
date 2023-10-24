def fixed_sliding_window(num, k):
    l = len(num)
    if l < k:
        return -1
    s = sum(num[:k])
    for i in range(k, l - k):
        temp = s - num[i - k] + num[i]
        if temp > s:
            s = temp
    return s


n = [1, 4, 2, 10, 23, 3, 1, 0, 20]

print(fixed_sliding_window(n, 4))


def dynamic_sliding_window(num, x):
    l = len(num)
    min_length, start, end, sum = l, 0, 0, 0
    while end < l:
        sum += num[end]
        end += 1
        while start < end and sum >= x:
            sum -= num[start]
            start += 1
            min_length = min(min_length, end - start + 1)
    return min_length


print(dynamic_sliding_window(n, 2))
print(float('inf'))
