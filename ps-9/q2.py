import matplotlib.pyplot as plt
import numpy as np
import scipy

# Exercise 8.7

# part a: see pdf

# part b:
def f(r, A):
	x = r[0]
	y = r[1]
	vx = r[2]
	vy = r[3]
	fx = vx
	fy = vy
	fvx = -np.pi/2 * A * vx * np.sqrt(vx**2 + vy**2)
	fvy = -1 - np.pi/2 * A * vy * np.sqrt(vx**2 + vy**2)
	return np.array([fx, fy, fvx, fvy])

def Sol(A, tPoints, r):
	xPoints = []
	yPoints = []
	vxPoints = []
	vyPoints = []
	for t in tPoints:
		xPoints.append(r[0])
		yPoints.append(r[1])
		vxPoints.append(r[2])
		vyPoints.append(r[3])
		k1 = h * f(r, A)
		k2 = h * f(r+1/2*k1, A)
		k3 = h * f(r+1/2*k2, A)
		k4 = h * f(r+k3, A)
		r = r + 1/6 * (k1+2*k2+2*k3+k4)
	return np.array(xPoints), np.array(yPoints), np.array(vxPoints), np.array(vyPoints)

m = 1
R = 0.08
angle = np.pi/6
v0 = 100
rho = 1.22
C = 0.47
g = 9.81
Tsquare = R / g
A = R**2 * rho * C * g * Tsquare / m
r0 = [0, 0, v0*np.cos(angle), v0*np.sin(angle)]

N = 1000
timeSpan = 100.0
h = timeSpan / N
tPoints = np.arange(0.0, timeSpan, h)

xPoints, yPoints, vxPoints, vyPoints = Sol(A, tPoints, r0)
yTemp = np.abs(yPoints[1:])
gndIdx = np.argmin(yTemp)
yPoints = yPoints[:gndIdx+2] * R
xPoints = xPoints[:gndIdx+2] * R

plt.plot(xPoints, yPoints)
plt.title('Trajectory of the cannonball')
plt.xlabel('$x$ (meters)')
plt.ylabel('$y$ (meters)')
plt.savefig('ps9Figures/q2b.png')
plt.close()

# part c
m1 = 5
m2 = 10
m3 = 15
A1 = R**2 * rho * C * g * Tsquare / m1
A2 = R**2 * rho * C * g * Tsquare / m2
A3 = R**2 * rho * C * g * Tsquare / m3

xPoints1, yPoints1, vxPoints1, vyPoints1 = Sol(A1, tPoints, r0)
xPoints2, yPoints2, vxPoints2, vyPoints2 = Sol(A2, tPoints, r0)
xPoints3, yPoints3, vxPoints3, vyPoints3 = Sol(A3, tPoints, r0)

yTemp = np.abs(yPoints1[1:])
gndIdx = np.argmin(yTemp)
yPoints1 = yPoints1[:gndIdx+2] * R
xPoints1 = xPoints1[:gndIdx+2] * R

yTemp = np.abs(yPoints2[1:])
gndIdx = np.argmin(yTemp)
yPoints2 = yPoints2[:gndIdx+2] * R
xPoints2 = xPoints2[:gndIdx+2] * R

yTemp = np.abs(yPoints3[1:])
gndIdx = np.argmin(yTemp)
yPoints3 = yPoints3[:gndIdx+2] * R
xPoints3 = xPoints3[:gndIdx+2] * R

plt.plot(xPoints, yPoints)
plt.plot(xPoints1, yPoints1)
plt.plot(xPoints2, yPoints2)
plt.plot(xPoints3, yPoints3)
plt.title('Trajectory of the cannonball')
plt.xlabel('$x$ (meters)')
plt.ylabel('$y$ (meters)')
plt.legend(['m=1kg', 'm=5kg', 'm=10kg', 'm=15kg'])
plt.savefig('ps9Figures/q2c.png')
plt.close()