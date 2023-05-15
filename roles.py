
import random
import config

def make_user_and_program_roles():
    roles = [config.NAME_NAUGHTS, config.NAME_CROSSES]
    user_r, program_r = random.sample(roles, 2)
    return user_r, program_r