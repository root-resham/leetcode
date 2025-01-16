arr = [1,3,6,4,2]
index = arr[0]
for i in range(1,len(arr)):
    arr[i-1] = arr[i]
arr[-1] = index

print(arr)
