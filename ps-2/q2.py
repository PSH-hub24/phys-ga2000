import numpy as np

increment32 = np.float32(np.exp2(-23))
increment64 = np.float32(np.exp2(-52))
oneIncrement32 = np.float32(1 + increment32)
oneIncrement64 = np.float64(1 + increment64)
print('Smallest increment to 1 in np.float32 is approx. 2^(-23), and the result is:')
print(oneIncrement32)
print('Smallest increment to 1 in np.float64 is approx. 2^(-52), and the result is:')
print(oneIncrement64)

minNum32 = np.float32(-np.exp2(127))
maxNum32 = np.float32(np.exp2(127))
minNum64 = np.float64(-np.exp2(1023))
maxNum64 = np.float64(np.exp2(1023))
print('Minimum of np.float32 is approx. -2^(127), which reads:')
print(minNum32)
print('Maximum of np.float32 is approx. 2^(127), which reads::')
print(maxNum32)
print('Minimum of np.float64 is approx. -2^(1023), which reads::')
print(minNum64)
print('Maximum of np.float64 is approx. 2^(1023), which reads::')
print(maxNum64)

