from datetime import date
from typing import Tuple


def get_user_input() -> Tuple[date, int]:
    start_day = int(input("START_DAY: "))
    start_month = int(input("START_MONTH: "))
    start_year = int(input("START_YEAR: "))
    START_DATE = convert_user_input(start_year, start_month, start_day)

    end_day = int(input("END_DAY: "))
    end_month = int(input("END_MONTH: "))
    end_year = int(input("END_YEAR: "))
    END_DATE = convert_user_input(end_year, end_month, end_day)
    DATES_COUNT = (END_DATE - START_DATE).days

    return START_DATE, DATES_COUNT


def convert_user_input(*args):
    try:
        DATE = date(*args)
        return DATE
    except ValueError:
        print("Invalid date")
        exit(-1)
