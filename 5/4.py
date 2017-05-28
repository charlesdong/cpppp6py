daphne = 100.0
cleo = 100.0

daphne += 100.0 * 0.1
cleo *= 1.05
year = 0
while cleo <= daphne:
  daphne += 100.0 * 0.1
  cleo *= 1.05
  year += 1

print('After %d years, Cleo\'s investment value exceed Daphne\'s.' % year)
