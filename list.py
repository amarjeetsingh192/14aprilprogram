##Finding the Maximum Number in a List

numberList = [15, 85, 35, 89, 125,2000]

maxNum = numberList[0]
for num in numberList:
    if maxNum < num:
        maxNum = num
print(maxNum)

