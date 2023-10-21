import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Circle

data = np.zeros([3,34,34])
data[0] = np.loadtxt('rho001.dat')
data[1] = np.loadtxt('rho010.dat')
data[2] = np.loadtxt('rho050.dat')

for i in range(3):
  data[i] = np.rot90(data[i], 2)
  circles = []
  for x in range(data[i].shape[0]):
    for y in range(data[i].shape[1]):
      circles.append(Circle((x,y), 0.25*data[i,x,y]))

  fig, ax = plt.subplots()
  collection = PatchCollection(circles, cmap=plt.cm.jet)
  ax.add_collection(collection)
  ax.set_xlim(data[i].shape[0])
  ax.set_ylim(data[i].shape[1])
  ax.set_aspect('equal')
  plt.show()
