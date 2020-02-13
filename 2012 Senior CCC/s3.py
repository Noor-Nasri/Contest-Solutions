totals = [0 for a in range(1001)]
for a in range(int(input())):
    totals[int(input())] += 1

highest = max(totals)
if totals.count(highest) > 1: # same frequency exists
    print(1000 - totals[::-1].index(highest) - totals.index(highest))
else:
    valHighest = totals.index(highest)
    totals[valHighest] = 0
    secondH = max(totals)
    if totals.count(secondH) == 1:
        print(abs(valHighest - totals.index(secondH)))
    else: # pick the best frequency of those at secondH
        print(max(abs(valHighest - (1000 - totals[::-1].index(secondH))), abs(valHighest - totals.index(secondH))))