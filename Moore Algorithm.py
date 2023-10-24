def finding_majority_element(nums):
    vote = 0
    for num in nums:
        if vote == 0:
            candidate = num
            vote = 1
        elif num == candidate:
            vote += 1
        else:
            vote -= 1
    vote = 0
    for num in nums:
        if num == candidate:
            vote += 1
    if vote > len(nums) // 2:
        return candidate
    else:
        return -1


print(finding_majority_element([1, 2, 3, 4, 5, 4, 4, 4]))
