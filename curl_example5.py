import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection="3d")

x = np.linspace(-5, 5, 10)
y = np.linspace(-5, 5, 10)
z = np.linspace(-5, 5, 10)

X, Y, Z = np.meshgrid(x, y, z)

P = np.sin(Y) + np.cos(Z)
Q = np.sin(Z) + np.cos(X)
R = np.sin(X) + np.cos(Y)
mag = np.sqrt(P**2 + Q**2 + R**2)
P = P/mag
Q = Q/mag
R = R/mag
mag = (mag - np.ones(mag.shape)*mag.min())/(mag.max()-mag.min())
c = plt.cm.hsv(mag)

ax.quiver(X, Y, Z, P, Q, R, lw=0.5)
plt.savefig("curl_example5.png")
plt.show()