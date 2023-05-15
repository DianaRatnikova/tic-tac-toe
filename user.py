import class_description

def ask_user_point():
    print("Введите координаты свободной клетки!", end='')
    p_x = int(input("\nenter x:  "))
    p_y = int(input("enter y:  "))
    return p_x, p_y


def make_user_point1(User):
    p_x, p_y = ask_user_point()
    return class_description.Point(p_x, p_y)

def make_user_point(User: class_description.Player):
    p_x, p_y = ask_user_point()
    Point = class_description.Point(p_x, p_y)
    if Point in User.list_point:
        print("Вы уже вводили эту точку!")
        return make_user_point(User)
    return class_description.Point(p_x, p_y)