import random

def make_player_point_if_user(Player, list_of_points):
    player_point = Point(0,0)
    while player_point not in list_of_points:
        player_point = make_user_point(Player)
    return player_point


def make_player_point_if_program(list_of_points):
    return random.choice(list_of_points)


def func_for_point_dict_and_list(Player: Player, coord_dict, list_of_points, who_plays):
# заполнение клетки игроком (пользователем)
    if (who_plays == config.NAME_USER):
        player_point = make_player_point_if_user(Player, list_of_points)
    else:
        player_point = make_player_point_if_program(list_of_points)
# дбавляем координату пользователя в его экземпляр
    Player.add_point(player_point)       
    Player.show_player()        
#подсчёт заполненных пользователем координат
    coord_dict = count_point_dictionary(coord_dict, player_point)

    list_of_points = make_list_of_available_points(list_of_points, player_point)
    return coord_dict, list_of_points