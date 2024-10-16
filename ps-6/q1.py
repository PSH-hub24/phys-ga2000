import numpy as np
import numpy.linalg as linalg
import scipy
import matplotlib.pyplot as plt
from astropy.io import fits
import timeit

# part a
hdu_list = fits.open('specgrid.fits')
logwave = hdu_list['LOGWAVE'].data
flux = hdu_list['FLUX'].data
plt.figure(figsize=(15, 10), dpi=100)
for i in range(4):
	plt.subplot(2, 2, i+1)
	plt.plot(logwave, flux[i])
	plt.xlabel('$\log_{10}(\lambda)$, Angstroms')
	plt.ylabel('flux, $10^{-17}$erg s$^{-1}$ cm$^{-2}$ $\AA^{-1}$')
	plt.title(f'Plot flux[{i}]')
plt.savefig('ps6Figures/q1a.png')

# part b
galNum = flux.shape[0]
fluxN = flux
for i in range(galNum):
	fMin = np.min(flux[i])
	fMax = np.max(flux[i])
	fluxN[i] = (flux[i] - fMin) / (fMax - fMin) 

# part c
wlNum = flux.shape[1]
meanSpectrum = np.zeros(wlNum)
for i in range(wlNum):
	meanSpectrum[i] = np.mean(fluxN[:,i])
residuals = np.zeros_like(flux)
for i in range(galNum):
	residuals[i] = fluxN[i] - meanSpectrum

# part d
def covMatEigen(residuals):
	R = np.column_stack(residuals)
	covMat = np.matmul(R, R.T)
	eigenvalues, eigenvectors = linalg.eig(covMat)
	return eigenvalues, eigenvectors

eigenvalues, eigenvectors = covMatEigen(residuals)
legends = []
for i in range(5):
	plt.plot(eigenvectors[:,i])
	legends.append(f'Eigenvector #{i}')
plt.xlabel('Entry index')
plt.ylabel('y')
plt.legend(legends)
plt.savefig('ps6Figures/q1d.png')	

# part e
def SVDEigen(residuals):
	R = np.column_stack(residuals)
	(u, w, vt) = linalg.svd(R, full_matrices=True)
	return u, w, vt

covMatTime = timeit.timeit("covMatEigen(residuals)", "from __main__ import covMatEigen, residuals", number=1)
SVDTime = timeit.timeit("SVDEigen(residuals)", "from __main__ import SVDEigen, residuals", number=1)
print(f'The covariance matrix method takes {covMatTime}.')
print(f'The SVD matrix method takes {SVDTime}.')

# part f
R = np.column_stack(residuals)
covMat = np.matmul(R, R.T)
REigvals = scipy.linalg.svdvals(R)
covMatEigvals = np.linalg.eigvals(covMat)
RCond = np.max(REigvals) / np.min(REigvals)
covMatCond = np.max(covMatEigvals) / np.min(covMatEigvals)
print(f'The condition number of C is {covMatCond}.')
print(f'The condition number of R is {RCond}.')

# part g
coeffs = np.zeros((galNum, 20))
for i in range(galNum):
	tempResiduals = np.matmul(eigenvectors.T, residuals[i])
	coeffs[i] = tempResiduals[:20]

# part h
c0 = coeffs[:,0]
c1 = coeffs[:,1]
c2 = coeffs[:,2]
plt.plot(c0)
plt.plot(c1)
plt.plot(c2)
plt.legend(['c0', 'c1', 'c2'])
plt.xlabel('Entry index')
plt.ylabel('y')
plt.savefig('ps6Figures/q1h.png')
plt.close()

# part i
def SqrRes(N):
	resSumSqr = 0
	for i in range(galNum):
		newSpec = 0
		for j in range(N):
			newSpec += coeffs[i][j] * eigenvectors[:,j]
		res = newSpec - residuals[i]
		resSumSqr += np.sum(res**2)
	return resSumSqr
N = np.arange(20)
sqrRes = np.zeros_like(N)
for i in range(20):
	sqrRes[i] = SqrRes(N[i])
plt.plot(N, sqrRes)
plt.xlabel('$N_c$')
plt.ylabel('squared residuals')
plt.title('The first galaxy as an example')
plt.savefig('ps6Figures/q1i.png')