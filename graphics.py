import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from main import *

x = Ellipse(e=0.9, arg=np.pi / 4, i=0.1, longitude=np.pi / 4)
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')
dots = np.array(x.cords)
print(x.cords)
ax.plot(dots[:, 0], dots[:, 1], dots[:, 2])
ax.plot([0, x.v1[0]], [0, x.v1[1]], [0, x.v1[2]])
ax.plot([0, x.v2[0]], [0, x.v2[1]], [0, x.v2[2]])
ax.plot([0, x.v3[0]], [0, x.v3[1]], [0, x.v3[2]])

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()
