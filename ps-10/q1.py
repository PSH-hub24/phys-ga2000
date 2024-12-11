import matplotlib.pyplot as plt
import numpy as np
from banded import banded

# Exercise 9.8

def psi0(x, x0, sigma, k):
	return np.exp(-(x-x0)**2/(2*sigma**2)) * np.exp(1j*k*x)

hbar = 1.055e-36
M = 9.109e-31
L = 1e-8
N = 1000
a = L / N
timeStep = 1e-18

term = hbar*1j / (2*M*a**2)
a1 = 1 + timeStep*term
a2 = -timeStep*term / 2
b1 =  1 - timeStep*term
b2 =  timeStep*term / 2

A = np.empty([3,N], complex)
A[0,:] = a2
A[1,:] = a1
A[2:,] = a2

x0 = L / 2
sig = 1e-10
k = 5e10
xPoints = np.linspace(0,L,N+1)
psiVec = np.zeros(N+1,complex)
for i in range(N+1):
	psiVec[i] = psi0(xPoints[i], x0, sig, k)
psiVec[0] = 0
psiVec[N] = 0

psiVec0 = np.real(psiVec) * 1e-9

v = np.zeros(N-1, complex)
for step in range(1000):
	v = b1*psiVec[1:N] + b2*(psiVec[2:N+1]+psiVec[0:N-1])
	psiVec[1:N] = banded(A,v,1,1)

psiVec1 = np.real(psiVec) * 1e-9

for step in range(5000):
	v = b1*psiVec[1:N] + b2*(psiVec[2:N+1]+psiVec[0:N-1])
	psiVec[1:N] = banded(A,v,1,1)

psiVec2 = np.real(psiVec) * 1e-9

plt.plot(xPoints, psiVec0)
plt.plot(xPoints, psiVec1)
plt.plot(xPoints, psiVec2)
plt.xlabel('meters')
plt.ylabel('1e-9 * real part of $\psi$')
plt.legend(['step # = 0','step # = 1000', 'step # = 5000'])
plt.show()
