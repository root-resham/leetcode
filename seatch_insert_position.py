def searchInsert(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        if nums[i] > target:
            return i

    return len(nums)
nums = [1,3,5,6]
target = 7
print(searchInsert(nums,target))