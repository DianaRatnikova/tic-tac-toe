from class_description import Point


def show_list_of_points(list_of_points):
    print("\nОставшиеся варианты:")
    for point in list_of_points:
        point.show_point()



def make_list_of_all_points():
    list_of_points = []
    for i in range(1, 4):
        for j  in range(1, 4):
            list_of_points.append(Point(i, j))
    return list_of_points


def make_list_of_available_points(list_of_points, point):
    lp = list_of_points
    if point in lp:
        lp.remove(point)
    return lp