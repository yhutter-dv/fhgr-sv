import numpy as np
import matplotlib.pyplot as plt

data_u = np.loadtxt('u.dat')
data_v = np.loadtxt('v.dat')

x = np.linspace(0, 1, data_u.shape[0])
y = np.linspace(0, 1, data_u.shape[1])
X, Y = np.meshgrid(x, y)

color = np.sqrt(data_u**2 + data_v**2)

fig, ax = plt.subplots()
stream = ax.streamplot(X, Y, data_u, data_v, color=color)
ax.set_aspect('equal')
fig.colorbar(stream.lines)
plt.show()
