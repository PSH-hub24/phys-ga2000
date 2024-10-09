import numpy as np
import matplotlib.pyplot as plt
import jax
import jax.numpy as jnp
jax.config.update('jax_enable_x64', True)

# Exercise 5.15
def f(x):
	return 1 + 1/2*np.tanh(2*x)

def dfCentral(f, x, dx):
	return((f(x + 0.5 * dx) - f(x - 0.5 * dx)) / dx)

def dfAnalytic(x):
	return 1 / np.cosh(2*x)**2

def f0Jax(x):
	return 2*x

def f1Jax(y):
	return 1 + 1/2*jnp.tanh(y)

def fJax(x):
	return f1Jax(f0Jax(x))

x = np.linspace(-2, 2, 100)
yCentral = dfCentral(f, x, 0.5 * 1.e-5)
yAnalytic = dfAnalytic(x)
plt.xlabel('x')
plt.ylabel('Derivative of f(x)')
plt.plot(x, yAnalytic)
plt.plot(x, yCentral, 'o', markersize=2.5)
plt.legend(['Analytic', 'Numerical'])
plt.savefig('q1CentralDiff.png')
plt.close()

dvJax = jax.grad(fJax)
yJax = jax.vmap(dvJax)(x)
plt.xlabel('x')
plt.ylabel('Derivative of f(x)')
plt.plot(x, yAnalytic)
plt.plot(x, yJax, 'o', markersize=2.5)
plt.legend(['Analytic', 'Jax'])
plt.savefig('q1Jax.png')



