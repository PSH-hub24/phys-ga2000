import numpy as np
import matplotlib.pyplot as plt

def Solution(a, b, c):
	sol1 = 1/(2*a) * (-b+np.sqrt(b**2-4*a*c))
	sol2 = 1/(2*a) * (-b-np.sqrt(b**2-4*a*c))
	return sol1, sol2

def NewSolution(a, b, c):
	sol1 = 2*c / (-b-np.sqrt(b**2-4*a*c))
	sol2 = 2*c / (-b+np.sqrt(b**2-4*a*c))
	return sol1, sol2
	
a = 0.001
b = 1000
c = 0.001
print('The solutions for part a:')
print(Solution(a, b, c))
print('The solutions for part b:')
print(NewSolution(a, b, c))
