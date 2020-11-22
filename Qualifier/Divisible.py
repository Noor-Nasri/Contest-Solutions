import sys
input = sys.stdin.readline

for a in range(int(input())):
    divisible, nums = [int(e) for e in input().split()]
    remainders = {0 : 1}
    summed = 0
    work = 0

    for item in (input().split()):
        summed += int(item)
        remainder = summed % divisible

        if not remainder in remainders:
            remainders[remainder] = 1
        else:
            work += remainders[remainder]
            remainders[remainder] += 1
    
    print(work)