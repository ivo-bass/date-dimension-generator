from typing import List

from classes.date_class import DateClass


class CalendarClass:
    def __init__(self) -> None:
        self.dates: List[DateClass] = []
        self.day_counter: int = 1
        self.week_counter: int = 1
        self.month_counter: int = 1
        self.year_counter: int = 1

    def increase_counters(self, current_date: DateClass) -> None:
        self.day_counter += 1
        if current_date.day_of_week == 7:
            self.week_counter += 1
        if current_date.month_end_flag == "Month End":
            self.month_counter += 1
        if current_date.day_of_year == 1 and current_date.day_num_overall > 1:
            self.year_counter += 1

    def assign_counters(self, date_instance: DateClass) -> None:
        date_instance.day_num_overall = self.day_counter
        date_instance.week_num_overall = self.week_counter
        date_instance.month_num_overall = self.month_counter
        date_instance.year_num_overall = self.year_counter
