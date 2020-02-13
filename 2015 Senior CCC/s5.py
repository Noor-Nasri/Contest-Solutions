def bash(total, remainingOptions):
    if len(remainingOptions) == 0:
        return total
    elif len(remainingOptions) <= 2:
        return total + max(remainingOptions)
    
    return max(bash(total, remainingOptions[1:]), bash(total + remainingOptions[0], remainingOptions[2:]))

def maybe(entireList, index):
    if (index >= len(entireList)):
        return []
    elif (index == len(entireList) - 1):
        return [index]
    elif (index == len(entireList) - 2):
        if (entireList[index - 1] > entireList[index ]):
            return [index - 1]
        else:
            return [index]
    
    if entireList[index + 1] > entireList[index] + entireList[index + 2]:
        return ([index + 1] + maybe(entireList, index + 3))
    elif entireList[index] > entireList[index + 1]:
        return ([index] + maybe(entireList, index + 2))
    else: #expand
        fullRemain = maybe(entireList, index + 2)
        if fullRemain[0] == index + 2: #Took that one
            return [index] + fullRemain
        elif fullRemain[0] == index + 3:
            if (entireList[index - 1] > entireList[index ]):
                return [index - 1]
            else:
                return [index]

n = int(input())
sugar = [int(input()) for a in range(n)]

#ignore m for now
m = int(input())
m2 = [int(input()) for a in range(m)]

#print(bash(0, sugar))
tot1 = 0
tot2 = 0
for a in range(0, len(sugar), 2):
    tot1 += sugar[a]
    if a + 1 < len(sugar):
        tot2 += sugar[a + 1]

print(max(tot1, tot2))

#indices = maybe(sugar, 0)
#tot = 0
#for item in indices:
#    tot += sugar[item]