import numpy as np
import matplotlib.pyplot as plt

data = np.zeros([3,32,32])
data_u = np.zeros([3,32,32])
data_v = np.zeros([3,32,32])
data_u[0] = np.loadtxt('u001.dat')
data_u[1] = np.loadtxt('u010.dat')
data_u[2] = np.loadtxt('u050.dat')
data_v[0] = np.loadtxt('v001.dat')
data_v[1] = np.loadtxt('v010.dat')
data_v[2] = np.loadtxt('v050.dat')

for i in range(3):
  data[i] = np.sqrt(data_u[i]**2 + data_v[i]**2)
  data[i] = np.rot90(data[i],1)
  plt.imshow(data[i], cmap=plt.cm.coolwarm)
  plt.colorbar()
  plt.show()