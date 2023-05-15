

def check_if_is_victory(coord_dict):
    for key, values in coord_dict.items():
        if values == 3:
            return True
    return False