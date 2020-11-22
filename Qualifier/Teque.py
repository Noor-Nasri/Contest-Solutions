import sys
import collections
input = sys.stdin.readline

lis1 = collections.deque([])
lis2 = collections.deque([])

for a in range(int(input())):
    command, value = input().split()
    value = int(value)

    if command == "get":
        if value < len(lis1):
            print(lis1[value])
        else:
            print(lis2[value - len(lis1)])

    elif command == "push_back":
        lis2.append(value)

        if len(lis2) > len(lis1):
            lis1.append(lis2.popleft())
    
    elif command == "push_front":
        lis1.appendleft(value)

        if len(lis1) > len(lis2) + 1:
            lis2.appendleft(lis1.pop())
    
    elif command == "push_middle":
        if len(lis1) == len(lis2):
            lis1.append(value)
        else: #lis2 is 1 smaller than lis1
            lis2.appendleft(value)