nJerseys = int(input())
nPlayers = int(input())
corres = {"S" : 1, "M": 2, "L": 3}

jerseys = [corres[input()] for a in range(nJerseys)]
works = 0
for plr in range(nPlayers):
    size, num = input().split()
    size = corres[size]
    num = int(num)

    if jerseys[num - 1] >= size:
        works += 1
        jerseys[num - 1] = -1

print(works)