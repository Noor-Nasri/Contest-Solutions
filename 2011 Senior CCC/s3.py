filled = [(1, 0), (2, 0), (3, 0), (2, 1)]
possibly = [(1, 1), (2, 2), (3, 1)]

def checkList(List, wanted):
    for a in List:
        if a[0] == wanted[0] and a[1] == wanted[1]:
            return True
    return False


def lookingGlass(x, y, m):
    actualX = x // pow(5, m-1)
    actualY = y // pow(5, m-1)

    if checkList(filled, (actualX, actualY)):
        return "crystal"
    elif not checkList(possibly, (actualX, actualY)) or m == 1:
        return "empty"
    else:
        return lookingGlass(x - pow(5, m-1) * actualX, y - pow(5, m-1) * actualY, m - 1)

for a in range(int(input())):
    m, x, y = [int(e) for e in input().split()]
    print(lookingGlass(x, y, m))
