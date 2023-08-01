def quick_hull_algorithm(points):
    def distance_from_line(p, q, r):
        # Function to compute the perpendicular distance from point r to the line passing through points p and q
        return abs((q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0]))

    def is_right_of_line(p, q, r):
        # Function to check if point r is to the right of the directed line passing through points p and q
        return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0]) < 0

    def quick_hull_recursive(A, B, S):
        if len(S) < 3:
            return S

        C = max(S, key=lambda p: distance_from_line(A, B, p))
        M = [p for p in S if is_right_of_line(A, C, p)]
        N = [p for p in S if is_right_of_line(C, B, p)]

        convex_hull_M = quick_hull_recursive(A, C, M)
        convex_hull_N = quick_hull_recursive(C, B, N)

        return convex_hull_M + [C] + convex_hull_N

    n = len(points)
    if n < 3:
        return points  # Convex hull is the same as the input points

    # Find the leftmost and rightmost points
    leftmost = min(points, key=lambda p: (p[0], p[1]))
    rightmost = max(points, key=lambda p: (p[0], p[1]))

    # Divide the points into two sets: S1 contains points to the right of line AB, and S2 contains points to the right of line BA
    S1 = [p for p in points if is_right_of_line(leftmost, rightmost, p)]
    S2 = [p for p in points if is_right_of_line(rightmost, leftmost, p)]

    # Compute the convex hull recursively for S1 and S2
    convex_hull_S1 = quick_hull_recursive(leftmost, rightmost, S1)
    convex_hull_S2 = quick_hull_recursive(rightmost, leftmost, S2)

    # Merge the convex hulls of S1, S2, and the endpoints of the line segment AB
    return convex_hull_S1 + [leftmost] + convex_hull_S2