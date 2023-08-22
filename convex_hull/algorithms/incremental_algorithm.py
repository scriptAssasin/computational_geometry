import matplotlib.pyplot as plt

def incremental_algorithm(points: list, visualize: bool):
    def plot_step(points, hull, title="", show_step = True):
        if(visualize):
            plt.scatter([p[0] for p in points], [p[1] for p in points], color='blue')
            hull.append(hull[0])  # Close the hull visually
            plt.plot([p[0] for p in hull], [p[1] for p in hull], 'r-')
            plt.title(title)
            plt.show()
            hull.pop()  # Remove the added point to keep the hull open

    # Step 1: Sort points in lexicographic order
    sorted_points = sorted(points)

    # Step 2: Create an upper hull list L_upper containing the first two points
    L_upper = [sorted_points[0], sorted_points[1]]
    plot_step(sorted_points, L_upper, "Initial Upper Hull")

    # Step 3: Iterate through the sorted points, starting from the third point
    for i in range(2, len(sorted_points)):
        L_upper.append(sorted_points[i])
        plot_step(sorted_points, L_upper, "Upper Hull after adding point")

        # Step 4: Check if the last three points in L_upper form a right turn
        while len(L_upper) >= 3 and not is_right_turn(L_upper[-3:]):
            # If they do not form a right turn, remove the middle point
            L_upper.pop(-2)
            plot_step(sorted_points, L_upper, "Upper Hull after potential right turn check")

    # Step 5: Create a lower hull list L_lower containing the last two points
    L_lower = [sorted_points[-1], sorted_points[-2]]
    plot_step(sorted_points, L_lower, "Initial Lower Hull")

    # Step 6: Iterate through the sorted points in reverse order, starting from the second-to-last point
    for i in range(len(sorted_points) - 3, -1, -1):
        L_lower.append(sorted_points[i])
        plot_step(sorted_points, L_lower, "Lower Hull after adding point")

        # Step 7: Check if the last three points in L_lower form a right turn
        while len(L_lower) >= 3 and not is_right_turn(L_lower[-3:]):
            # If they do not form a right turn, remove the middle point
            L_lower.pop(-2)
            plot_step(sorted_points, L_lower, "Lower Hull after potential right turn check")

    # Step 8: Combine the upper and lower hulls to get the final convex hull
    convex_hull = L_upper + L_lower[1:-1]
    plot_step(sorted_points, convex_hull, "Final Convex Hull")

    return convex_hull


def is_right_turn(points: list):
    x1, y1 = points[-3]
    x2, y2 = points[-2]
    x3, y3 = points[-1]
    # Check if the points form a right turn
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1) < 0
