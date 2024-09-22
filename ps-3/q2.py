import numpy as np
import matplotlib.pyplot as plt

Bi213Num = 10000 
PbNum = 0
TlNum = 0
Bi209Num = 0
Bi213Arr = [Bi213Num]
PbArr = [PbNum]
TlArr = [TlNum]
Bi209Arr = [Bi209Num]
timeLen = 20000
timeArr = np.arange(timeLen)

# Decay prob over 1 sec: P = 1 - 2**(-t/half-life)
BiDecayProb = 1 - 2**(-1/(46*60))
PbDecayProb = 1 - 2**(-1/(3.3*60))
TlDecayProb = 1 - 2**(-1/(2.2*60))

for t in range(1,timeLen):
	for i in range(PbNum):
		randNum = np.random.rand()
		if randNum < PbDecayProb:
			PbNum -= 1
			Bi209Num += 1
	for i in range(TlNum):
		randNum = np.random.rand()
		if randNum < TlDecayProb:
			TlNum -= 1
			PbNum += 1
	for i in range(Bi213Num):
		randNum1 = np.random.rand()
		randNum2 = np.random.rand()
		if randNum1 < BiDecayProb:
			Bi213Num -= 1
			if randNum2 < 0.9791:
				PbNum += 1
			else:
				TlNum += 1

	Bi213Arr.append(Bi213Num)
	PbArr.append(PbNum)
	TlArr.append(TlNum)
	Bi209Arr.append(Bi209Num)

plt.plot(timeArr, Bi213Arr)
plt.plot(timeArr, PbArr)
plt.plot(timeArr, TlArr)
plt.plot(timeArr, Bi209Arr)
plt.xlabel('seconds')
plt.ylabel('Number of atoms')
plt.legend(['Bi213', 'Pb', 'Tl', 'Bi209'])
plt.savefig('q2.png')


