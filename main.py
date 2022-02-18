import json
from datetime import date, timedelta
from typing import Tuple

from classes.calendar_class import CalendarClass
from classes.date_class import DateClass


def get_user_input() -> Tuple[date, int]:
    start_day = int(input("START_DAY: "))
    start_month = int(input("START_MONTH: "))
    start_year = int(input("START_YEAR: "))
    end_day = int(input("END_DAY: "))
    end_month = int(input("END_MONTH: "))
    end_year = int(input("END_YEAR: "))

    START_DATE = date(start_year, start_month, start_day)
    END_DATE = date(end_year, end_month, end_day)
    DATES_COUNT = (END_DATE - START_DATE).days

    return START_DATE, DATES_COUNT


def write_to_json(calendar: CalendarClass) -> None:
    with open("output.json", "w") as file:
        for date_instance in calendar.dates:
            item = date_instance.generate_dict()
            line = json.dumps(item)
            file.write(line + "\n")


def main():
    START_DATE, DATES_COUNT = get_user_input()
    current_date = START_DATE
    calendar = CalendarClass()
    for _ in range(DATES_COUNT):
        date_inst = DateClass(current_date)
        calendar.assign_counters(date_inst)
        calendar.increase_counters(current_date=date_inst)
        calendar.dates.append(date_inst)
        current_date += timedelta(days=1)
    write_to_json(calendar)


if __name__ == "__main__":
    main()
