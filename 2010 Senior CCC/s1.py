computers = []

for item in range(int(input())):
    name, ram, cpu, storage = input().split()
    ram = int(ram)
    cpu = int(cpu)
    storage = int(storage)

    value = 2*ram + 3*cpu + storage
    computers.append([name, value])

def returnValue(i):
    extraValue = 0
    for a in range(len(i[0])):
        extraValue += ord(i[0][a])/100**a
    return i[1] - extraValue/1000

computers = sorted(computers, key = returnValue, reverse = True)
for a in range(min(len(computers), 2)):
    print(computers[a][0])