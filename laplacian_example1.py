import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D

#f(x, y) = sin(x) + sin(y)
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
F = np.sin(X) + np.sin(Y)

fig = plt.figure()
ax = fig.gca(projection = "3d")
ax.plot_surface(X, Y, F, antialiased = False)
ax.set_title("$f(x, y) = \sin(x) + \sin(y)$")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_zlabel("$f$")

plt.savefig("laplacian_example1.png")
plt.show()

#cut, line and wireframe, in direction [1, 2] passing through the origin
X_cut, Y_cut = np.meshgrid(x, y)
for i in range(X_cut.shape[0]):
	for j in range(X_cut.shape[1]):
		if 2*X_cut[i, j] - Y_cut[i, j] >= 0:
			X_cut[i, j] = None
			Y_cut[i, j] = None
F_cut = np.sin(X) + np.sin(Y)

fig = plt.figure()
ax = plt.gca(projection = "3d")

ax.plot_surface(X_cut, Y_cut, F_cut, antialiased = False)

x_line = np.array(np.linspace(np.nanmax(X_cut[0]), np.nanmax(X_cut), 150))
y_line = np.array(np.linspace(np.nanmin(Y_cut), np.nanmax(Y_cut), 150))
f_line = np.sin(x_line) + np.sin(y_line)

ax.plot(x_line, y_line, f_line, "r", lw=5)

X_mesh = np.array([x_line for i in range(len(x_line))])
Y_mesh = np.array([y_line for i in range(len(y_line))])
f_mesh = np.linspace(F.min(), F.max(), X_mesh.shape[0])
F_temp, F_mesh = np.meshgrid(np.ones(X_mesh.shape[0]), f_mesh)
ax.plot_wireframe(X_mesh, Y_mesh, F_mesh, rstride = 10, cstride = 10)

ax.set_title("$f(x, y) = \sin(x) + \sin(y)$")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_zlabel("$f$")

plt.show()

#2d line plot
fig = plt.figure()
ax = fig.gca()
k_line = [np.sqrt(xi**2 + yi**2)*xi/abs(xi) for xi, yi in zip(x_line, y_line)]

ax.plot(k_line, f_line)
ax.set_title("$f(x, y) = \sin(x) + \sin(y)$ cut in direction $[1, 2]$")
ax.set_xlabel("$k$")
ax.set_ylabel("$f$")

plt.show()

#1st derivative and directional derivative = (np.cos(x) + np.cos(y))/np.sqrt(2)
fig, ax = plt.subplots(1, 1)

dk = k_line[1] - k_line[0]
fdk_line = []
for i in range(len(k_line)):
	if i == 0:
		fdk_line.append((f_line[1]-f_line[0])/dk)
	elif i == len(k_line) - 1:
		fdk_line.append((f_line[i]-f_line[i-1])/dk)
	else:
		fdk_line.append((f_line[i+1]-f_line[i-1])/(2*dk))

dd_line = [(np.cos(xi) + 2*np.cos(yi))/np.sqrt(5) for xi, yi in zip(x_line, y_line)]

ax.plot(k_line[1:-2], fdk_line[1:-2])
ax.plot(k_line, dd_line)

plt.show()

#2nd derivative and Laplacian = -np.sin(x) - np.sin(y)
fig, ax = plt.subplots(1, 1)

fddk_line = []
for i in range(len(k_line)):
	if i == 0:
		fddk_line.append((fdk_line[1]-fdk_line[0])/dk)
	elif i == len(k_line) - 1:
		fddk_line.append((fdk_line[i]-fdk_line[i-1])/dk)
	else:
		fddk_line.append((fdk_line[i+1]-fdk_line[i-1])/(2*dk))

lap_line = [- np.sin(xi) - np.sin(yi) for xi, yi in zip(x_line, y_line)]

ax.plot(k_line[2:-3], fddk_line[2:-3])
ax.plot(k_line, lap_line)


plt.show()