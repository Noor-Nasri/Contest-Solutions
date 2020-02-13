instructs = input()
horiz = instructs.count("H")
vert = len(instructs) - horiz

start = [["1", "2"], 
         ["3", "4"]]

if (horiz % 2 == 1): 
    start = start[::-1]

if (vert % 2 == 1):
    start[0] = start[0][::-1]
    start[1] = start[1][::-1]

for item in start:
    print(" ".join(item))