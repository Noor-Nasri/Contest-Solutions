def moveStack(stacks, numberWanted, stackWanted, stackPos = None):
    #DeepStacks = stacks[:]
    if not stackPos: #Find the location
        for a in range(len(stacks)):
            if stacks[a].Find(numberWanted):
                stackPos = a
                break

    if stacks[stackPos][-1] != numberWanted: #not the number we want to move, so move this one first
      #  s1, b1 = moveStack(stacks, stacks[stackPos][-1], stackPos - 1, stackPos) 
       # s2, b2 = moveStack(stacks, stacks[stackPos][-1], stackPos + 1, stackPos) 
        #if (b1 != -1 and )
        pass
    
    
    return [stacks, 1]

stacks = []
while True:
    num = int(input())
    if num == 0:
        break
    
    stacks = [[int(e)] for e in range(8)]
    tot = 0
    for a in range(num, 0, -1):
        stacks, bonus =  moveStack(stacks, a, a - 1)
        tot += bonus

    print(tot)
    
