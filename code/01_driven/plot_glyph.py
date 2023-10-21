import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Circle

data = np.loadtxt('p.dat')
data = np.rot90(data, 3)

circles = []
for x in range(0, data.shape[0], 1):
  for y in range(0, data.shape[1], 1):
    circles.append(Circle((x,y), 1.5*data[x,y]))

fig, ax = plt.subplots()
collection = PatchCollection(circles, cmap=plt.cm.jet)
ax.add_collection(collection)
ax.set_xlim(data.shape[0])
ax.set_ylim(data.shape[1])
ax.set_aspect('equal')
plt.show()
