import numpy as np
import matplotlib.pyplot as plt

data_u = np.loadtxt('u.dat')
data_v = np.loadtxt('v.dat')

x = np.linspace(0, 1, data_u.shape[0])
y = np.linspace(0, 1, data_u.shape[1])
X, Y = np.meshgrid(x, y)

scale = 10.*np.max([np.max(data_u), np.max(data_v)])
st = 2 # stride factor

fig, ax = plt.subplots()
ax.quiver(X[::st,::st] , Y[::st,::st], data_u[::st,::st], data_v[::st,::st], scale=scale)
ax.set_aspect('equal')
plt.show()
