class Pizza(object):

	def __init__(self, company, diameter, weight):
		self.company = company
		self.diameter = diameter
		self.weight = weight

company = input('Enter the name of the pizza company: ')
diameter = float(input('Enter the diameter of the pizza: '))
weight = float(input('Enter the weight of the pizza: '))

pizza = Pizza(company, diameter, weight)
print('Company name:', pizza.company)
print('Diameter:', pizza.diameter)
print('Weight:', pizza.weight)
