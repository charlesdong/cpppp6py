class CandyBar(object):
    def __init__(self, name, weight, heat):
        self.name = name
        self.weight = weight
        self.heat = heat

L = [CandyBar('Mocha Munch', 2.3, 350), CandyBar('Sweet Candy Sweet', 3.0, 600), CandyBar('Yummie', 2.5, 320)]
for i, cb in enumerate(L):
    print('Candy bar %d:' % (i + 1))
    print('Name:', cb.name)
    print('Weight:', cb.weight)
    print('Heat quantity:', cb.heat)
