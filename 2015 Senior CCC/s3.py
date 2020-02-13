gates = [True for a in range(int(input()) + 1)]
work = 0

for a in range(int(input())):
    cur = int(input())
    broke = True
    for b in range(cur, 0, -1):
        if gates[b]:
            gates[b] = False
            broke = False
            work += 1
            break
    if broke:
        break

print(work)