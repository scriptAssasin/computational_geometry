from enum import Enum

class GeometricalSearchAlgorithms(Enum):
    ALGORITHM_1 = 1

class GeometricalSearch:
    def __init__(self) -> None:
        self.algorithm = None
        
    def set_algorithm(self, algorithm: GeometricalSearchAlgorithms):
        return self
    
    def compute(self, points):
        return self
    
    