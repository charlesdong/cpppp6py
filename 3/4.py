secs = int(input('Enter the number of seconds: '))
temp = secs
N1 = 60
N2 = 24
s = temp % N1
temp //= N1
m = temp % N1
temp //= N1
h = temp % N2
temp //= N2
d = temp
print('%d seconds = %d days, %d hours, %d minutes, %d seconds' % (secs, d, h, m, s))
