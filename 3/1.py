height = int(input('Enter your height in inches: '))
IPF = 12  # inches per feet
feets = height / IPF
inches = height % IPF
print('Your height:', feets, 'feet(s),', inches, 'inch(es).')
