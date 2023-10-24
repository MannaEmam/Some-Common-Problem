def seocnd_largest(num):
    first, second = -2147483648, -2147483648
    for n in num:
        if n > first:
            second = first
            first = n
        elif n > second and n != first:
            second = n
    if second == -2147483648:
        return -1
    return second
nums = [12, 35, 1, 10, 34, 1]
# nums = [10, 10, 10]
print(seocnd_largest(nums))