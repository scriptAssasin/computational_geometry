import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

# Generate 30 random 3D points
points = np.random.rand(30, 3)

# Compute the convex hull using the QuickHull algorithm from scipy.spatial
hull = ConvexHull(points)
print(hull)

# Plot the convex hull
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:,0], points[:,1], points[:,2], 'o')
ax.plot_trisurf(hull.points[:,0], hull.points[:,1], hull.points[:,2], triangles=hull.simplices, shade=True, color='g', alpha=0.5)
plt.show()
