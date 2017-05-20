print('Enter a latitute in degrees, minutes, and seconds: ')
d = int(input('First, enter the degrees: '))
m = int(input('Next, enter the minutes of arc: '))
s = int(input('Finally, enter the seconds of arc: '))
N = 60
print(d, 'degrees,', m, 'minutes,', s, 'seconds =', (d + m / N + s / N / N), 'degrees')
