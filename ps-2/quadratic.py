import numpy as np

class quadratic:
	@staticmethod
	def quadratic(a, b, c):
		a = np.float64(a)
		b = np.float64(b)
		c = np.float64(c)
		sol1 = 1/(2*a) * (-b+np.sqrt(b**2-4*a*c))
		sol2 = 1/(2*a) * (-b-np.sqrt(b**2-4*a*c))
		return sol1, sol2 