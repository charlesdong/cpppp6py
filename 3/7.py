fe = float(input('Enter your car's fuel economy (L/100km): '))
fe = 1.0 / fe * 100.0	# km/L
fe = fe * 0.6214	# mile/L
fe = fe * 3.875		# mile/gallon
print('Your fuel economy (in MPG):', fe)
