def findKthLargest(nums,k):
        newnum = sorted(nums)
        return newnum[-k]

nums =  [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums,k))

#without sorting

def kth(nums):
        num = nums[0]
        for i in nums:
                if num < i:
                        num = i
        return num
print(kth(nums))