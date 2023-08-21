def quick_hull_algorithm(points):        

    def _side(p1, p2, p):
        return (p2[0] - p1[0]) * (p[1] - p1[1]) - (p2[1] - p1[1]) * (p[0] - p1[0])
    

    def _distance(p1, p2, p):
        return abs((p2[1] - p1[1]) * p[0] - (p2[0] - p1[0]) * p[1] + p2[0] * p1[1] - p2[1] * p1[0])
    

    def _find_extreme_points(points):

        leftmost = min(points, key=lambda p: p[0])

        rightmost = max(points, key=lambda p: p[0])

        topmost = max(points, key=lambda p: p[1])

        bottommost = min(points, key=lambda p: p[1])

        return leftmost, rightmost, topmost, bottommost
   
    def _quick_hull_recursive(p1, p2, points):

        if not points:
            return []

        # find the point farthest from the line segment p1-p2

        max_dist = -1

        max_point = None

        for p in points:

            d = _distance(p1, p2, p)

            if _side(p1, p2, p) > 0 and d > max_dist:
                max_dist = d
                max_point = p

        # divide the points based on the two segments created by max_point

        s1 = [p for p in points if _side(p1, max_point, p) > 0]
        s2 = [p for p in points if _side(max_point, p2, p) > 0]
        
        return _quick_hull_recursive(p1, max_point, s1) + [max_point] + _quick_hull_recursive(max_point, p2, s2)
    
    n = len(points)

    if n < 3:
        return points
    

    leftmost, rightmost, topmost, bottommost = _find_extreme_points(points)
    upper_hull = _quick_hull_recursive(leftmost, rightmost, [p for p in points if _side(leftmost, rightmost, p) > 0])

    lower_hull = _quick_hull_recursive(rightmost, leftmost, [p for p in points if _side(rightmost, leftmost, p) > 0])

    return [leftmost] + upper_hull + [rightmost] + lower_hull
    return points

