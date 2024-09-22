import numpy as np
import timeit
import matplotlib.pyplot as plt

def MatProd(A, B):
	# Square matrix product
	N = (A.shape)[0]
	C = np.zeros((N,N))
	for i in range(N):
		for j in range(N):
			for k in range(N):
				C[i,j] += A[i,k] * B[k,j]
	return C

def TestMatProdTime(N):
	A = np.random.rand(N, N)
	B = np.random.rand(N, N)
	return MatProd(A, B)

def TestDotTime(N):
	A = np.random.rand(N, N)
	B = np.random.rand(N, N)
	return np.dot(A, B)

dataNum = 10
spacing = 10
N = 10
Narray = []
matProdTime = np.zeros(dataNum)
dotTime = np.zeros(dataNum)

for i in range(dataNum):
	Narray.append(N)
	matProdTime[i] = timeit.timeit("TestMatProdTime(N)", "from __main__ import TestMatProdTime, N", number=1)
	dotTime[i] = timeit.timeit("TestDotTime(N)", "from __main__ import TestDotTime, N", number=1)
	N += spacing

Narray = np.array(Narray)
Ncubic = Narray**3
plt.yscale('log')
plt.plot(Narray, matProdTime)
plt.plot(Narray, dotTime)
plt.plot(Narray, Ncubic)
plt.xlabel('N')
plt.ylabel('seconds (log scale)')
plt.legend(['Explicit function', 'dot method', 'N^3'])
plt.savefig('q1(log_scale).png')

