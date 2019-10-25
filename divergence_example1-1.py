import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
#Success!!

#f = xsin(y)
x_vect = np.linspace(-5, 5, 20)
y_vect = np.linspace(-5, 5, 20)
X_vect, Y_vect = np.meshgrid(x_vect, y_vect)
U = np.sin(Y_vect)
V = X_vect*np.cos(Y_vect)
colors = np.sqrt(U**2 + V**2)
U_vect = U/colors
V_vect = V/colors

fig = plt.figure()
ax = plt.gca()

ax.quiver(X_vect, Y_vect, U_vect, V_vect, colors, scale_units = "xy", angles = "xy")

x_points = np.linspace(-5, 5, 20)
y_points = np.linspace(-5, 5, 20)
X_points, Y_points = np.meshgrid(x_points, y_points)

points = ax.scatter([], [])
dx = 0.01
dy = 0.01

def init():
	global X_points, Y_points
	points.set_offsets([[None,None]]*X_points.shape[0]**2)
	return points

def update(i):
	global X_points, Y_points, dx, dy
	U_points = np.sin(Y_points)
	V_points = X_points*np.cos(Y_points)
	X_points = X_points + U_points*dx
	Y_points = Y_points + V_points*dy
	for i in range(X_points.shape[0]):
		for j in range(X_points.shape[1]):
			if X_points[i, j] < -5 or X_points[i, j] > 5 or Y_points[i, j] < -5 or Y_points[i, j] > 5:
				X_points[i, j] = np.random.random()*10 - 5
				Y_points[i, j] = np.random.random()*10 - 5
	x_coords = X_points.flatten()
	y_coords = Y_points.flatten()
	coords = []
	for j in range(len(x_coords)):
		coords.append([x_coords[j], y_coords[j]])
	points.set_offsets(coords)
	return points, X_points, Y_points

ax.set_title("$f(x, y) = x\sin(y)$")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")

anim = animation.FuncAnimation(fig, update, init_func=init, frames=400, interval=10)

plt.show()