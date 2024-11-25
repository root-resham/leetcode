def total_planted(index,flowerbed):
    if flowerbed[index] != 0:
        return False
    left_planted = index - 1
    right_planted = index + 1
    if flowerbed[left_planted] == 1 or flowerbed[right_planted] == 1:
        return False
    else:
        return True
    

def canplace_flower(n,flowerbed):
    planted = 0
    for i in range(len(flowerbed)):
        if total_planted(i,flowerbed):
            planted += 1

    if n <= planted:
        print('true')
    else:
        print('false')

flowerbed = [1,0,0,0,1]
n = 1
canplace_flower(n,flowerbed)