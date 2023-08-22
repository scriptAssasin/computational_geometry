from geometrical_search.common.Rectangle import Rectangle
from geometrical_search.common.KDTree import TreeNode

def two_dimensional_geometrical_kd_tree_search(node: TreeNode, region: Rectangle):
    """
    Searches the KD-tree for points within a specified region.
    """
    results = []
    _search_recursive(node, region, results)
    return results

def _search_recursive(node: TreeNode, region: Rectangle, results: list):
    """
    Recursive function to search the KD-tree.
    """
    if node is None:
        return

    if node.point:
        if region.contains_point(node.point):
            results.append(node.point)
        return

    if region.intersects_split_line(node.split_line):
        _search_recursive(node.left, region, results)
        _search_recursive(node.right, region, results)
    elif node.split_line[0] == "vertical":
        if region.top_right[0] < node.split_line[1]:
            _search_recursive(node.left, region, results)
        else:
            _search_recursive(node.right, region, results)
    else:
        if region.top_right[1] < node.split_line[1]:
            _search_recursive(node.left, region, results)
        else:
            _search_recursive(node.right, region, results)
