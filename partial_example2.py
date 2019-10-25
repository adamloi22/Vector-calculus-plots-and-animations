import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

x = np.arange(-10, 10, 40, endpoint=True)
y = np.arange(-10, 10, 40, endpoint=True)

X, Y = np.meshgrid(x, y)

F = X**2*np.sin(Y)
U = 2*X*np.sin(Y)
V = X**2*np.cos(Y)
M = np.sqrt(U**2 + V**2)
D = np.zeros((x.size, y.size, 2))
for i in range(X.shape[0]):
	for j in range(X.shape[1]):
		mag = np.sqrt(U[i, j]**2 + V[i, j]**2)
		du = U[i, j]/mag
		dv = V[i, j]/mag
		D[i, j] = [du, dv]

plt.quiver(X, Y, D[:, :, 0], D[:, :, 1], M, scale_units="xy", units = "xy")
plt.colorbar()
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("$f(x, y) = x^2\sin(y)$")
plt.savefig("partial_example2.png")
plt.show()

fig = plt.figure()
ax = fig.gca(projection = "3d")

surf = ax.plot_surface(X, Y, F)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title("$f(x, y) = x^2\sin(y)$")
plt.savefig("partial_example3.png")
plt.show()