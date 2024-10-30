import numpy as np
import scipy

omega = (3-np.sqrt(5)) / 2

def y(x):
	return (x-0.3)**2 * np.exp(x)

def ParabolicStep(a, b, c):
	R = y(b) / y(c)
	S = y(b) / y(a)
	T = y(a) / y(c)
	P = S * (T*(R-T)*(c-b) - (1-R)*(b-a))
	Q = (T-1) * (R-1) * (S-1)
	return b + P/Q

def Brent(a, b, c, tol, maxIter):
	previousStep = c - a
	previousVal = y(b)
	for i in range(maxIter):
		x = ParabolicStep(a, b, c)
		if x > c or x < a or (x-a) > previousStep:
			x = c - omega*(c-a)
		fx = y(x)
		if np.abs(fx - previousVal) <= tol*np.abs(fx):
			return x
		fb = y(b)
		previousStep = x - a
		previousVal = fx
		if fx < fb:
			if x < b:
				c = b
			else:
				a = b
			b = x
		else:
			if x < b:
				a = x
			else:
				c = x
	return x


a = 0
c = 0.5
b = omega*(c-a) + a
tol = 1e-15
maxIter = 50
xMin = Brent(a, b, c, tol, maxIter)
print(f'My Brent function gives x_min = {xMin}.')

xScipyMin = scipy.optimize.brent(y)
print(f'Scipy\'s Brent function gives x_min = {xScipyMin}.')

xMinDiff = np.abs(xMin-0.3)
xScipyMinDiff = np.abs(xScipyMin-0.3)
print(f'Boolean value of whether my x_min is closer to 0.3 compared to scipy\'s x_min: {xMinDiff<xScipyMin}')




