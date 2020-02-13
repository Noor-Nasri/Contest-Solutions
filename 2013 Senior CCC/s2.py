weight = int(input())
cars = [int(input()) for e in range(int(input()))]
loaded = [0, 0, 0, 0]
maximum = len(cars)

for a in range(len(cars)):
    del loaded[0]
    loaded.append(cars[a])
    if (sum(loaded) > weight): #This car makes the bridge fall
        maximum = a
        break

print(maximum)