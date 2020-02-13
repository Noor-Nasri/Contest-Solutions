num = int(input())
names = input().split()
names2 = input().split()
works = True
listings = {}
for a in range(num):
    n1, n2 = [names[a], names2[a]]
    if n1 == n2 or n1 in listings and listings[n1] != n2 or n2 in listings and listings[n2] != n1:
        works = False
        break

    listings[n1] = n2

print(works and "good" or "bad")