import matplotlib.pyplot as plt
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

LIM = 5
SCAT_NUM = 40

def plot_laplacian3():
	x = np.linspace(-LIM, LIM, 30)
	y = np.linspace(-LIM, LIM, 30)
	X, Y = np.meshgrid(x, y)
	F = np.e**(X)*np.sin(Y)

	fig = plt.figure()
	ax = fig.gca(projection = "3d")
	ax.plot_surface(X, Y, F, antialiased = False)
	ax.set_title("$f(x, y) = e^x\sin(y)$")
	ax.set_xlabel("$x$")
	ax.set_ylabel("$y$")
	ax.set_zlabel("$f$")

	plt.savefig("laplacian_example3.png")
	plt.show()	

def plot_laplacian4():
	x = np.linspace(-LIM, LIM, 30)
	y = np.linspace(-LIM, LIM, 30)
	X, Y = np.meshgrid(x, y)
	P = np.e**(X)*np.sin(Y)
	Q = np.e**(X)*np.cos(Y)
	colours = np.sqrt(P**2 + Q**2)
	P = P/colours
	Q = Q/colours

	fig = plt.figure()
	ax = fig.gca()
	vect_field = ax.quiver(X, Y, P, Q, colours, scale_units = "xy", angles = "xy")
	ax.set_title("Gradient field of $f(x, y) = e^x\sin(y)$")
	ax.set_xlabel("$x$")
	ax.set_ylabel("$y$")
	plt.colorbar(vect_field)

	plt.savefig("laplacian_example4")

	x_points = np.linspace(-LIM, LIM, SCAT_NUM)
	y_points = np.linspace(-LIM, LIM, SCAT_NUM)
	X_points, Y_points = np.meshgrid(x_points, y_points)
	X_pointsi, Y_pointsi = np.meshgrid(x_points, y_points)
	points = ax.scatter([], [])
	dx = 0.001
	dy = dx

	def init():
		nonlocal X_points, Y_points
		points.set_offsets([[None, None]])
		return points, X_points, Y_points

	def update(i):
		nonlocal X_points, Y_points, X_pointsi, Y_pointsi, dx, dy
		P_points = np.e**(X_points)*np.sin(Y_points)
		Q_points = np.e**(X_points)*np.cos(Y_points)
		X_points += P_points*dx
		Y_points += Q_points*dy
		for i in range(SCAT_NUM):
			for j in range(SCAT_NUM):
				if X_points[i, j] > LIM + 2 or X_points[i, j] < -(LIM + 2) or Y_points[i, j] > LIM + 2 or Y_points[i, j] < -(LIM + 2):
					X_points[i, j] = X_pointsi[np.random.randint(0, SCAT_NUM-1), np.random.randint(0, SCAT_NUM-1)]
					Y_points[i, j] = Y_pointsi[np.random.randint(0, SCAT_NUM-1), np.random.randint(0, SCAT_NUM-1)]
		x_coords = X_points.flatten()
		y_coords = Y_points.flatten()
		coords = []
		for i in range(len(x_coords)):
			coords.append([x_coords[i], y_coords[i]])
		points.set_offsets(coords)
		return points, X_points, Y_points

	anim = animation.FuncAnimation(fig, update, init_func = init, frames = 100, interval = 10)

	plt.show()

if __name__ == "__main__":
	plot_laplacian3()
	plot_laplacian4()