def recurLights(allLight, currentLight): #check for any consecutive and turn them off
    for a in range(len(allLight) - 3):
        if all(allLight[a:a+4]): #there is a sequence now!
            b = a
            while b<len(allLight):
                if allLight[b]:
                    allLight[b] = 0
                    b += 1
                else:
                    break

    #start returning
    if currentLight == len(allLight):
        return 0
    elif allLight[currentLight]:
        return recurLights(allLight, currentLight + 1)
    
    changed = allLight[:]
    changed[currentLight] = 1
    return min(recurLights(allLight, currentLight + 1), 1 + recurLights(changed, currentLight + 1))

values = [int(input()) for e in range(int(input()))]
print(recurLights(values, 0))
