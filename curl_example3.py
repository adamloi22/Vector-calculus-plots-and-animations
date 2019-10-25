import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib import animation

#v(x, y) = [y^3-9y, x^3-9x]
x_lim = 5
y_lim = 5
N_vect = 20
#vector field
x_vect = np.linspace(-x_lim, x_lim, N_vect)
y_vect = np.linspace(-y_lim, y_lim, N_vect)
X_vect, Y_vect = np.meshgrid(x_vect, y_vect)
P_vect = Y_vect**3 - 9*Y_vect
Q_vect = X_vect**3 - 9*X_vect
colors = np.sqrt(P_vect**2 + Q_vect**2)
P_vect = P_vect/colors
Q_vect = Q_vect/colors

fig = plt.figure()
ax = fig.gca()

ax.quiver(X_vect, Y_vect, P_vect, Q_vect, colors, scale_units = "xy", angles = "xy")

#contour lines
x_cont = np.linspace(-x_lim, x_lim, 50)
y_cont = np.linspace(-y_lim, y_lim, 50)
X_cont, Y_cont = np.meshgrid(x_cont, y_cont)
P_cont = Y_cont**3 - 9*Y_cont
Q_cont = X_cont**3 - 9*X_cont
mags = np.sqrt(P_cont**2 + Q_cont**2)
P_cont = P_cont/mags
Q_cont = Q_cont/mags
ax.contour(X_cont, Y_cont, mags)

#animation
N_points = 30
x_points = np.linspace(-x_lim, x_lim, N_points)
y_points = np.linspace(-y_lim, y_lim, N_points)
X_points, Y_points = np.meshgrid(x_points, y_points)
X_pointsi, Y_pointsi = np.meshgrid(x_points, y_points)
points = ax.scatter([], [])
dx = 0.001
dy = 0.001

def init():
	global X_points
	points.set_offsets([[None, None]]*X_points.shape[0]**2)
	return points

def update(i):
	global X_points, Y_points, X_pointsi, Y_pointsi, dx, dy, x_lim, y_lim
	P_points = Y_points**3 - 9*Y_points
	Q_points = X_points**3 - 9*X_points
	X_points = X_points + P_points*dx
	Y_points = Y_points + Q_points*dx
	for j in range(X_points.shape[0]):
		for k in range(X_points.shape[1]):
			if X_points[j, k] < -x_lim - 2 or X_points[j, k] > x_lim + 2 or Y_points[j, k] < -y_lim - 2 or Y_points[j, k] > y_lim + 2:
				X_points[j, k] = X_pointsi[np.random.randint(-X_pointsi.shape[0], X_pointsi.shape[0]), np.random.randint(-X_pointsi.shape[0], X_pointsi.shape[0])]
				Y_points[j, k] = Y_pointsi[np.random.randint(-X_pointsi.shape[0], X_pointsi.shape[0]), np.random.randint(-X_pointsi.shape[0], X_pointsi.shape[0])]
	x_coords = X_points.flatten()
	y_coords = Y_points.flatten()
	coords = []
	for j in range(len(x_coords)):
		coords.append([x_coords[j], y_coords[j]])
	points.set_offsets(coords)
	return points, X_points, Y_points

anim = animation.FuncAnimation(fig, update, init_func = init, frames = 200, interval = 15)

ax.set_title("$v(x, y) = [y^3 - 9y, x^3 - 9x]$")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")

plt.show()