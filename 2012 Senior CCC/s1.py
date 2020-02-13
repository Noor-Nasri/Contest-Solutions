import itertools
last_touch = int(input())

print(len(list(itertools.combinations([i for i in range(last_touch-1)], 3))))