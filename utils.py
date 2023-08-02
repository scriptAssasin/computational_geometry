from typing import List, Tuple
import random

def generate_random_points(num_points, min_value=0, max_value=10) -> List[Tuple[float, float]]:
    points = []
    for _ in range(num_points):
        x = round(random.uniform(min_value, max_value), 0)
        y = round(random.uniform(min_value, max_value), 0)
        points.append((x, y))
    return points

def print_algorithm_time_table(times_object) -> None:   
    # Determine the maximum length of the algorithm name
    max_length = max([len(name) for name in times_object.keys()])

    # Add some padding (e.g., 5 spaces)
    standard_length = max_length + 5

    # Display the table
    header = "| {:<{width}} | {:<20} |".format("Algorithm", "Time Taken (seconds)", width=standard_length)
    separator = "+" + "-"*(standard_length+2) + "+" + "-"*22 + "+"

    print(separator)
    print(header)
    print(separator)

    for algorithm, time_taken in times_object.items():
        row = "| {:<{width}} | {:<20.2f} |".format(algorithm, time_taken, width=standard_length)
        print(row)
        print(separator)
