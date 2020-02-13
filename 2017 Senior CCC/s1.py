input()
games1 = [0] + [int(e) for e in input().split()]
games2 = [0] + [int(e) for e in input().split()]

for a in range(1, len(games1)):
    games1[a] += games1[a-1]
    games2[a] += games2[a-1]

for b in range(len(games1) - 1, -1, -1):
    if games1[b] == games2[b]:
        print(b)
        break
    