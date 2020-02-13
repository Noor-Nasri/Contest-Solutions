questions = int(input())
answers = []

for a in range(questions):
    answers.append(input())

x = 0
for a in range(questions):
    if input() == answers[a]:
        x += 1

print(x)
