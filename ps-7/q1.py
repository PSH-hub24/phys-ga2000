import numpy as np
import scipy
import jax
import jax.numpy as jnp


G = 6.674 * 1e-11

# part a

def f(rp, mp):
	# rp = r/R, mp = m/M
	return G/(rp**2) - G*mp/((1-rp)**2) - G*rp

def SingleNewton(x, mp, dvJax):
	fp = dvJax(x, mp)
	xp = x - f(x, mp)/fp
	return xp

def bracketing(a, mp, stepSize, iterNum):
	b = a + stepSize
	for i in range(iterNum):
		if f(a, mp) * f(b, mp) < 0:
			b = min(b, 1.0)
			return a, b
		a = b
		b = b + stepSize
	return 0.0, 1.0

dvJax = jax.grad(f)
stepSize = 0.1
iterNum = 10
a0 = 0.001

# Earth and Moon
M = 5.974 * 1e24
m = 7.348 * 1e22
mp = m / M
a, b = bracketing(a0, mp, stepSize, iterNum)
x0 = (a+b) / 2
print(f'initial guess: {x0}')
xp = x0
iterNum = 10
for i in range(iterNum):
	xp = SingleNewton(xp, mp, dvJax)
print(f'r/R value of L1 between the Earth and the Moon: {xp}')

# Earth and Sun
M = 1.989 * 1e30
m = 5.974 * 1e24
mp = m / M
a, b = bracketing(a0, mp, stepSize, iterNum)
x0 = (a+b) / 2
print(f'initial guess: {x0}')
xp = x0
iterNum = 10
for i in range(iterNum):
	xp = SingleNewton(xp, mp, dvJax)
print(f'r/R value of L1 between the Sun and the Earth: {xp}')

# Jupiter-mass planet orbiting the Sun at the distance of the Earth
M = 1.989 * 1e30
m = 1.898 * 1e27
mp = m / M
a, b = bracketing(a0, mp, stepSize, iterNum)
x0 = (a+b) / 2
print(f'initial guess: {x0}')
xp = x0
iterNum = 10
for i in range(iterNum):
	xp = SingleNewton(xp, mp, dvJax)
print(f'r/R value of L1 between the Sun and the Jupiter-mass planet (at the Earth distance): {xp}')