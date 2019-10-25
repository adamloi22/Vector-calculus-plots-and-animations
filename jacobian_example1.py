import matplotlib.pyplot as plt
import numpy as np 

#f([x, y])=[x+sin(y), y+sin(x)]
x_lim = 5
y_lim = 5
N = 200
x_coord = -2
y_coord = 3
square_size = 0.1

def plot_jacobian1():
	fig = plt.figure()
	ax = fig.gca()

	ax.set_xlim(-x_lim, x_lim)
	ax.set_ylim(-y_lim, y_lim)

	xvert_coords = []
	yvert_coords = []
	for i in range(-x_lim, x_lim+1):
		xvert_coords.append([i]*N)
		yvert_coords.append(np.linspace(-y_lim, y_lim, N))

	temp = 0
	for x_coords, y_coords in zip(xvert_coords, yvert_coords):
		if temp == x_lim:
			ax.plot(x_coords, y_coords, "g")
		else:
			ax.plot(x_coords, y_coords, "r")
		temp += 1

	xhor_coords = []
	yhor_coords = []
	for i in range(-x_lim, x_lim+1):
		yhor_coords.append([i]*N)
		xhor_coords.append(np.linspace(-y_lim, y_lim, N))

	temp = 0
	for x_coords, y_coords in zip(xhor_coords, yhor_coords):
		if temp == y_lim:
			ax.plot(x_coords, y_coords, "g")
		else:
			ax.plot(x_coords, y_coords, "r")
		temp += 1

	major_xticks = np.arange(-x_lim, x_lim, 1)
	minor_xticks = np.arange(-x_lim, x_lim, 0.5)
	major_yticks = np.arange(-x_lim, x_lim, 1)
	minor_yticks = np.arange(-x_lim, x_lim, 0.5)
	
	ax.set_xticks(major_xticks)
	ax.set_xticks(minor_xticks, minor = True)
	ax.set_yticks(major_yticks)
	ax.set_yticks(minor_yticks, minor = True)

	ax.grid(which = "major", alpha = 0.5)
	ax.grid(which = "minor", alpha = 0.2)

	ax.set_xlabel("$x$")
	ax.set_ylabel("$y$")
	ax.set_title("$f([x, y]) = [x + \sin(y), y + \sin(x)]$, before transformation")

	plt.savefig("jacobian_example1.png")
	plt.show()

def plot_jacobian2():
	fig = plt.figure()
	ax = fig.gca()

	ax.set_xlim(-x_lim, x_lim)
	ax.set_ylim(-y_lim, y_lim)

	xvert_coords = []
	yvert_coords = []
	for i in range(-x_lim, x_lim+1):
		xvert_coords.append([i]*N)
		yvert_coords.append(np.linspace(-y_lim, y_lim, N))

	xhor_coords = []
	yhor_coords = []
	for i in range(-x_lim, x_lim+1):
		yhor_coords.append([i]*N)
		xhor_coords.append(np.linspace(-y_lim, y_lim, N))

	Xvert_coords = np.array(xvert_coords) + np.sin(np.array(yvert_coords))
	Yvert_coords = np.array(yvert_coords) + np.sin(np.array(xvert_coords))
	Xhor_coords = np.array(xhor_coords) + np.sin(np.array(yhor_coords))
	Yhor_coords = np.array(yhor_coords) + np.sin(np.array(xhor_coords))

	temp = 0
	for x_coords, y_coords in zip(Xvert_coords, Yvert_coords):
		if temp == x_lim:
			ax.plot(x_coords, y_coords, "g")
		else:
			ax.plot(x_coords, y_coords, "r")
		temp += 1

	temp = 0
	for x_coords, y_coords in zip(Xhor_coords, Yhor_coords):
		if temp == y_lim:
			ax.plot(x_coords, y_coords, "g")
		else:
			ax.plot(x_coords, y_coords, "r")
		temp += 1

	major_xticks = np.arange(-x_lim, x_lim, 1)
	minor_xticks = np.arange(-x_lim, x_lim, 0.5)
	major_yticks = np.arange(-x_lim, x_lim, 1)
	minor_yticks = np.arange(-x_lim, x_lim, 0.5)
	
	ax.set_xticks(major_xticks)
	ax.set_xticks(minor_xticks, minor = True)
	ax.set_yticks(major_yticks)
	ax.set_yticks(minor_yticks, minor = True)

	ax.grid(which = "major", alpha = 0.5)
	ax.grid(which = "minor", alpha = 0.2)

	ax.set_xlabel("$x$")
	ax.set_ylabel("$y$")
	ax.set_title("$f([x, y]) = [x + \sin(y), y + \sin(x)]$, after transformation")

	plt.savefig("jacobian_example2.png")
	plt.show()

