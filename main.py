__author__ = 'DIANA'

import random

from class_description import Point, Player
import config
from count_points import count_point_dictionary, make_coord_dict
from lists_from_cycle import func_for_point_dict_and_list
from list_of_all_points import make_list_of_available_points, make_list_of_all_points, show_list_of_points
from roles import make_user_and_program_roles
from user import make_user_point
from victory import check_if_is_victory






if __name__ == "__main__":
    print(config.HELLO_MESSAGE)

# рандомно определяем, кто за крестики, кто за нолики
    user_role, program_role = make_user_and_program_roles()
# создаём экземпляры для
    User = Player(user_role)
    Program = Player(program_role)

    print("user_role = ", User.role)
    print("program_role = ", Program.role)

# формируем список всех точек игрового поля
    list_of_points = make_list_of_all_points()
    show_list_of_points(list_of_points)

    crosses_coord_dict = make_coord_dict()
    naughts_coord_dict = make_coord_dict()

    who_plays_first = config.NAME_USER if User.role == config.NAME_CROSSES else config.NAME_PROGRAM
    Player1 = User if User.role == config.NAME_CROSSES else Program

    who_plays_second = config.NAME_PROGRAM if User.role == config.NAME_CROSSES else config.NAME_USER
    Player2 = User if User.role == config.NAME_CROSSES else Program

    while len(list_of_points) > 0:
        crosses_coord_dict, list_of_points = func_for_point_dict_and_list(Player1, crosses_coord_dict, list_of_points, who_plays_first)

        if check_if_is_victory(crosses_coord_dict):
            print(config.CROSSES_WIN)
            break
        elif len(list_of_points)==0:
            print(config.DRAW_WIN)
            break

        naughts_coord_dict, list_of_points = func_for_point_dict_and_list(Player2, naughts_coord_dict, list_of_points, who_plays_second)

        if check_if_is_victory(naughts_coord_dict):
            print(config.NAUGHTS_WIN)
            break

        
# показываем оставшиеся пустые клетки
        show_list_of_points(list_of_points)

