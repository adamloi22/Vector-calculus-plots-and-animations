import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

#f is an inexact function
#vector field
x_vect = np.linspace(-5, 5, 20)
y_vect = np.linspace(-5, 5, 20)
X_vect, Y_vect = np.meshgrid(x_vect, y_vect)
U = np.ones(X_vect.shape)
V = np.sin(X_vect)
colors = np.sqrt(U**2 + V**2)
U_vect = U/colors
V_vect = V/colors

fig = plt.figure()
ax = plt.gca()

ax.quiver(X_vect, Y_vect, U_vect, V_vect, colors, scale_units = "xy", angles = "xy")

#circle
theta = np.linspace(0, 2*np.pi,100)
R = 2
x_circle = [R*np.sin(thetai) for thetai in theta]
y_circle = [R*np.cos(thetai) for thetai in theta]
ax.plot(x_circle, y_circle, "r")

#animation scatter plots
x_points = np.linspace(-7, 7, 20)
y_points = np.linspace(-7, 7, 20)
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
	U_points = np.ones(X_points.shape)
	V_points = np.sin(X_points)
	X_points = X_points + U_points*dx
	Y_points = Y_points + V_points*dy
	for i in range(X_points.shape[0]):
		for j in range(X_points.shape[1]):
			if X_points[i, j] > 7:
				X_points[i, j] = X_points[i, j] - 14
				Y_points[i, j] = Y_points[i, j]
				
	x_coords = X_points.flatten()
	y_coords = Y_points.flatten()
	coords = []
	for j in range(len(x_coords)):
		coords.append([x_coords[j], y_coords[j]])
	points.set_offsets(coords)
	return points, X_points, Y_points

ax.set_title("Inexact function. $U(x, y) = 1, V(x, y) = \sin(x)$")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")

anim = animation.FuncAnimation(fig, update, init_func=init, frames=400, interval=10)

plt.show()