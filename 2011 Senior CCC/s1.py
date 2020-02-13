tot = 0
for a in range(int(input())):
    sentence = input()
    tot += sentence.count("T") + sentence.count("t") -  sentence.count("S") - sentence.count("s")

if (tot > 0):
    print("English")
else:
    print("French")
    
