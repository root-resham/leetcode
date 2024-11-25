def removeElement(nums,val):
    dist = 0
    for i in nums:
        if i != val:
            nums[dist] = i
            dist = dist+1
    return dist

nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums,val))