import sys
input = sys.stdin.readline

while True:
    case = input()
    if case == '0' or case == '0\n':
        break
    
    spots, paths = [int(e) for e in case.split()]

    # Set all the pathways
    connections = [[] for a in range(spots + 1)]
    for path in range(paths):
        start, end, dist = [int(e) for e in input().split()]
        connections[start].append([end, dist])
        connections[end].append([start, dist])
    
    # Get Through
    shortestPaths = [[None, -1] for a in range(spots + 1)]
    shortestPaths[1] = [-1, -1]
    locations = [[1, 0]] #Location, cost

    while len(locations) > 0:
        newList = []
        for spot in locations:
            for pathway in connections[spot[0]]:
                newPos, newCost = [pathway[0], spot[1] + pathway[1]]
                if shortestPaths[newPos][0] == None or newCost <= shortestPaths[newPos][0]:
                    shortestPaths[newPos] = [newCost, newCost == shortestPaths[newPos][0] and shortestPaths[newPos][1] + 1 or 1]
                    newList.append([newPos, newCost])

        locations = newList

    print(shortestPaths[2][1])