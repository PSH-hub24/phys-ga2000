import matplotlib.pyplot as plt
import numpy as np

# Exercise 8.6

# part a
def f(r, t, omega):
	x = r[0]
	v = r[1]
	fx = v
	fv = -omega**2 * x
	return np.array([fx, fv])

def Sol(omega, tPoints, r):
	xPoints = []
	vPoints = []
	for t in tPoints:
		xPoints.append(r[0])
		vPoints.append(r[1])
		k1 = h * f(r, t, omega)
		k2 = h * f(r+1/2*k1, t+0.5*h, omega)
		k3 = h * f(r+1/2*k2, t+0.5*h, omega)
		k4 = h * f(r+k3, t+h, omega)
		r = r + 1/6 * (k1+2*k2+2*k3+k4)
	return xPoints, vPoints

omega = 1.0
N = 1000
h = 50.0 / N
tPoints = np.arange(0.0, 50.0, h)
r1 = [1.0, 0.0]

xPoints1, vPoints1 = Sol(omega, tPoints, r1)

plt.plot(tPoints, xPoints1)
plt.title('Plot of $x$ as a function of time')
plt.xlabel('time')
plt.ylabel('$x$')
plt.savefig('ps9Figures/q1a.png')
plt.close()

# part b
r2 = [2.0, 0.0]
xPoints2, vPoints2 = Sol(omega, tPoints, r2)
plt.plot(tPoints, xPoints1)
plt.plot(tPoints, xPoints2)
plt.title('Plot of $x$ as a function of time')
plt.legend(['x=1', 'x=2'])
plt.xlabel('time')
plt.ylabel('$x$')
plt.savefig('ps9Figures/q1b.png')
plt.close()

# part c
def fp(r, t, omega):
	x = r[0]
	v = r[1]
	fx = v
	fv = -omega**2 * x**3
	return np.array([fx, fv])

def Solp(omega, tPoints, r):
	xPoints = []
	vPoints = []
	for t in tPoints:
		xPoints.append(r[0])
		vPoints.append(r[1])
		k1 = h * fp(r, t, omega)
		k2 = h * fp(r+1/2*k1, t+0.5*h, omega)
		k3 = h * fp(r+1/2*k2, t+0.5*h, omega)
		k4 = h * fp(r+k3, t+h, omega)
		r = r + 1/6 * (k1+2*k2+2*k3+k4)
	return xPoints, vPoints

xPoints1, vPoints1 = Solp(omega, tPoints, r1)
xPoints2, vPoints2 = Solp(omega, tPoints, r2)

plt.plot(tPoints, xPoints1)
plt.plot(tPoints, xPoints2)
plt.title('Plot of $x$ as a function of time (anharmonic oscillator)')
plt.legend(['x=1', 'x=2'])
plt.xlabel('time')
plt.ylabel('$x$')
plt.savefig('ps9Figures/q1c.png')
plt.close()

# part d
plt.plot(xPoints1, vPoints1)
plt.plot(xPoints2, vPoints2)
plt.title('Plot of $v$ against $x$ (anharmonic oscillator)')
plt.legend(['x=1', 'x=2'])
plt.xlabel('$x$')
plt.ylabel('$v(dx/dt)$')
plt.savefig('ps9Figures/q1d.png')
plt.close()

# part e
def fVan(r, t, omega, mu):
	x = r[0]
	v = r[1]
	fx = v
	fv = mu * (1-x**2) * v - omega**2 * x 
	return np.array([fx, fv])

def SolVan(omega, mu, tPoints, r):
	xPoints = []
	vPoints = []
	for t in tPoints:
		xPoints.append(r[0])
		vPoints.append(r[1])
		k1 = h * fVan(r, t, omega, mu)
		k2 = h * fVan(r+1/2*k1, t+0.5*h, omega, mu)
		k3 = h * fVan(r+1/2*k2, t+0.5*h, omega, mu)
		k4 = h * fVan(r+k3, t+h, omega, mu)
		r = r + 1/6 * (k1+2*k2+2*k3+k4)
	return xPoints, vPoints

omega = 1.0
mu1 = 1.0
mu2 = 2.0
mu3 = 4.0
N = 1000
h = 20.0 / N
tPoints = np.arange(0.0, 20.0, h)
r = [1.0, 0.0]

xPoints1, vPoints1 = SolVan(omega, mu1, tPoints, r)
xPoints2, vPoints2 = SolVan(omega, mu2, tPoints, r)
xPoints3, vPoints3 = SolVan(omega, mu3, tPoints, r)

plt.plot(xPoints1, vPoints1)
plt.plot(xPoints2, vPoints2)
plt.plot(xPoints3, vPoints3)
plt.title('Plot of $v$ against $x$ (van der Pol)')
plt.legend(['$\mu=1$', '$\mu=2$', '$\mu=4$'])
plt.xlabel('$x$')
plt.ylabel('$v$')
plt.savefig('ps9Figures/q1e.png')
plt.close()

