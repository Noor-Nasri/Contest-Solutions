import math
nums = int(input())
tides = [int(e) for e in input().split()]
tides = sorted(tides)
lis1 = tides[:math.ceil(nums/2)] #low
lis2 = tides[math.ceil(nums/2):] #high
fixed = []
for a in range(len(lis1)):
    lowPos = lis1[len(lis1) - 1 - a]
    fixed.append(str(lowPos))

    if a < len(lis2):
        fixed.append(str(lis2[a]))

print(" ".join(fixed))