import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib import animation

#f(x, y) = sin(x) + sin(y)
#vector field
n_vect = 20
x_lim = 4
y_lim = 4
x_vect = np.linspace(-x_lim, x_lim, n_vect)
y_vect = np.linspace(-y_lim, y_lim, n_vect)
X_vect, Y_vect = np.meshgrid(x_vect, y_vect)
P = np.cos(X_vect)
Q = np.cos(Y_vect)
colours = np.sqrt(P**2 + Q**2)
P_vect = P/colours
Q_vect = Q/colours

fig = plt.figure()
ax = fig.gca()

vect_field = ax.quiver(X_vect, Y_vect, P_vect, Q_vect, colours, scale_units = "xy", angles = "xy")

ax.set_title("$f(x, y) = \sin(x) + \sin(y)$")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
fig.colorbar(vect_field)

plt.savefig("laplacian_example2.png")
plt.show()