def divide_and_conquer_algorithm(points):
    # Base case: If there are 3 or fewer points, return the points as the convex hull
    if len(points) <= 3:
        return points

    # Step [B.1]: Sort points by their x-coordinate
    points.sort(key=lambda p: (p[0], p[1]))

    # Step [B.2]: Divide the points into two subsets A and B
    mid = len(points) // 2
    A = points[:mid]
    B = points[mid:]

    # Step [B.3]: Recursively compute the convex hulls of A and B
    convex_hull_A = divide_and_conquer_algorithm(A)
    convex_hull_B = divide_and_conquer_algorithm(B)

    # Step [B.4]: Merge the convex hulls of A and B
    return merge_convex_hulls(convex_hull_A, convex_hull_B)


def merge_convex_hulls(A, B):
    # Find the upper bridge of the two convex hulls A and B
    upper_bridge = find_upper_bridge(A, B)

    # Find the indices of the upper bridge points in the convex hulls A and B
    i = A.index(upper_bridge[0])
    j = B.index(upper_bridge[1])

    # Merge the convex hulls using the upper bridge
    convex_hull = A[:i + 1] + B[j:] + B[:j + 1] + A[i + 1:]

    return convex_hull


def find_upper_bridge(A, B):
    # Initialize leftmost point of A and rightmost point of B
    i = 0
    j = len(B) - 1

    while True:
        # Check if the line connecting Ai and Ai+1 separates points of A and B
        if not is_separating_line(A[i], A[(i + 1) % len(A)], B[j]):
            i = (i + 1) % len(A)

        # Check if the line connecting Bj and Bj-1 separates points of A and B
        elif not is_separating_line(B[j], B[(j - 1) % len(B)], A[i]):
            j = (j - 1) % len(B)

        # If neither of the above conditions is met, then we found the upper bridge
        else:
            return A[i], B[j]


def is_separating_line(p, q, r):
    # Function to check if the line connecting p and q separates point r from a set of points
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0]) >= 0
