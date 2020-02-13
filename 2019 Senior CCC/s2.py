import math
answers = {}
def isPrime(n):
    if n in answers:
        return answers[n]
    
    for a in range(2,  math.ceil(n**(1/2)) + 1):
        if n%a == 0:
            answers[n] = False
            return False

    answers[n] = True
    return answers[n]

for a in range(int(input())):
    N = int(input())
    for b in range(2, N + 1):
        if isPrime(b) and isPrime(N*2 - b):
            print(b, 2*N-b)
            break