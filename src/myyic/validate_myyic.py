import datetime
from .constants import CODE_STATE


def remove_dash(input_string):
    """ Remove '-' If Any """
    return input_string.replace("-", "").strip()


def check_birth_date(date: str):
    """ Check Birth Date Validity """
    try:
        datetime.datetime.strptime(date, "%y-%m-%d").date()
    except ValueError:
        raise ValueError('Invalid')


def check_birth_place(code):
    """ Check Birthplace Validity """
    match_result = code in CODE_STATE
    if not match_result:
        raise ValueError('Invalid')


def nric(input_string: str):
    """ Check NRIC / MyKad Validity """
    try:
        input_string = remove_dash(input_string)

        if not input_string.isdigit():
            raise ValueError('Invalid Value')

        if len(input_string) != 12:
            raise ValueError('Invalid Value')

        check_birth_date(f'{input_string[0:2]}-{input_string[2:4]}-{input_string[4:6]}')

        check_birth_place(input_string[6:8])

        return True

    except ValueError as error:
        return False
