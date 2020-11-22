import math
def getNumber(n, x, y):
    if n == 0:
        return 1
    elif n == 1:
        if x == 1 and y == 1:
            return -1
        else:
            return 1
    
    cutoff = 2**(n-1)
    onExtra = [x >= cutoff, y >= cutoff]

    if onExtra[0]:
        x -= cutoff
    
    if onExtra[1]:
        y -= cutoff
    
    n -= 1

    if all(onExtra):
        return getNumber(n, x, y) * -1
    
    return getNumber(n, x, y)

for a in range(int(input())):
    n, x, y, w, h = [int(e) for e in input().split()]
    solution = []
    real_n = math.log(n, 2)

    for row in range(y, y + h):
        line = []
        for column in range(x, x + w):
            line.append(str(getNumber(real_n, column, row)))


        solution.append(" ".join(line))
    
    print("\n".join(solution))