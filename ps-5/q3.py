import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as linalg

# part a
signal = np.genfromtxt('signal.dat')
timeArr = []
signalArr = []
for i in range(1, signal.shape[0]):
		timeArr.append(signal[i][1])
		signalArr.append(signal[i][3])
plt.plot(timeArr, signalArr, 'o', markersize=0.5)		
plt.xlabel('time')
plt.ylabel('signal')
plt.savefig('q3a.png')
plt.close() 

# part b
# Rescale the time variable.
timeArr = np.array(timeArr)
timeArr = (timeArr - timeArr.mean()) / timeArr.std()
signalArr = np.array(signalArr)
A = np.zeros((timeArr.size, 4))
A[:, 0] = 1.
A[:, 1] = timeArr	 
A[:, 2] = timeArr**2
A[:, 3] = timeArr**3
(u, w, vt) = np.linalg.svd(A, full_matrices=False)
Ainv = vt.transpose().dot(np.diag(1. / w)).dot(u.transpose())
x = Ainv.dot(signalArr)
signalArrFit = A.dot(x)

plt.plot(timeArr, signalArr, '.', label='signal data', markersize=0.5)
plt.plot(timeArr, signalArrFit, '.', label='model', markersize=0.7)
plt.xlabel('time')
plt.ylabel('signal')
plt.legend()
plt.savefig('q3b.png')
plt.close()

# part c
r = signalArrFit - signalArr
plt.plot(timeArr, r, '.', markersize=0.5)
plt.xlabel('time')
plt.ylabel('residual')
plt.title('residual of data wrt model')
plt.savefig('q3c.png')
plt.close()
RMSE = np.sqrt(np.sum(r**2)/r.size)
print(f'Part c: the RMSE value is {RMSE}.')

# part d
order = 30
A = np.zeros((timeArr.size, order))
A[:, 0] = 1.
for i in range(1, order):
	A[:, i] = timeArr**i
(u, w, vt) = np.linalg.svd(A, full_matrices=False)

condNum = np.max(w) / np.min(w)
print(f'Part d: Conditional number of A is {condNum}.')

Ainv = vt.transpose().dot(np.diag(1. / w)).dot(u.transpose())
x = Ainv.dot(signalArr)
signalArrFit = A.dot(x)

plt.plot(timeArr, signalArr, '.', label='signal data', markersize=0.5)
plt.plot(timeArr, signalArrFit, '.', label=f'model, order = {order}', markersize=0.7)
plt.xlabel('time')
plt.ylabel('signal')
plt.legend()
plt.savefig('q3dFit.png')
plt.close()

r = signalArrFit - signalArr
plt.plot(timeArr, r, '.', markersize=0.5)
plt.xlabel('time')
plt.ylabel('residual')
plt.savefig('q3dResidual.png')
plt.close()
RMSE = np.sqrt(np.sum(r**2)/r.size)
print(f'Part d: the RMSE value is {RMSE}.')

# part e
freq = 0.2
Nsize = 11
N = np.arange(Nsize)
A = np.zeros((timeArr.size, 2*Nsize))
for i in range(Nsize):
	A[:, i] = np.cos(2*np.pi*freq*N[i]*timeArr)
for i in range(Nsize, 2*Nsize):
	A[:, i] = np.sin(2*np.pi*freq*N[i-Nsize]*timeArr)

(u, w, vt) = np.linalg.svd(A, full_matrices=False)
Ainv = vt.transpose().dot(np.diag(1. / w)).dot(u.transpose())
x = Ainv.dot(signalArr)
signalArrFit = A.dot(x)
plt.plot(timeArr, signalArr, '.', label='signal data', markersize=0.5)
plt.plot(timeArr, signalArrFit, '.', label='Lomb-Scargle', markersize=0.7)
plt.xlabel('time')
plt.ylabel('signal')
plt.legend()
plt.savefig('q3eFit.png')
plt.close()

r = signalArrFit - signalArr
plt.plot(timeArr, r, '.', markersize=0.5)
plt.xlabel('time')
plt.ylabel('residual')
plt.savefig('q3eResidual.png')
plt.close()
RMSE = np.sqrt(np.sum(r**2)/r.size)
print(f'Part e: the RMSE value is {RMSE}.')





