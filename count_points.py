
def make_coord_dict():
    return {"x=1": 0, "x=2": 0, "x=3": 0, "y=1": 0, "y=2": 0, "y=3": 0, "x=y": 0, "x+y=4": 0}

def increase_points(coord, num):
    return 1 if coord == num else 0


def count_point_dictionary(coord_dictionary, point):
    coord_dict = coord_dictionary
    coord_dict["x=1"] += increase_points(point.x, 1)
    coord_dict["y=1"] += increase_points(point.y, 1)
    coord_dict["x=2"] += increase_points(point.x, 2)
    coord_dict["y=2"] += increase_points(point.y, 2)
    coord_dict["x=3"] += increase_points(point.x, 3)
    coord_dict["y=3"] += increase_points(point.y, 3)
    coord_dict["x=y"] += 1 if (point.x == point.y) else 0
    coord_dict["x+y=4"] += 1 if (point.x + point.y == 4) else 0
    return coord_dict
