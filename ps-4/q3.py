import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import scipy.special as special

# Exercise 5.13

# part a
def H(n, x):
	if n == 0:
		return (1., 0)
	if n == 1:
		return (2.*x, 1.)
	firstH, secondH = H(n-1, x)
	return ((2.*x * firstH - 2.*(n-1) * secondH), firstH)

def waveFunc(n, x):
	factor = 1 / np.sqrt(2.**n * np.math.factorial(n) * np.sqrt(np.pi)) * np.exp(-x**2/2)
	Hn, dummy = H(n, x)
	return factor * Hn

xArray = np.linspace(-4, 4, 100)
nArray = [0, 1, 2, 3]
legends = []
for i in range(len(nArray)):
	yArray = np.zeros(xArray.size)
	for j in range(xArray.size):
		yArray[j] = waveFunc(nArray[i], xArray[j])
	plt.plot(xArray, yArray)
	legends.append(f'n = {nArray[i]}')
plt.xlabel('x')
plt.ylabel('wavefunction')
plt.legend(legends)
plt.savefig('q3a.png')
plt.close()

# part b
xArray = np.linspace(-10, 10, 1000)
yArray = np.zeros(xArray.size)
for i in range(xArray.size):
	yArray[i] = waveFunc(30, xArray[i])
plt.plot(xArray, yArray)
plt.xlabel('x')
plt.ylabel('wavefunction')
plt.legend(['n = 30'])
plt.savefig('q3b.png')

# part c
def Integrand(z, n):
	# Rescale (-inf, inf) to [-pi/2, pi/2]
	return (np.tan(z))**2 * np.abs(waveFunc(n, np.tan(z)))**2 / np.cos(z)**2

def rms(n):
	(val, none) = integrate.fixed_quad(Integrand, a=-np.pi/2, b=np.pi/2, args=(n,), n=100)
	return np.sqrt(val)

rmsVal = rms(5)
print(f'part c: The rms of the particle for n = 5 is {rmsVal}.')

# part d
def waveFuncHermite(x):
	n = 5
	# Account for the weight exp(-x^2)
	factor = 1 / np.sqrt(2**n * np.math.factorial(n) * np.sqrt(np.pi))
	Hn, dummy = H(n, x)
	return factor * Hn

def rmsIntegrand(x):
	# n = 5
	return x**2 * waveFuncHermite(x)**2

N = 100
x, w = special.roots_hermite(N)
val = np.sum(w * rmsIntegrand(x))
print(f'part d answer: {np.sqrt(val)}')

		

