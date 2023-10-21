import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('p.dat')
data = np.transpose(data)
data = np.rot90(data, 1)

plt.imshow(data, cmap=plt.cm.seismic)
#plt.imshow(data, cmap=plt.cm.ocean)
plt.colorbar()
plt.show()
