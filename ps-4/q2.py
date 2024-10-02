import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

# Exercise 5.10
def V(x):
	return x**4

def Integrand(x, a):
	return 1 / np.sqrt(V(a)-V(x))

def T(a):
	(val, none) = integrate.fixed_quad(Integrand, a=0, b=a, args=(a,), n=20)
	# m = 1
	return np.sqrt(8) * val

aArray = np.linspace(0, 2, 100)
TArray = np.zeros(aArray.size)
for i in range(TArray.size):
	TArray[i] = T(aArray[i])

plt.plot(aArray, TArray)
plt.xlabel('Amplitude')
plt.ylabel('Period')
plt.title('N = 20 sample points')
plt.savefig('q2b.png')

