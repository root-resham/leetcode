#brute
d = 3
arr = [1,2,3,4,5,6,7]
new = arr[:d]

for i in range(d,len(arr)):
    arr[i-d] = arr[i]

j = 0
for i in range(len(arr)-d,len(arr)):
    arr[i] = new[j]
    j += 1
print(arr)

#second_way(better)

d = 3
arr = [1,2,3,4,5,6,7]
new = arr[:d]

for i in range(d,len(arr)):
    arr[i-d] = arr[i]

for i in range(len(arr)-d,len(arr)):
   arr[i] = new[i-(len(arr)-d)]             #arr[4] = new[4-(7-3)] so arr[4] = new[0] for first time of running loop

print(arr)

#using slicing
d = 7
arr = [1,2,3,4,5,6,7]
if d > len(arr):
    d = d % len(arr)
else:
    d = d
new = arr[:d]
new1 = arr[d:]
arr = new1+new
print(arr)
