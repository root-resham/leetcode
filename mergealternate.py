def mergeAlternately(word1, word2):
    newnum = ''
    for i in word1:
        newnum += i
        for j in word2:
            newnum +=j
    return newnum
word1 = "ab"
word2 = "pqrs"
print(mergeAlternately(word1,word2))

