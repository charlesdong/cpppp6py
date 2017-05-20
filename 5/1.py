x = int(input('Enter an integer: '))
y = int(input('Enter another integer: '))
print('Sum between %d and %d (including %d and %d) is %d' % (x, y, x, y, sum(range(x, y+1))))
