#find largest number
import sys
arr = [1,2,3,3,4,8,64,3]
largest = arr[0]
for i in range(len(arr)):
    if arr[i] > largest:
        largest = arr[i]

print(largest)
new = sorted(arr)
print(new[-1])



#
narr = [4, 5, 3, 6, 7]
greatest = 0
second = 0
smallest = narr[0]
secsmall = 0

def secondLargest(a):
    largest = a[0]
    sslargest = -1

    for i in range(len(a)):
        if a[i] > largest:
            sslargest = largest
            largest = a[i]
        elif a[i] < largest and a[i] > sslargest:
            sslargest = a[i]
    return sslargest
            
def secondSmallest(a):
    smallest = a[0]
    ssmallest = sys.maxsize
    for i in range(len(a)):
        if a[i] < smallest:
            ssmallest = smallest
            smallest = a[i]
        elif a[i] != smallest and a[i] < ssmallest:
            ssmallest = a[i]
    return ssmallest


def slargesmall(s):
    slargest = secondLargest(a)
    ssmallest =  secondSmallest(a)
    return(slargest, ssmallest)
