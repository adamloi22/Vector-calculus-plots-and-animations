import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 40)
y = np.linspace(-10, 10, 40)
X, Y = np.meshgrid(x, y)

F = X*Y
U = Y
V = X
colors = np.sqrt(U**2 + V**2)

du = U/colors
dv = V/colors

cmap = plt.contour(X, Y, F, np.arange(F.min(), F.max(), 10), colors="black")
plt.clabel(cmap, inline=1)
plt.quiver(X, Y, du, dv, colors)
plt.colorbar()
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("$f(x, y) = xy$")
plt.savefig("partial_example4.png")
plt.show()