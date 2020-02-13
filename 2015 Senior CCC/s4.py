health, islands, routes = [int(e) for e in input().split()]
allRoutes = [[] for a in range(islands + 1)]

for route in range(routes):
    start, end, time, damage = [int(e) for e in input().split()]
    
    if damage < health:
        allRoutes[start].append([end, time, damage])
        allRoutes[end].append([start, time, damage])

begin, end = [int(e) for e in input().split()]
bestTimes = [[-1 for b in range (health)] for a in range(islands + 1)]
currentRoutes = [ [begin, set(), 0, 0] ]

while currentRoutes:
    newRoutes = []
    for point in currentRoutes:
        pos, visited, timeSpent, damageDealt = point
        if (bestTimes[pos][damageDealt] == -1 or timeSpent < bestTimes[pos][damageDealt]):
            #print("Updated best route to", pos, "as", timeSpent)
            bestTimes[pos][damageDealt] = timeSpent

            for possible in allRoutes[pos]:
                travelTo, extraTime, extraDamage = possible
                if travelTo not in visited and damageDealt + extraDamage < health:
                    # Add this route
                    copyVisit = set(visited)
                    copyVisit.add(pos)
                    newRoutes.append([travelTo, copyVisit, timeSpent + extraTime, damageDealt + extraDamage])
                    #print("Will check out", travelTo)

    currentRoutes = newRoutes
    #print(bestTimes)

lowest = -1
for a in bestTimes[end]:
    if lowest == -1 or (a != -1 and a < lowest):
        lowest = a
print(lowest)
