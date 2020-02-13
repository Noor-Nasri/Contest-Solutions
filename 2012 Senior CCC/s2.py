values = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
string = input()
total = 0
last = -1

for a in range(len(string)-2, -1, -2):
    summed = int(string[a]) * values[string[a+1]]
    if (last > values[string[a+1]]):
        total -= summed
    else:
        total += summed
    last = values[string[a+1]]

print(total)