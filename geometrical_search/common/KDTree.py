class TreeNode:
    def __init__(self, split_line=None, point=None, left=None, right=None):
        self.split_line = split_line  # Splitting line: either vertical or horizontal
        self.point = point  # Data point for this node
        self.left = left  # Left child node
        self.right = right  # Right child node

class KDTree:
    def __init__(self, points):
        self.root = self._build_kd_tree(points)

    def get_root_node(self):
        return self.root
    
    def _build_kd_tree(self, points, depth=0):
        """
        Builds a KD-tree from the given points.
        """
        # If there's only one point
        if len(points) == 1:
            return TreeNode(point=points[0])

        median = len(points) // 2

        # If the depth is even
        if depth % 2 == 0:
            sorted_points = sorted(points, key=lambda point: point[0])  # Sort by x-coordinate
            split_line = ("vertical", sorted_points[median][0])  # Vertical splitting line
        # If the depth is odd
        else:
            sorted_points = sorted(points, key=lambda point: point[1])  # Sort by y-coordinate
            split_line = ("horizontal", sorted_points[median][1])  # Horizontal splitting line

        P1 = sorted_points[:median]
        P2 = sorted_points[median:]

        left_child = self._build_kd_tree(P1, depth + 1)
        right_child = self._build_kd_tree(P2, depth + 1)

        return TreeNode(split_line=split_line, left=left_child, right=right_child)
