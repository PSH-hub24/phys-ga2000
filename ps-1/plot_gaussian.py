import numpy as np
import matplotlib.pyplot as plt

mean = 0
std = 3

def Gaussian(mean, std, x):
	return 1./(std*np.sqrt(2.*np.pi)) * np.exp(-np.power((x-mean)/std,2)/2.)

xArray = np.linspace(-10, 10, 1000)
yArray = Gaussian(mean, std, xArray)
plt.plot(xArray, yArray)
plt.savefig('gaussian.png')
