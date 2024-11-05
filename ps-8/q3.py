import matplotlib.pyplot as plt
import numpy as np

# Exercise 7.4

# part a
dow = np.loadtxt('dow.txt')
plt.plot(dow, label='dow data')
plt.xlabel('Business day since late 2006')
plt.ylabel('Daily closing value')
plt.legend()
plt.savefig('ps8Figures/q3a.png')

# part b
dowFFT = np.fft.rfft(dow)

# part c
N = dowFFT.size
dowFFT[int(N/10):] = 0

# part d
dowNew = np.fft.irfft(dowFFT)
plt.plot(dowNew, label='New dow data (first 10%)')
plt.legend()
plt.savefig('ps8Figures/q3d.png')

# part e
dowFFT[int(N/50):] = 0
dowNew = np.fft.irfft(dowFFT)
plt.plot(dowNew, label='New dow data (first 2%)')
plt.legend()
plt.savefig('ps8Figures/q3e.png')
