from geometrical_search.common.Rectangle import Rectangle
from geometrical_search.common.KDTree import KDTree
from geometrical_search.algorithms.two_dimensional_geometrical_kd_tee_search_algorithm import two_dimensional_geometrical_kd_tree_search

if __name__ == "__main__":
    points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
    tree = KDTree(points)  # Construct the KDTree with the given points
    tree_root_node = tree.get_root_node()
    
    search_region = Rectangle((1, 1), (7, 5))
    results = two_dimensional_geometrical_kd_tree_search(tree_root_node, search_region)  # The search function returns results directly

    print(f"Points in the region {search_region.bottom_left} to {search_region.top_right}: {results}")
