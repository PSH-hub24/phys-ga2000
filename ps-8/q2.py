import matplotlib.pyplot as plt
import numpy as np

# Exercise 7.3

piano = np.loadtxt('piano.txt')
trumpet = np.loadtxt('trumpet.txt')

# part a
plt.plot(piano, label='piano')
plt.legend()
plt.savefig('ps8Figures/q2aPianoWaveForm.png')
plt.close()
plt.plot(trumpet, label='trumpet')
plt.legend()
plt.savefig('ps8Figures/q2aTrumpetWaveForm.png')
plt.close()

pianoFFT = np.fft.rfft(piano)
pianoFFTMag = np.abs(pianoFFT[:10001])
plt.plot(pianoFFTMag, label='Magnitude of first 10000 coeffs')
plt.legend()
plt.title('Piano FFT')
plt.savefig('ps8Figures/q2aPianoFFT.png')
plt.close()

trumpetFFT = np.fft.rfft(trumpet)
trumpetFFTMag = np.abs(trumpetFFT[:10001])
plt.plot(trumpetFFTMag, label='Magnitude of first 10000 coeffs')
plt.legend()
plt.title('Trumpet FFT')
plt.savefig('ps8Figures/q2aTrumpetFFT.png')


# part b
pianoDominantIndex = np.argmax(pianoFFTMag[1:]) + 1
samplingRate = 44100
N = piano.size
pianoFreq = pianoDominantIndex * samplingRate / N
print(f'Fundamental frequency: {pianoFreq}Hz, which corresponds to note C in Octave 5 (523.25Hz)')


