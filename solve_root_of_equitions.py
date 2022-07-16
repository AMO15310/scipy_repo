import scipy
from scipy.optimize import root
from math import sin

def eqn(x):
    return x + sin(x**2)
myroot = root(eqn,5)
print(f"The answer is {myroot.x}")
