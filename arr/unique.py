a = [1,1,2,2,2,3,3]

print(list(set(a)))

#for i in range(1,len(a)):
#    if a[i] != a[i-1]:
#        continue
#    else:
#        a.insert(-1,a[i])
#print(a)
def unique(a):
    index = 0
    for i in range(len(a)):
            if a[index] != a[i]:
                a[index+1] = a[i]
                index += 1
    return index+1

print(unique(a))
print(a)
