feets, inches = map(int, input('Enter your height in feets and inches: ').strip().split(' '))
pounds = float(input('Enter your weight in pounds: '))
IPF = 12        # inches per feet
MPI = 0.0254    # meters per inch
PPKG = 2.2      # pounds per kilogram
weight = pounds / PPKG
height = (feets * IPF + inches) * MPI
print('BMI:', weight / (height * height))
