import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

N = 200
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)

X, Y = np.meshgrid(x, y)

F = X**2*Y

fig = plt.figure()
ax = fig.gca(projection = "3d")

surf = ax.plot_surface(X, Y, F, antialiased = False)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title("$f(x, y) = x^2y$")

plt.savefig("partial_example8-1.png")
plt.show()

x_line = []
y_line = []
f_line = []
for i in range(X.shape[0]):
	for j in range(X.shape[1]):
		if (X[i, j] - Y[i, j] > 0):
			X[i, j] = None
			Y[i, j] = None
		if (X[i, j] == Y[i, j]):
			x_line.append(X[i, j])
			y_line.append(Y[i, j])
			f_line.append(F[i, j])

X_cut, Y_cut = np.meshgrid(x_line, y_line)
f_cut = np.linspace(min(f_line), max(f_line), len(x_line), endpoint = True)
F_cut = np.array([f_cut for i in range(len(f_cut))])

fig = plt.figure()
ax = fig.gca(projection = "3d")

surf = ax.plot_surface(X, Y, F, antialiased = False)
surfcut = ax.plot_wireframe(Y_cut, Y_cut, F_cut, rstride = 10, cstride = 10)
ax.plot(x_line, y_line, f_line, "r", linewidth = 3)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title("$f(x, y) = x^2y$")

plt.savefig("partial_example8-2.png")
plt.show()

x_coord = -1
y_coord = -1
f_coord = x_coord**2*y_coord
dfdx = 2*x_coord*y_coord
dfdy = x_coord**2
x_gradline = [min(x_line), max(x_line)]
y_gradline = [min(y_line), max(y_line)]
f_gradline = [(min(x_line) - x_coord)*dfdx + (min(y_line) - y_coord)*dfdy + f_coord, (max(x_line) - x_coord)*dfdx + (max(y_line) - y_coord)*dfdy + f_coord]

fig = plt.figure()
ax = fig.gca(projection = "3d")

ax.plot(x_line, y_line, f_line, "r", linewidth = 3)
ax.plot(x_gradline, y_gradline, f_gradline, "--")
ax.plot([x_coord], [y_coord], [f_coord], "o")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title("$f(x, y) = x^2y$")

plt.savefig("partial_example8-3.png")
plt.show()