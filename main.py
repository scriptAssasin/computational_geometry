import matplotlib.pyplot as plt
import time
from utils import *
from convex_hull.ConvexHull import ConvexHull, ConvexHullAlgorithms
from geometrical_search.GeometricalSearch import GeometricalSearch, GeometricalSearchAlgorithms
from geometrical_search.common.Rectangle import Rectangle

if __name__ == "__main__":
    random_points = generate_random_points(num_points=100, min_value=0, max_value=1000)
        
    algorithms = [
        ConvexHullAlgorithms.INCREMENTAL_ALGORITHM,
        # ConvexHullAlgorithms.GIFT_WRAPPING,
        # ConvexHullAlgorithms.DIVIDE_AND_CONQUER,
        ConvexHullAlgorithms.QUICKHULL
    ]

    convex_hull_object = ConvexHull()
    times_object = {}

    for algorithm in algorithms:
        start_time = time.time()
        
        convex_hull_object.set_algorithm(algorithm)
        convex_hull_result = convex_hull_object.compute(random_points, False)
        
        convex_hull_object_list_result = convex_hull_result.print_as_list()
        convex_hull_object_diagram_result = convex_hull_result.plot_diagram()
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        # Store the elapsed_time in the times_object dictionary
        times_object[str(algorithm)] = elapsed_time

    # Use the helper function to print the table
    print_algorithm_time_table(times_object)
    
    # Quick Hull 3d
    points = generate_random_3d_points(80)
    convex_hull_object.set_algorithm(ConvexHullAlgorithms.QUICKHULL)
    convex_hull_result = convex_hull_object.compute(points, False)
    
    print(convex_hull_result)

    
    # # Geometrical Search
    # random_70_points = generate_random_points(num_points=70, min_value=0, max_value=100)
    # random_2_points_rectangle = generate_random_points(num_points=2,min_value=1,max_value=99)
    # print(random_70_points)
    # print(random_2_points_rectangle)
    # search_region = Rectangle(random_2_points_rectangle[0], random_2_points_rectangle[1])
    
    # geometrical_search_object = GeometricalSearch()
    # geometrical_search_object.set_algorithm(GeometricalSearchAlgorithms.KD_TREE_2D)
    # results = geometrical_search_object.compute(random_70_points, search_region)

    # print(f"Points in the region {search_region.bottom_left} to {search_region.top_right}: {results}")