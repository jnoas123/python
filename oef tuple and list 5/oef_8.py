print('Enter the scores for the test. Use -1 if you want to finish')
scores = []
times = 0
total = 0
score = float(input('score: '))
while score != -1:
    scores.append(score)
    total += score
    times += 1
    score = float(input('score: '))
scores.sort()
if times != 0:
    average = total / times
else:
    average = 0
print('The scores (ordered):', scores)
print('The average of these', times, 'scores =', average)
