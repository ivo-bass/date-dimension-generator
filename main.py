from datetime import timedelta

from classes.calendar_class import CalendarClass
from classes.date_class import DateClass
from functions.read import get_user_input
from functions.write import write_to_json


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
