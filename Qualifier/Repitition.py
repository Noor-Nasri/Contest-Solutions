#import sys
import math
#input = sys.stdin.readline

for a in range(int(input())):
    line = input()
    start = line[0]
    best = len(line)

    for b in range(1, len(line)):
        if line[b] == start: #Check if this index works
            s = ""
            if b == 1:
                s = start * len(line)
                
            else: #division by 0 error
                s = line[:b] * math.ceil(len(line) / (b-1))

            if s[:len(line)] == line:
                best = b
                break

    print(best)