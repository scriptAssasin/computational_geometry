def gift_wrapping_algorithm(points):
    n = len(points)
    if n < 3:
        return points  # Convex hull is the same as the input points

    # Find the leftmost point
    leftmost = min(points, key=lambda p: (p[0], p[1]))

    hull = []
    p = leftmost
    q = None
    while True:
        hull.append(p)
        q = points[0]
        for r in points[1:]:
            if r == p:
                continue
            if q == p or orientation(p, q, r) == 2:  # r is more counterclockwise than current q
                q = r
        p = q
        if p == leftmost:
            break

    return hull

def orientation(p, q, r):
    # Function to determine the orientation of three points (p, q, r)
    # Returns 0 if p, q, r are collinear, 1 if clockwise, and 2 if counterclockwise
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2
