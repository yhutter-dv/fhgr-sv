import numpy as np
import matplotlib.pyplot as plt

data_u = np.loadtxt('u.dat')
data_v = np.loadtxt('v.dat')

x = np.linspace(0, 1, data_u.shape[0])
y = np.linspace(0, 1, data_u.shape[1])
X, Y = np.meshgrid(x, y)

color = np.sqrt(data_u**2 + data_v**2)
seed = np.array([0.5*np.ones(20), np.linspace(0,1,20)])
#seed = np.array([np.linspace(0,1,20), 0.5*np.ones(20)])
#seed = np.array([np.random.rand(50), np.random.rand(50)])

fig, ax = plt.subplots()
stream = ax.streamplot(X, Y, data_u, data_v, color=color, start_points=seed.T)
ax.plot(seed[0], seed[1], 'b.')
ax.set_aspect('equal')
fig.colorbar(stream.lines)
plt.show()
