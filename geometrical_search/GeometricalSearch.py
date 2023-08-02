from typing import List, Tuple
from enum import Enum
from geometrical_search.common.Rectangle import Rectangle
from geometrical_search.common.KDTree import KDTree
from geometrical_search.algorithms.two_dimensional_geometrical_kd_tee_search_algorithm import two_dimensional_geometrical_kd_tree_search

class GeometricalSearchAlgorithms(Enum):
    KD_TREE_2D = 1

class GeometricalSearch:
    def __init__(self) -> None:
        self.algorithm = None
        self.points = None

    def set_algorithm(self, algorithm: GeometricalSearchAlgorithms) -> 'GeometricalSearch':
        if algorithm == GeometricalSearchAlgorithms.KD_TREE_2D:
            self.algorithm = algorithm
        else:
            raise ValueError("Invalid algorithm specified. Please choose 'GeometricalSearchAlgorithms.KD_TREE_2D'")
        return self

    def compute(self, points, search_region: Rectangle) -> List[Tuple[float, float]]:
        self.points = points
        
        if self.algorithm == GeometricalSearchAlgorithms.KD_TREE_2D:
            tree = KDTree(self.points)
            tree_root_node = tree.get_root_node()
            results = two_dimensional_geometrical_kd_tree_search(tree_root_node, search_region)
            return results

        return []