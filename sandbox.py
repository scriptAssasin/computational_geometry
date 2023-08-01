class Node:
    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right
        self.axis = None

def build_kd_tree(points, depth=0):
    if not points:
        return None

    k = len(points[0])  # διάσταση του χώρου
    axis = depth % k

    points.sort(key=lambda x: x[axis])
    median = len(points) // 2

    node = Node(points[median])
    node.axis = axis
    node.left = build_kd_tree(points[:median], depth + 1)
    node.right = build_kd_tree(points[median + 1:], depth + 1)

    return node

def range_search(node, rect, results):
    if not node:
        return

    x, y = node.point

    if rect["xmin"] <= x <= rect["xmax"] and rect["ymin"] <= y <= rect["ymax"]:
        results.append((x, y))

    if node.axis == 0:
        if rect["xmin"] <= x:
            range_search(node.left, rect, results)
        if rect["xmax"] >= x:
            range_search(node.right, rect, results)
    else:
        if rect["ymin"] <= y:
            range_search(node.left, rect, results)
        if rect["ymax"] >= y:
            range_search(node.right, rect, results)

points = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)]
root = build_kd_tree(points)

# Ένα παράδειγμα αναζήτησης για όλα τα σημεία μέσα στο ορθογώνιο με xmin=3, xmax=9, ymin=1, ymax=7
rect = {"xmin": 3, "xmax": 9, "ymin": 1, "ymax": 7}
results = []
range_search(root, rect, results)
print(results)
