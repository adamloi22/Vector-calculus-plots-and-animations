import matplotlib.pyplot as plt
import numpy as np 

x_lim = 5
y_lim = 5

fig = plt.figure()
ax = fig.gca()

ax.set_xlim(-x_lim, x_lim)
ax.set_ylim(-y_lim, y_lim)

major_ticks = np.arange(-x_lim, x_lim, 1)
minor_ticks = np.arange(-x_lim, x_lim, 0.5)
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor = True)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor = True)
ax.grid(which = "major", alpha = 0.5)
ax.grid(which = "minor", alpha = 0.2)

ax.set_title("$f([x, y]) = [x + \sin(y), y + \sin(x)]$, before transformation")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")

x = 0
y = 0
x0 = -2
y0 = 3

ax.quiver(0, 0, x0, y0, scale_units = "xy", angles = "xy", scale = 1)

plt.savefig("jacobian_example3.png")
plt.show()


fig = plt.figure()
ax = fig.gca()

ax.set_xlim(-x_lim, x_lim)
ax.set_ylim(-y_lim, y_lim)

major_ticks = np.arange(-x_lim, x_lim, 1)
minor_ticks = np.arange(-x_lim, x_lim, 0.5)
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor = True)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor = True)
ax.grid(which = "major", alpha = 0.5)
ax.grid(which = "minor", alpha = 0.2)

ax.set_title("$f([x, y]) = [x + \sin(y), y + \sin(x)]$, after transformation")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")

p = x0 + np.sin(y0)
q = y0 + np.sin(x0)

ax.quiver(0, 0, p, q, color = "red", scale_units = "xy", angles = "xy", scale = 1)

plt.savefig("jacobian_example4.png")
plt.show()