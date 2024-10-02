import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

# Exercise 5.9
V = 0.001  		# 1000 cm^3 -> 0.001 m^3
rho = 6.022e28
thetaD = 428
kB = 1.381e-23

def Integrand(x):
	return (x**4 * np.exp(x)) / ((np.exp(x)-1)**2)

def cv(T, N):
	coeff = 9.* V * rho * kB * (T/thetaD)**3
	(val, none) = integrate.fixed_quad(Integrand, 0, thetaD/T, n=N)
	return val * coeff

TArray = np.linspace(5, 500, 1000)
cvArray = np.zeros(TArray.size)
for i in range(TArray.size):
	cvArray[i] = cv(TArray[i], 50)

plt.plot(TArray, cvArray)
plt.xlabel('Temperature (K)')
plt.ylabel('Heat capacity')
plt.title('N = 50 sample points')
plt.savefig('q1(N=50).png')

plt.close()
plt.xlabel('Temperature (K)')
plt.ylabel('Heat capacity')
legends = []
NArray = np.linspace(10, 70, 7)
for i in range(NArray.size):
	cvArray = np.zeros(TArray.size)
	for j in range(TArray.size):
		cvArray[j] = cv(TArray[j], NArray[i])
	plt.plot(TArray, cvArray, linewidth=0.5)
	legends.append(f'N = {NArray[i]}')
plt.title('Array of N')
plt.legend(legends)
plt.savefig('q1(part c).png')

