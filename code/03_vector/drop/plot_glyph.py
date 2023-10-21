import numpy as np
import matplotlib.pyplot as plt

data_u = np.zeros([3,32,32])
data_v = np.zeros([3,32,32])
data_u[0] = np.loadtxt('u001.dat')
data_u[1] = np.loadtxt('u010.dat')
data_u[2] = np.loadtxt('u050.dat')
data_v[0] = np.loadtxt('v001.dat')
data_v[1] = np.loadtxt('v010.dat')
data_v[2] = np.loadtxt('v050.dat')

x = np.linspace(0, 1, data_u[0].shape[0])
y = np.linspace(0, 1, data_u[0].shape[1])
X, Y = np.meshgrid(x, y)

for i in range(3):
  color = np.sqrt(data_u[i]**2 + data_v[i]**2)
  fig, ax = plt.subplots()
  quiv = ax.quiver(X , Y, data_u[i].T, data_v[i].T, color, scale=20.)
  fig.colorbar(quiv)
  ax.set_aspect('equal')
  plt.show()