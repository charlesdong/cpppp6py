print('Enter one number per line, 0 to quit:')
x = float(input())
sum = 0.0
while x != 0.0:
  sum += x
  x = float(input())
print('Sum:', sum)
