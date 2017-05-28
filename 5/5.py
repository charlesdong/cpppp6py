MONTHS = (
	'January',
	'February',
	'March',
	'April',
	'May',
	'June',
	'July',
	'August',
	'September',
	'October',
	'November',
	'December'
)

s = 0
for month in MONTHS:
	s += int(input('Enter the sales volume of %s: ' % month))
print('Sum:', s / 12)
