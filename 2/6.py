def astro(ly):
  return ly * 63240

ly = int(input('Enter the number of light years: '))
print(ly, 'light years =', astro(ly), 'astronomical units.')