def plot_jacobian5_6():
	fig = plt.figure()
	ax = fig.gca()

	ax.set_xlim(-x_lim, x_lim)
	ax.set_ylim(-y_lim, y_lim)

	xvert_coords = []
	yvert_coords = []
	for i in range(-x_lim, x_lim+1):
		xvert_coords.append([i]*N)
		yvert_coords.append(np.linspace(-y_lim, y_lim, N))

	temp = 0
	for x_coords, y_coords in zip(xvert_coords, yvert_coords):
		if temp == x_lim:
			ax.plot(x_coords, y_coords, "g")
		else:
			ax.plot(x_coords, y_coords, "r")
		temp += 1

	xhor_coords = []
	yhor_coords = []
	for i in range(-x_lim, x_lim+1):
		yhor_coords.append([i]*N)
		xhor_coords.append(np.linspace(-y_lim, y_lim, N))

	temp = 0
	for x_coords, y_coords in zip(xhor_coords, yhor_coords):
		if temp == y_lim:
			ax.plot(x_coords, y_coords, "g")
		else:
			ax.plot(x_coords, y_coords, "r")
		temp += 1

	square_xvert_coords = []
	square_yvert_coords = []
	for i in range(5):
		square_xvert_coords.append([x_coord + i*(square_size/4) - square_size/2]*N)
		square_yvert_coords.append(np.linspace(-y_lim, y_lim, N))

	temp = 0
	for x_coords, y_coords in zip(square_xvert_coords, square_yvert_coords):
		if temp == 2:
			ax.plot(x_coords, y_coords, "b")
		else:
			ax.plot(x_coords, y_coords, "c")
		temp += 1

	square_xhor_coords = []
	square_yhor_coords = []
	for i in range(5):
		square_yhor_coords.append([y_coord - i*(square_size/4) + square_size/2]*N)
		square_xhor_coords.append(np.linspace(-y_lim, y_lim, N))

	temp = 0
	for x_coords, y_coords in zip(square_xhor_coords, square_yhor_coords):
		if temp == 2:
			ax.plot(x_coords, y_coords, "b")
		else:
			ax.plot(x_coords, y_coords, "c")
		temp += 1

	major_xticks = np.arange(-x_lim, x_lim, 1)
	minor_xticks = np.arange(-x_lim, x_lim, 0.5)
	major_yticks = np.arange(-x_lim, x_lim, 1)
	minor_yticks = np.arange(-x_lim, x_lim, 0.5)

	square_major_xticks = np.linspace(x_coord - square_size/2, x_coord + square_size/2, 5)
	square_major_yticks = np.linspace(y_coord - square_size/2, y_coord + square_size/2, 5)
	major_xticks = np.concatenate((major_xticks, square_major_xticks))
	major_yticks = np.concatenate((major_yticks, square_major_yticks))	

	square_minor_xticks = np.linspace(x_coord - square_size/2, x_coord + square_size/2, 9)
	square_minor_yticks = np.linspace(y_coord - square_size/2, y_coord + square_size/2, 9)
	minor_xticks = np.concatenate((minor_xticks, square_minor_xticks))
	minor_yticks = np.concatenate((minor_yticks, square_minor_yticks))

	ax.set_xticks(major_xticks)
	ax.set_xticks(minor_xticks, minor = True)
	ax.set_yticks(major_yticks)
	ax.set_yticks(minor_yticks, minor = True)

	ax.grid(which = "major", alpha = 0.5)
	ax.grid(which = "minor", alpha = 0.2)

	ax.set_xlabel("$x$")
	ax.set_ylabel("$y$")
	ax.set_title("$f([x, y]) = [x + \sin(y), y + \sin(x)]$, before transformation")

	plt.savefig("jacobian_example5.png")
	plt.show()

