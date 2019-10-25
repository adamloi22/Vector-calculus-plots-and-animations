import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib import animation

#v = [sin(x), sin(y)]
x_lim = 5
y_lim = 5
N_vect = 20
#vector field
x_vect = np.linspace(-x_lim, x_lim, N_vect)
y_vect = np.linspace(-y_lim, y_lim, N_vect)
X_vect, Y_vect = np.meshgrid(x_vect, y_vect)
P_vect = np.sin(Y_vect)
Q_vect = np.sin(X_vect)
colors = np.sqrt(P_vect**2 + Q_vect**2)
P_vect = P_vect/colors
Q_vect = Q_vect/colors

fig = plt.figure()
ax = fig.gca()

ax.quiver(X_vect, Y_vect, P_vect, Q_vect, colors, scale_units = "xy", angles = "xy")

#animation
N_points = 40
x_points = np.linspace(-x_lim, x_lim, N_points)
y_points = np.linspace(-y_lim, y_lim, N_points)
X_points, Y_points = np.meshgrid(x_points, y_points)
X_pointsi, Y_pointsi = np.meshgrid(x_points, y_points)
points = ax.scatter([], [])
dx = 0.01
dy = 0.01

def init():
	global X_points
	points.set_offsets([[None, None]]*X_points.shape[0]**2)
	return points

def update(i):
	global X_points, Y_points, X_pointsi, Y_pointsi, dx, dy
	P_points = np.sin(Y_points)
	Q_points = np.sin(X_points)
	X_points = X_points + P_points*dx
	Y_points = Y_points + Q_points*dx
	x_coords = X_points.flatten()
	y_coords = Y_points.flatten()
	coords = []
	for j in range(len(x_coords)):
		coords.append([x_coords[j], y_coords[j]])
	points.set_offsets(coords)
	return points, X_points, Y_points

anim = animation.FuncAnimation(fig, update, init_func = init, frames = 200, interval = 15)

ax.set_title("$v(x, y) = [\sin(y), \sin(x)]$")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")

plt.show()