import matplotlib.pyplot as plt
import numpy as np
from dcst import dst, idst

# Exercise 9.9

# part a
def psi0(x, x0, sigma, k):
	return np.exp(-(x-x0)**2/(2*sigma**2)) * np.exp(1j*k*x)

hbar = 1.055e-36
M = 9.109e-31
L = 1e-8
N = 1000
a = L / N
timeStep = 1e-18

x0 = L / 2
sig = 1e-10
k = 5e10
xPoints = np.linspace(0,L,N+1)
psiVec = np.zeros(N+1,complex)
for i in range(N+1):
	psiVec[i] = psi0(xPoints[i], x0, sig, k)
psiVec[0] = 0
psiVec[N] = 0

realBFull = dst(np.real(psiVec))
imgBFull = dst(np.imag(psiVec))

realB = realBFull[1:N]
imgB = imgBFull[1:N]
bk = realBFull + 1j*imgBFull

# part b
realPsi = np.zeros(N+1)
t = 1e-16
for i in range(1,N):
	term = np.pi**2*hbar*i**2/(2*M*L**2)*t
	realPsi = realPsi + (realB[i-1]*np.cos(term) - imgB[i-1]*np.sin(term))*np.sin(np.pi*i*np.arange(0,N+1)/N)
realPsi = realPsi / N

temp = np.zeros(N+1, complex)
bCoeff = bk * np.exp(1j*np.pi**2*hbar*np.arange(0,N+1)**2/(2*M*L**2)*t)
realPsiIDST = idst(np.real(bCoeff))

plt.plot(xPoints, realPsi)
plt.plot(xPoints, realPsiIDST)
plt.xlabel('meters')
plt.ylabel('real part of $\psi$')
plt.legend(['formula','idst'])
plt.savefig('ps10Figures/q2b.png')
plt.close()


# part c, d
plt.plot(xPoints, realPsi)
realPsi = np.zeros(N+1)
t = 1e-15
for i in range(1,N):
	term = np.pi**2*hbar*i**2/(2*M*L**2)*t
	realPsi = realPsi + (realB[i-1]*np.cos(term) - imgB[i-1]*np.sin(term))*np.sin(np.pi*i*np.arange(0,N+1)/N)
realPsi0 = realPsi / N

realPsi = np.zeros(N+1)
t = 1e-14
for i in range(1,N):
	term = np.pi**2*hbar*i**2/(2*M*L**2)*t
	realPsi = realPsi + (realB[i-1]*np.cos(term) - imgB[i-1]*np.sin(term))*np.sin(np.pi*i*np.arange(0,N+1)/N)
realPsi1 = realPsi / N

plt.plot(xPoints, realPsi0)
plt.plot(xPoints, realPsi1)
plt.xlabel('meters')
plt.ylabel('real part of $\psi$')
plt.legend(['t=1e-16','t=1e-15','t=1e-14'])
plt.savefig('ps10Figures/q2d.png')