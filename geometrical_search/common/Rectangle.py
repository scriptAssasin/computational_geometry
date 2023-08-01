class Rectangle:
    def __init__(self, bottom_left, top_right):
        """
        Initializes a rectangle.

        :param bottom_left: Bottom left corner coordinates (x, y).
        :param top_right: Top right corner coordinates (x, y).
        """
        self.bottom_left = bottom_left
        self.top_right = top_right

    def contains_point(self, point):
        """
        Checks if the rectangle contains a given point.

        :param point: Point to check.
        :return: True if the rectangle contains the point, False otherwise.
        """
        x, y = point
        return (self.bottom_left[0] <= x <= self.top_right[0] and 
                self.bottom_left[1] <= y <= self.top_right[1])

    def intersects_split_line(self, split_line):
        """
        Checks if the rectangle intersects a given split line.

        :param split_line: Splitting line defined by its orientation ("vertical" or "horizontal") and position.
        :return: True if the rectangle intersects the split line, False otherwise.
        """
        if split_line[0] == "vertical":
            return self.bottom_left[0] <= split_line[1] <= self.top_right[0]
        else:
            return self.bottom_left[1] <= split_line[1] <= self.top_right[1]