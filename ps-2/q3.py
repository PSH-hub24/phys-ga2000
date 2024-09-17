import numpy as np
import timeit

# For-loop version
def MForloop(L):
	M = 0
	for i in range(-L,L+1):
		for j in range(-L,L+1):
			for k in range(-L,L+1):
				if i == 0 and j == 0 and k == 0:
					continue
				squareSum = i**2 + j**2 + k**2
				parity = 1 - 2*((i+j+k)%2==0)
				M = M + parity*(1/np.sqrt(squareSum))
	print(f'The for-loop version calculates M = {M}')

# No for-loop version
def MNoForloop(L):
	arrDim = 2*L + 1
	initMat = np.indices((arrDim,arrDim,arrDim)) - L
	mat = np.sum(initMat**2, axis=0)
	mat = 1/np.sqrt(mat)
	mat[L,L,L] = 0
	mat = np.where((initMat[0]+initMat[1]+initMat[2])%2==0, -mat, mat)
	M = np.sum(mat)
	print(f'The no-for-loop version calculates M = {M}')

L = 100
print(timeit.timeit("MForloop(L)", "from __main__ import MForloop, L", number=1))
print(timeit.timeit("MNoForloop(L)", "from __main__ import MNoForloop, L", number=1))


