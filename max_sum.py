def maxSubArray(nums):
    max_sum = float('-inf')
    current_sum = 0
    for i in nums:
        current_sum += i
        if max_sum < current_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return(max_sum)

nums = [-5,-3,6,5,-1]
print(maxSubArray(nums))