import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

N = 100
x = np.linspace(-3, 3, N)
y = np.linspace(-3, 3, N)

x_coord = -1
y_coord = 1
f_coord = (x_coord**2)*y_coord + np.sin(y_coord)

X, Y = np.meshgrid(x, y)
f = (X**2)*Y + np.sin(Y)

#Surface
fig = plt.figure()
ax = fig.gca(projection="3d")

surf = ax.plot_surface(X, Y, f, antialiased = False)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title("$f(x, y) = x^2y + \sin(y)$")

plt.savefig("partial_example1-1.png")
plt.show()

X1, Y1 = np.meshgrid(np.linspace(-3, x_coord), y)
f1 = (X1**2)*Y1 + np.sin(Y1)
Xcut1, Ycut1 = np.meshgrid([x_coord]*N, y)
fcut1 = (X/3)*f.max()
xline1 = [x_coord]*N
yline1 = y
fline1 = [(xi**2)*yi + np.sin(yi) for xi, yi in zip(xline1, yline1)]

#First cut surface
fig = plt.figure()
ax = fig.gca(projection="3d")

surf = ax.plot_surface(X1, Y1, f1, antialiased = False)
surfcut = ax.plot_wireframe(Xcut1, Ycut1, fcut1, rstride=10, cstride=10)
ax.plot(xline1, yline1, fline1, "r", linewidth=3)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title("$f(x, y) = x^2y + \sin(y)$")

plt.savefig("partial_example1-2.png")
plt.show()

X2, Y2 = np.meshgrid(x, np.linspace(y_coord, 3, N))
f2 = (X2**2)*Y2 + np.sin(Y2)
Xcut2, Ycut2 = np.meshgrid(x, [y_coord]*N)
fcut2 = (Y/3)*f.max()
xline2 = x
yline2 = [y_coord]*N
fline2 = [(xi**2)*yi + np.sin(yi) for xi, yi in zip(xline2, yline2)]

#Second cut surface
fig = plt.figure()
ax = fig.gca(projection="3d")

surf = ax.plot_surface(X2, Y2, f2, antialiased = False)
surfcut = ax.plot_wireframe(Xcut2, Ycut2, fcut2, rstride=10, cstride=10)
ax.plot(xline2, yline2, fline2, "r", linewidth=3)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title("$f(x, y) = x^2y + \sin(y)$")

plt.savefig("partial_example1-3.png")
plt.show()

dx = 0.01
dy = 0.01
fx_grad = [(xi**2)*y_coord + np.sin(y_coord) for xi in [x_coord-dx, x_coord+dx]]
fy_grad = [(x_coord**2)*yi + np.sin(yi) for yi in [y_coord-dy, y_coord+dy]]
x_grad = (fx_grad[1]-fx_grad[0])/(2*dx)
y_grad = (fy_grad[1]-fy_grad[0])/(2*dy)
x_gradline = [-3, -0.5]
y_gradline = [-3, 2]
fx_gradline = [x_grad*(xi-x_coord) + f_coord for xi in x_gradline]
fy_gradline = [y_grad*(yi-y_coord) + f_coord for yi in y_gradline]

#First cut line
plt.plot(yline1, fline1)
plt.plot(y_gradline, fy_gradline, "--")
plt.plot([y_coord], [f_coord], "o")
plt.xlabel("$y$")
plt.ylabel("$f$")
plt.title("Cut at x = {} of $f(x, y) = x^2y + \sin(y)$".format(x_coord))

plt.savefig("partial_example1-4.png")
plt.show()

#Second cut line
plt.plot(xline2, fline2)
plt.plot(x_gradline, fx_gradline, "--")
plt.plot([x_coord], [f_coord], "o")
plt.xlabel("$x$")
plt.ylabel("$f$")
plt.title("Cut at y = {} of $f(x, y) = x^2y + \sin(y)$".format(y_coord))

plt.savefig("partial_example1-5.png")
plt.show()