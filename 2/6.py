def astro(ly):
  return ly * 63240.0

ly = float(input('Enter the number of light years: '))
print(ly, 'light years =', astro(ly), 'astronomical units.')
