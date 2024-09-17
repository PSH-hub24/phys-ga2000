import numpy as np

def get_fbits(value):
	# Convert np.float32 value to its binary representation
	binRep = np.asarray(value, dtype=np.float32).view(np.int32)
	return binRep

def get_fvalue(binRep):
	# Convert binary representation to its np.float32 value
	value = np.asarray(binRep, dtype=np.int32).view(np.float32).item()
	return value

num = 100.98763
np32Num = np.float32(num)
np32BinRep = get_fbits(np32Num)
np32Value = get_fvalue(np32BinRep)
print('The binary representation of 100.98763 in np.float32:')
print('{:032b}'.format(np32BinRep))
print('The 32-bit number is:')
print(np32Value)
print('The difference between the actual number from its binary representation:')
print(np32Value-num)


