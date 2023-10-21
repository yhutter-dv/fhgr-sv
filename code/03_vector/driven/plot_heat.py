import numpy as np
import matplotlib.pyplot as plt

data_u = np.loadtxt('u.dat')
data_v = np.loadtxt('v.dat')
data_u = np.transpose(data_u)
data_u = np.rot90(data_u, 1)
data_v = np.transpose(data_v)
data_v = np.rot90(data_v, 1)

data = np.sqrt(data_u**2 + data_v**2)

plt.imshow(data, cmap=plt.cm.coolwarm)
plt.colorbar()
plt.show()
