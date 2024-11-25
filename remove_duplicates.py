def removeDuplicates(nums):
    distinct = 0
    for i in range(1,len(nums)):
        if nums[distinct] != nums[i]:
            distinct = distinct+1
            nums[distinct] = nums[i]
    return distinct+1
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))