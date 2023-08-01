def incremental_algorithm(points: list):
    # Step 1: Sort points in lexicographic order
    sorted_points = sorted(points)

    # Step 2: Create an upper hull list L_upper containing the first two points
    L_upper = [sorted_points[0], sorted_points[1]]

    # Step 3: Iterate through the sorted points, starting from the third point
    for i in range(2, len(sorted_points)):
        L_upper.append(sorted_points[i])
        # Step 4: Check if the last three points in L_upper form a right turn
        while len(L_upper) >= 3 and not is_right_turn(L_upper[-3:]):
            # If they do not form a right turn, remove the middle point
            L_upper.pop(-2)

    # Step 5: Create a lower hull list L_lower containing the last two points
    L_lower = [sorted_points[-1], sorted_points[-2]]

    # Step 6: Iterate through the sorted points in reverse order, starting from the second-to-last point
    for i in range(len(sorted_points) - 3, -1, -1):
        L_lower.append(sorted_points[i])
        # Step 7: Check if the last three points in L_lower form a right turn
        while len(L_lower) >= 3 and not is_right_turn(L_lower[-3:]):
            # If they do not form a right turn, remove the middle point
            L_lower.pop(-2)

    # Step 8: Combine the upper and lower hulls to get the final convex hull
    convex_hull = L_upper + L_lower[1:-1]
    return convex_hull


def is_right_turn(points: list):
    x1, y1 = points[-3]
    x2, y2 = points[-2]
    x3, y3 = points[-1]
    # Check if the points form a right turn
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1) < 0
