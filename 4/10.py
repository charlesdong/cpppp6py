from functools import reduce

print('Please enter the scores of your three 40-yard runs:')

scores = []
for i in range(3):
	scores.append(float(input('Enter score %d: ' % (i + 1))))

print('Average score:', sum(scores) / 3.0)
