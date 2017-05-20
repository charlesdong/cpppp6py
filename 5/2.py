factorials = [1] * 101
for i in range(2, 101):
	factorials[i] = i * factorials[i-1]
for i, n in enumerate(factorials):
	print('%d! = %d' % (i, n))
