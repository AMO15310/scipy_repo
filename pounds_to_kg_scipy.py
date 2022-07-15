import scipy
from scipy import constants


x =float(input("Enter weight in pounds: "))

y = constants.pound

z = float(x*y)

print(f"{x} in kilograms is {z} kgs")

