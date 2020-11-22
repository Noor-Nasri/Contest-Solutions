import sys
input = sys.stdin.readline
old = {}

while True:
    #x += 1
    try:
        case = input() #'1/' + str(x) 
        if case == '0' or case == '0\n' or len(case) <= 2:
            break

        if case in old:
            print(old[case])
            continue


        n = int(case[2:])
        works = 0

        for i in range(n + 1, n * 2 + 1):
            if ((n*i) % (i-n)) == 0:
                works += 1
        
        print(works)
        old[case] = works

    except:
        break
#print(x)