from enum import Enum
import matplotlib.pyplot as plt
from convex_hull.algorithms.incremental_algorithm import incremental_algorithm
from convex_hull.algorithms.gift_wrapping_algorithm import gift_wrapping_algorithm
from convex_hull.algorithms.divide_and_conquer_algorithm import divide_and_conquer_algorithm
from convex_hull.algorithms.quick_hull_algorithm import quick_hull_algorithm

class ConvexHullAlgorithms(Enum):
    INCREMENTAL_ALGORITHM = 1
    GIFT_WRAPPING = 2
    DIVIDE_AND_CONQUER = 3
    QUICKHULL = 4

class ConvexHull:
    def __init__(self) -> None:
        self.algorithm = None
        self.result = []
        
    def set_algorithm(self, algorithm: ConvexHullAlgorithms) -> 'ConvexHull':
        if algorithm == ConvexHullAlgorithms.INCREMENTAL_ALGORITHM:
            self.algorithm = incremental_algorithm
        elif algorithm == ConvexHullAlgorithms.GIFT_WRAPPING:
            self.algorithm = gift_wrapping_algorithm
        elif algorithm == ConvexHullAlgorithms.DIVIDE_AND_CONQUER:
            self.algorithm = divide_and_conquer_algorithm
        elif algorithm == ConvexHullAlgorithms.QUICKHULL:
            self.algorithm = quick_hull_algorithm
        else:
            raise ValueError("Invalid algorithm specified. Please choose 'ConvexHullAlgorithms.INCREMENTAL_ALGORITHM', 'ConvexHullAlgorithms.GIFT_WRAPPING', or 'ConvexHullAlgorithms.DIVIDE_AND_CONQUER', or 'ConvexHullAlgorithms.QUICKHULL'")
        return self
        
    def compute(self, points) -> 'ConvexHull':
        self.result = self.algorithm(points)
        return self

    def print_as_list(self) -> 'ConvexHull':
        print(self.result)
        return self
    
    def plot_diagram(self) -> 'ConvexHull':
        x_values, y_values = zip(*self.result)
        x_values += (x_values[0],)
        y_values += (y_values[0],)

        plt.figure(figsize=(6, 6))
        plt.plot(x_values, y_values, marker='o', linestyle='-')
        plt.title('Convex Hull Diagram')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
        plt.show()
        
        return self