def plot_jacobian7_8():
	fig = plt.figure()
	ax = fig.gca()

	ax.set_xlim(-x_lim, x_lim)
	ax.set_ylim(-y_lim, y_lim)

	xvert_coords = []
	yvert_coords = []
	for i in range(-x_lim, x_lim+1):
		xvert_coords.append([i]*N)
		yvert_coords.append(np.linspace(-y_lim, y_lim, N))

	xhor_coords = []
	yhor_coords = []
	for i in range(-x_lim, x_lim+1):
		yhor_coords.append([i]*N)
		xhor_coords.append(np.linspace(-y_lim, y_lim, N))

	Xvert_coords = np.array(xvert_coords) + np.sin(np.array(yvert_coords))
	Yvert_coords = np.array(yvert_coords) + np.sin(np.array(xvert_coords))
	Xhor_coords = np.array(xhor_coords) + np.sin(np.array(yhor_coords))
	Yhor_coords = np.array(yhor_coords) + np.sin(np.array(xhor_coords))

	temp = 0
	for x_coords, y_coords in zip(Xvert_coords, Yvert_coords):
		if temp == x_lim:
			ax.plot(x_coords, y_coords, "g")
		else:
			ax.plot(x_coords, y_coords, "r")
		temp += 1

	temp = 0
	for x_coords, y_coords in zip(Xhor_coords, Yhor_coords):
		if temp == y_lim:
			ax.plot(x_coords, y_coords, "g")
		else:
			ax.plot(x_coords, y_coords, "r")
		temp += 1

	square_xvert_coords = []
	square_yvert_coords = []
	for i in range(5):
		square_xvert_coords.append([x_coord - i*(square_size/4) + square_size/2]*N)
		square_yvert_coords.append(np.linspace(-y_lim, y_lim, N))

	square_xhor_coords = []
	square_yhor_coords = []
	for i in range(5):
		square_yhor_coords.append([y_coord - i*(square_size/4) + square_size/2]*N)
		square_xhor_coords.append(np.linspace(-y_lim, y_lim, N))

	square_Xvert_coords = np.array(square_xvert_coords) + np.sin(np.array(square_yvert_coords))
	square_Yvert_coords = np.array(square_yvert_coords) + np.sin(np.array(square_xvert_coords))
	square_Xhor_coords = np.array(square_xhor_coords) + np.sin(np.array(square_yhor_coords))
	square_Yhor_coords = np.array(square_yhor_coords) + np.sin(np.array(square_xhor_coords))	

	temp = 0
	for x_coords, y_coords in zip(square_Xvert_coords, square_Yvert_coords):
		if temp == 2:
			ax.plot(x_coords, y_coords, "b")
		else:
			ax.plot(x_coords, y_coords, "c")
		temp += 1

	temp = 0
	for x_coords, y_coords in zip(square_Xhor_coords, square_Yhor_coords):
		if temp == 2:
			ax.plot(x_coords, y_coords, "b")
		else:
			ax.plot(x_coords, y_coords, "c")
		temp += 1

	x_coord_new = x_coord + np.sin(y_coord)
	y_coord_new = y_coord + np.sin(x_coord)

	major_xticks = np.arange(-x_lim, x_lim, 1)
	minor_xticks = np.arange(-x_lim, x_lim, 0.5)
	major_yticks = np.arange(-x_lim, x_lim, 1)
	minor_yticks = np.arange(-x_lim, x_lim, 0.5)

	square_major_xticks = np.linspace(x_coord_new - square_size/2, x_coord_new + square_size/2, 5)
	square_major_yticks = np.linspace(y_coord_new - square_size/2, y_coord_new + square_size/2, 5)
	major_xticks = np.concatenate((major_xticks, square_major_xticks))
	major_yticks = np.concatenate((major_yticks, square_major_yticks))	

	square_minor_xticks = np.linspace(x_coord_new - square_size/2, x_coord_new + square_size/2, 9)
	square_minor_yticks = np.linspace(y_coord_new - square_size/2, y_coord_new + square_size/2, 9)
	minor_xticks = np.concatenate((minor_xticks, square_minor_xticks))
	minor_yticks = np.concatenate((minor_yticks, square_minor_yticks))
	
	ax.set_xticks(major_xticks)
	ax.set_xticks(minor_xticks, minor = True)
	ax.set_yticks(major_yticks)
	ax.set_yticks(minor_yticks, minor = True)

	ax.grid(which = "major", alpha = 0.5)
	ax.grid(which = "minor", alpha = 0.2)

	ax.set_xlabel("$x$")
	ax.set_ylabel("$y$")
	ax.set_title("$f([x, y]) = [x + \sin(y), y + \sin(x)]$, after transformation")

	plt.savefig("jacobian_example7.png")
	plt.show()

if __name__ == "__main__":
	plot_jacobian1()
	plot_jacobian2()
	plot_jacobian5_6()
	plot_jacobian7_8()