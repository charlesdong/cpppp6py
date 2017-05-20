def c2f(cel):
  return cel * 1.8 + 32.0

cel = float(input('Please enter a Celsius value: '))
print(cel, 'degrees Celsius is', c2f(cel), 'degrees Fahrenheit.')
