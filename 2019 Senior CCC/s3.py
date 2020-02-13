def solve(mapped, xCount):
    for y in range(3):
        for x in range(3):
            if mapped[y][x] == "X":
                #check if either horz or vert can be solved
                order = None
                if (mapped[y][(x + 1) % 3] != "X" and mapped[y][(x + 2) % 3] != "X"):
                    #Solve horrizontally
                    order = mapped[y]

                elif (mapped[(y + 1) % 3][x] != "X" and mapped[(y + 2) % 3][x] != "X"):
                    #Solve horrizontally
                    order = [mapped[0][x], mapped[1][x], mapped[2][x]]

                if order != None:
                    indX = order.index("X")
                    if indX == 0:
                        mapped[y][x] = str( int(order[1]) * 2 - int(order[2]) )
                    elif indX == 1:
                        mapped[y][x] = str( (int(order[0]) + int(order[2])) //2 )
                    elif indX == 2:
                        mapped[y][x] = str( int(order[1]) * 2 - int(order[0]) )
                    xCount -= 1

                    return solve(mapped, xCount)

    return [mapped, xCount]

mapped = [input().split() for a in range(3)]
xCount = 0

for a in mapped:
    xCount += a.count("X")

while xCount > 0:
    # Try to solve
    mapped, xCount = solve(mapped, xCount)

    if xCount > 0: # Fill in X way
        for a in range(3):
            xFixing = mapped[a].count("X")
            if xFixing > 1: #Here is where we work
                if xFixing == 2:
                    for b in range(3):
                        if mapped[a][b] != "X":
                            mapped[a][(b + 1) % 3] = mapped[a][b]
                            break
                elif xFixing == 3:
                    for b in range(3):
                        mapped[a][b] = "0"

                xCount -= xFixing
                break

for item in mapped:
    print(" ".join(item))