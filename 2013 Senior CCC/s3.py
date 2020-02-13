allGames = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
scores = [-1, 0, 0, 0, 0]
favTeam = int(input())

for a in range(int(input())):
    t1, t2, s1, s2 = [int(e) for e in input().split()]
    if s1 > s2:
        scores[t1] += 3
    elif s2 > s1:
        scores[t2] += 3
    else:
        scores[t1] += 1
        scores[t2] += 1
    allGames.remove([min(t1, t2), max(t1, t2)])

def callExtrap(allGames, scores, favTeam, t1, t2, winner):
    bonusScores = scores[:]
    if winner == -1:
        bonusScores[t1] += 1
        bonusScores[t2] += 1
    else:
        bonusScores[winner] += 3

    return extrapolate(allGames, bonusScores, favTeam)

def extrapolate(allGames, scores, favTeam):
    if len(allGames) == 0:
        if scores[favTeam] == max(scores) and scores.count(scores[favTeam]) == 1: #We win!
            return 1
        return 0
    elif max(scores) - scores[favTeam] > 3 * len(allGames): # Impossible for any branches to work
        return 0
    else: #Check if all branches work
        numGames = [0, 0, 0, 0, 0]
        beatsAll = True

        for remaining in allGames:
            numGames[remaining[0]] += 1
            numGames[remaining[1]] += 1

        for team in range(1, 5):
            if team != favTeam and scores[team] + 3 * len(allGames) >= scores[favTeam]:
                beatsAll = False
                break
        
        if beatsAll: #All shall work
            return pow(3, len(allGames))

    #Branch into all 3
    playing = allGames[0]
    remGames = [e[:] for e in allGames]
    remGames.remove(playing)
    
    tot = 0
    tot += callExtrap(remGames, scores, favTeam, playing[0], playing[1], -1)
    tot += callExtrap(remGames, scores, favTeam, playing[0], playing[1], playing[0])
    tot += callExtrap(remGames, scores, favTeam, playing[0], playing[1], playing[1])

    return tot

print(extrapolate(allGames, scores, favTeam))