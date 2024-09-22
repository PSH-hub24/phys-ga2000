import numpy as np
import matplotlib.pyplot as plt

def CheckLength(z):
	return (np.absolute(z) <= 2)

def UpdateFunc(c, z):
	return z**2 + c

def GetMandelbrot(cMat):
	iterations = 100
	zMat = np.zeros(cMat.shape)
	for i in range(iterations):
		zMat = zMat**2 + cMat
	return zMat

N = 2000
spacing = 4/(N-1)
initMat = np.indices((N,N))
cMat = initMat[0]*spacing +  initMat[1]*spacing*1j
cMat = cMat - (2+2j)
zMat = GetMandelbrot(cMat)



pointsBlack = cMat[(CheckLength(zMat)).nonzero()]
pointsWhite = cMat[(~CheckLength(zMat)).nonzero()]
blackSize = np.size(pointsBlack)
whiteSize = np.size(pointsWhite)
xArrayBlack = np.zeros(blackSize)
yArrayBlack = np.zeros(blackSize)
xArrayWhite = np.zeros(whiteSize)
yArrayWhite = np.zeros(whiteSize)

for i in range(blackSize):
	xArrayBlack[i] = np.real(pointsBlack[i])
	yArrayBlack[i] = np.imag(pointsBlack[i])
for i in range(whiteSize):
	xArrayWhite[i] = np.real(pointsWhite[i])
	yArrayWhite[i] = np.imag(pointsWhite[i])

plt.scatter(xArrayBlack, yArrayBlack, color='black')
plt.scatter(xArrayWhite, yArrayWhite, color='White')
plt.show()