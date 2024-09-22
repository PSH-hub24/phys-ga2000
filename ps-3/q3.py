import numpy as np
import matplotlib.pyplot as plt

def CountDecay(decayTimeArr, t):
	# Assume sorted array
	cnt = 0
	for i in range(decayTimeArr.size):
		if decayTimeArr[i] <= t:
			cnt += 1
		else:
			break
	return cnt


randNums = np.random.rand(1000)
mu = np.log(2)/(3.053*60)
randNums = -1/mu * np.log(1-randNums)
randNums = np.sort(randNums)
timeArr = np.arange(1000)
decayCountArr = np.zeros(1000)
for i in range(1000):
	decayCountArr[i] = CountDecay(randNums, timeArr[i])
plt.plot(timeArr, 1000-decayCountArr)
plt.xlabel('Time (seconds)')
plt.ylabel('Number of atoms not decayed')
plt.savefig('q3.png')