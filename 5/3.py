print('Enter one number per line, 0 to quit:')
x = float(input())
s = 0.0
while x != 0.0:
  s += x
  x = float(input())
print('Sum:', s)
