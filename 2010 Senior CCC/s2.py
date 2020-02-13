binToText = {}
checkingOrder = []

for a in range(int(input())):
    text, binary = input().split()
    binToText[binary] = text
    checkingOrder.append(binary)

checkingOrder = sorted(checkingOrder, key = len, reverse= True)
wantedDecode = input()
completedDecode = ""

while len(wantedDecode) > 0:
    for item in checkingOrder:
        if wantedDecode[:len(item)] == item:
            completedDecode += binToText[item]
            wantedDecode = wantedDecode[len(item):]

print(completedDecode)