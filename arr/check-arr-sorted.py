arr = [1,2,2,4,5]

def checkArry(arr):
    for i in range(1,len(arr)):
        if arr[i] >= arr[i-1]:
            continue
        else:
           return False
    return True

print(checkArry(arr))