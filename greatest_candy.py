def kidsWithCandies(candies,extraCandies):
    newlist = []
    max = 0
    for i in candies:
        if i > max:
            max = i
    for i in candies:
        if (i + extraCandies) >= max:
            newlist.append(True)
        else:
            newlist.append(False)
    return newlist

candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies,extraCandies))