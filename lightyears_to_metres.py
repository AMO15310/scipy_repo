import scipy 
from scipy import constants
x= float(input("Enter the distance in light years: "))
y = constants.light_year
z = x*y
print(f"{x} light years is  {z} meters ")
