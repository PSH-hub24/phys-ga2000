import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats



# N = np.array([1, 10, 100, 1000, 2500, 5000, 7500, 10000])
N = np.arange(0,101,10)
N[0] = 1
meanArr = np.zeros(N.size)
varArr = np.zeros(N.size)
skewArr = np.zeros(N.size)
kurArr = np.zeros(N.size)

yTrials = 10000
yArr = np.zeros(yTrials)
legends = []
for i in range(N.size):
    for j in range(yTrials):	
        x = np.random.exponential(scale=1.0, size=N[i])
        yArr[j] = np.sum(x)/N[i]
    meanArr[i] = np.mean(yArr)
    varArr[i] = np.var(yArr)
    skewArr[i] = stats.skew(yArr)
    kurArr[i] = stats.kurtosis(yArr)
    plt.hist(yArr, bins=50, density=True, alpha=0.5)
    legends.append(f'N = {N[i]}')
plt.legend(legends)
plt.savefig('q4LargeN.png')
plt.close()

plt.plot(N, meanArr)
plt.plot(N, varArr)
plt.plot(N, skewArr)
plt.plot(N, kurArr)
plt.xlabel('N')
plt.ylabel('Moments')
plt.legend(['Mean', 'Variance', 'Skewness', 'Kurtosis'])
plt.savefig('q4Moments.png')

skewBoundary = 0.01 * skewArr[0]
kurBoundary = 0.01 * kurArr[0]
for i in range(1, N.size):
    if skewArr[i] > skewBoundary:
        print(f'The skewness has reached about 1% of its value for N = 1 at N = {N[i]}')
        break
for i in range(1, N.size):
    if kurArr[i] > kurBoundary:
        print(f'The kurtosis has reached about 1% of its value for N = 1 at N = {N[i]}')
        break





