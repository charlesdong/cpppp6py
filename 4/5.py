class CandyBar(object):
    def __init__(self, brand, weight, heat):
        self.brand = brand
        self.weight = weight
        self.heat = heat

snack = CandyBar('Mocha Munch', 2.3, 350)
print('Brand:', snack.brand)
print('Weight:', snack.weight)
print('Heat quantity:', snack.heat)
