import random
from datetime import datetime, timedelta
from .constants import CODE_STATE, STATE_LIST, STATE_CODE


def generate(separator='-', gender=None, state=None):
    """ Generate Random Valid NRIC """
    birthday = random_birth_date()
    birthplace = random_birth_place(state=state)
    ending_number = random_ending_number(gender=gender)

    return f'{birthday}{separator}{birthplace}{separator}{ending_number}'


def random_birth_date():
    """ Generate Random Birthday """
    end = datetime.now().date()
    start = end - timedelta(days=29220)
    random_date = start + (end - start) * random.random()
    return random_date.strftime("%y%m%d")


def random_birth_place(state=None):
    """ Generate Random Birthplace """
    if state not in STATE_LIST:
        raise ValueError('Invalid Birthplace Shortcode')

    if state:
        return STATE_CODE[str(state)][random.randrange(0, len(STATE_CODE[str(state)]))]

    while True:
        birth_place_code = str(random.randrange(0, 58)).zfill(2)
        if str(birth_place_code) in CODE_STATE:
            break
    return birth_place_code


def random_ending_number(gender=None):
    """ Generate Random Ending Number """
    gender_list = ['F', 'M', None]
    if gender not in gender_list:
        raise ValueError('Invalid Gender')

    if gender == 'F':
        return str(random.randrange(0, 9999, 2)).zfill(4)
    elif gender == 'M':
        return str(random.randrange(0, 9999, 1)).zfill(4)

    return str(random.randrange(0, 9999)).zfill(4)
