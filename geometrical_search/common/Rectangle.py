class Rectangle:
    def __init__(self, bottom_left, top_right):
        """
        Initializes a rectangle.
        """
        self.bottom_left = bottom_left
        self.top_right = top_right

    def contains_point(self, point):
        """
        Checks if the rectangle contains a given point.
        """
        x, y = point
        return (self.bottom_left[0] <= x <= self.top_right[0] and 
                self.bottom_left[1] <= y <= self.top_right[1])

    def intersects_split_line(self, split_line):
        """
        Checks if the rectangle intersects a given split line.
        """
        if split_line[0] == "vertical":
            return self.bottom_left[0] <= split_line[1] <= self.top_right[0]
        else:
            return self.bottom_left[1] <= split_line[1] <= self.top_right[1]