x = int(input()) + 1
while True:
    testing = str(x)
    works = True
    for a in testing:
        if testing.count(a) > 1:
            works = False
            break

    if works:
        break
    x += 1

print(x)