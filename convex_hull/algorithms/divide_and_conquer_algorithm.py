# stores the centre of polygon (It is made global because it is used in compare function)
mid = [0, 0]

def sort_key(point):
    p = [point[0]-mid[0], point[1]-mid[1]]
    q = [0, 0]  # Reference direction, typically (1,0)
    
    one = quadrant(p)
    two = quadrant(q)

    if one != two:
        return (one, p[1]*q[0] - q[1]*p[0])
    return (one, -p[1]*q[0] + q[1]*p[0])
 
# determines the quadrant of a point (used in compare())
def quadrant(point):
    """Return the quadrant of the given point."""
    x, y = point
    if x >= 0 and y >= 0: return 1
    if x <= 0 and y >= 0: return 2
    if x <= 0 and y <= 0: return 3
    return 4
 
# Checks whether the line is crossing the polygon
def orientation(a, b, c):
    res = (b[1]-a[1]) * (c[0]-b[0]) - (c[1]-b[1]) * (b[0]-a[0])
    if res == 0:
        return 0
    if res > 0:
        return 1
    return -1
 
# compare function for sorting
def compare(p1, q1):
    p = [p1[0]-mid[0], p1[1]-mid[1]]
    q = [q1[0]-mid[0], q1[1]-mid[1]]
    
    one, two = quadrant(p), quadrant(q)

    if one != two:
            return -1 if one < two else 1
    return -1 if p[1]*q[0] < q[1]*p[0] else 1
 

def merge_hulls(polygon_a, polygon_b):
    num_points_a = len(polygon_a)
    num_points_b = len(polygon_b)
    
    rightmost_point_a = 0
    leftmost_point_b = 0

    # Find the rightmost point of polygon_a
    for i in range(1, num_points_a):
        if polygon_a[i][0] > polygon_a[rightmost_point_a][0]:
            rightmost_point_a = i

    # Find the leftmost point of polygon_b
    for i in range(1, num_points_b):
        if polygon_b[i][0] < polygon_b[leftmost_point_b][0]:
            leftmost_point_b = i

    # Find the upper bridge
    current_point_a, current_point_b = rightmost_point_a, leftmost_point_b
    finding_upper_bridge = True
    while finding_upper_bridge:
        finding_upper_bridge = False
        while orientation(polygon_b[current_point_b], polygon_a[current_point_a], polygon_a[(current_point_a+1) % num_points_a]) >= 0:
            current_point_a = (current_point_a + 1) % num_points_a

        while orientation(polygon_a[current_point_a], polygon_b[current_point_b], polygon_b[(num_points_b+current_point_b-1) % num_points_b]) <= 0:
            current_point_b = (current_point_b - 1) % num_points_b
            finding_upper_bridge = True

    upper_bridge_point_a, upper_bridge_point_b = current_point_a, current_point_b
    current_point_a, current_point_b = rightmost_point_a, leftmost_point_b

    # Find the lower bridge
    finding_lower_bridge = True
    while finding_lower_bridge:
        finding_lower_bridge = False
        while orientation(polygon_a[current_point_a], polygon_b[current_point_b], polygon_b[(current_point_b+1) % num_points_b]) >= 0:
            current_point_b = (current_point_b + 1) % num_points_b

        while orientation(polygon_b[current_point_b], polygon_a[current_point_a], polygon_a[(num_points_a+current_point_a-1) % num_points_a]) <= 0:
            current_point_a = (current_point_a - 1) % num_points_a
            finding_lower_bridge = True

    lower_bridge_point_a, lower_bridge_point_b = current_point_a, current_point_b

    # Construct the merged convex hull
    merged_hull = []
    current_index = upper_bridge_point_a
    merged_hull.append(polygon_a[upper_bridge_point_a])
    while current_index != lower_bridge_point_a:
        current_index = (current_index + 1) % num_points_a
        merged_hull.append(polygon_a[current_index])

    current_index = lower_bridge_point_b
    merged_hull.append(polygon_b[lower_bridge_point_b])
    while current_index != upper_bridge_point_b:
        current_index = (current_index + 1) % num_points_b
        merged_hull.append(polygon_b[current_index])

    return merged_hull
 
# Brute force algorithm to find convex hull for a set of less than 6 points
def smallset_convex_hull(points):
    hull_points = set()

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            x1, x2 = points[i][0], points[j][0]
            y1, y2 = points[i][1], points[j][1]
            a, b, c = y1-y2, x2-x1, x1*y2-y1*x2

            pos, neg = 0, 0
            for k in range(len(points)):
                if (k == i) or (k == j) or (a*points[k][0] + b*points[k][1] + c <= 0):
                    neg += 1
                if (k == i) or (k == j) or (a*points[k][0] + b*points[k][1] + c >= 0):
                    pos += 1

            if pos == len(points) or neg == len(points):
                hull_points.add(tuple(points[i]))
                hull_points.add(tuple(points[j]))

    # Convert set to list
    hull_list = list(map(list, hull_points))

    # Compute centroid of the hull points for sorting in anti-clockwise order
    global mid
    mid = [sum(point[0] for point in hull_list) / len(hull_list),
           sum(point[1] for point in hull_list) / len(hull_list)]

    # Sort points in anti-clockwise order using the computed centroid 'mid'
    hull_list.sort(key=sort_key)

    return hull_list

def divide_and_conquer_algorithm(points):
    # If the number of points is less than 6 then the
    # function uses the brute algorithm to find the
    # convex hull
    if len(points) <= 5:
        return smallset_convex_hull(points)
 
    # left contains the left half points
    # right contains the right half points
    left, right = [], []
    start = int(len(points)/2)
    for i in range(start):
        left.append(points[i])
    for i in range(start, len(points)):
        right.append(points[i])
 
    # convex hull for the left and right sets
    left_hull = divide_and_conquer_algorithm(left)
    right_hull = divide_and_conquer_algorithm(right)
 
    # merging the convex hulls
    return merge_hulls(left_hull, right_hull)