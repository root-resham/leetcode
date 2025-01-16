arr = [1,2,3,4,5,6,7]
temp = arr[-1]

for i in range(len(arr)-1,0,-1):
    arr[i] = arr[i-1]
arr[0] = temp
print(arr)


d = 3
arr = [1,2,3,4,5,6,7]
temp = arr[len(arr)-d:]
for i in range((len(arr)-d),0,-1):
    arr[i+d-1] = arr[i-1]
j = 0
for i in range(len(temp)):
    arr[i] = temp[j]
    j += 1
print(arr)