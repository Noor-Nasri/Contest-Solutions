n = int(input())
allNums = []
for a in range(n):
    num = int(input())
    if (num == 0):
        del allNums[-1]
    else:
        allNums.append(num)
print(sum(allNums))