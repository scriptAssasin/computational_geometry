import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

def quick_hull_algorithm(points):
    hull = ConvexHull(points)
    
    if len(points[0]) == 2:  # If the input points are 2D
        return np.array(points)[hull.vertices].tolist()
    elif len(points[0]) == 3:  # If the input points are 3D
        hull_triangles = [hull.points[simplex] for simplex in hull.simplices]
        
        # Plot the convex hull
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(points[:,0], points[:,1], points[:,2], 'o')
        ax.plot_trisurf(hull.points[:,0], hull.points[:,1], hull.points[:,2], triangles=hull.simplices, shade=True, color='g', alpha=0.5)
        plt.show()

        return hull_triangles
    else:
        raise ValueError("The provided points should be either 2D or 3D.")
