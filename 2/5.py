def c2f(cel):
  return cel * 1.8 + 32.0

cel = float(input('Please enter a Celsius value: '))
print('%.1f degrees Celsius is %.1f degrees Fahrenheit.'%(cel, c2f(cel)))
