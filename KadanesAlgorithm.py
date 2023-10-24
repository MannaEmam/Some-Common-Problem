from sys import maxsize


def kadanes_algorithm(num):
    max_so_far = - maxsize - 1
    max_ending_here = 0
    for n in num:
        max_ending_here += n
        max_so_far = max(max_so_far, max_ending_here)
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


nums = [-2, -3, 4, -1, -2, 1, 5, -3]
print(kadanes_algorithm(nums))
print(maxsize)


def maxSubarraySumCircular(self, num):
    max_so_far = -2147483649
    max_ending_here = total = min_ending_here = 0
    min_so_far = 2147483648

    for n in num:
        total += n
        max_ending_here = max(max_ending_here + n, n)
        max_so_far = max(max_ending_here, max_so_far)
        min_ending_here = min(min_ending_here + n, n)
        min_so_far = min(min_ending_here, min_so_far)

    return max(max_so_far, total - min_so_far) if max_so_far > 0 else max_so_far
