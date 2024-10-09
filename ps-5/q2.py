import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import scipy.special as special

# Exercise 5.17
def Integrand(x, a):
	return x**(a-1) * np.exp(-x)

def IntegrandAlt(x, a):
	return np.exp((a-1)*np.log(x) - x)

def IntegrandCOV(z, a):
	c = a - 1
	return IntegrandAlt(z*c/(1-z), a) * c/((1-z)**2)

def gamma(a):
	(val, none) = integrate.fixed_quad(IntegrandCOV, a=0, b=1, args=(a,), n=100)
	return val


# part a
x = np.linspace(0, 5, 100)
a = [2, 3, 4]
for i in range(3):
	y = Integrand(x, a[i])
	plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['a=2', 'a=3', 'a=4'])
plt.savefig('q2a.png')

# part e
val = gamma(3/2)
print(f'The value for part e is {val}.')

# part f
G3 = gamma(3)
G6 = gamma(6)
G10 = gamma(10)
print(f'gamma(3) = {G3}, 2! = 2.')
print(f'gamma(6) = {G6}, 5! = 120.')
print(f'gamma(10) = {G10}, 9! = 362880.')


