from matplotlib import pyplot as plt
import numpy as np

v = np.loadtxt('./models/mug_v.dat')
f = np.loadtxt('./models/mug_f.dat', dtype=int)

fig = plt.figure()
ax = plt.axes(projection='3d')
for i in range(int(f.size/4)):
	ax.plot([v[f[i,1],0], v[f[i,2],0]], [v[f[i,1],1], v[f[i,2],1]], zs=[v[f[i,1],2], v[f[i,2],2]], color='blue', linewidth=0.5)
	ax.plot([v[f[i,2],0], v[f[i,3],0]], [v[f[i,2],1], v[f[i,3],1]], zs=[v[f[i,2],2], v[f[i,3],2]], color='blue', linewidth=0.5)
	ax.plot([v[f[i,3],0], v[f[i,1],0]], [v[f[i,3],1], v[f[i,1],1]], zs=[v[f[i,3],2], v[f[i,1],2]], color='blue', linewidth=0.5)
ax.set_box_aspect((np.ptp(v[:,0]), np.ptp(v[:,1]), np.ptp(v[:,2])))
plt.show()
