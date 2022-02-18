import calendar
from datetime import date, timedelta
from math import ceil


class DateClass:
    def __init__(self, the_date):
        self.date_key = int(the_date.strftime("%Y%m%d"))
        self.full_date = the_date.strftime("%x")
        self.day = the_date.day
        self.day_of_week = the_date.isoweekday()
        self.day_of_year = int(the_date.strftime("%j"))
        self.day_num_overall = 0
        self.day_name = the_date.strftime("%A")
        self.day_abbrev = the_date.strftime("%a")
        self.weekday_flag = "N" if the_date.isoweekday() > 5 else "Y"
        self.week_num_in_year = int(the_date.strftime("%W"))
        self.week_num_overall = 0
        self.week_begin_date = self.get_week_begin_datetime(the_date).strftime("%x")
        self.week_begin_date_key = int(
            self.get_week_begin_datetime(the_date).strftime("%Y%m%d")
        )
        self.month = the_date.month
        self.month_num_overall = 0
        self.month_name = the_date.strftime("%B")
        self.month_abbrev = the_date.strftime("%b")
        self.quarter = ceil(the_date.month / 3)
        self.year = the_date.year
        self.year_num_overall = 0
        self.yearmonth = int(the_date.strftime("%Y%m"))
        self.fiscal_month = (the_date.month + 5) % 12 + 1
        self.fiscal_quarter = (self.quarter + 1) % 4 + 1
        self.fiscal_year = self.year if self.month < 7 else self.year + 1
        self.month_end_flag = self.get_monthend_flag()

    def get_week_begin_datetime(self, the_date: date) -> date:
        return the_date - timedelta(days=self.day_of_week - 1)

    def get_monthend_flag(self) -> str:
        last_date = calendar.monthrange(self.year, self.month)[1]
        return "Month End" if self.day == last_date else "Not Month End"

    def generate_dict(self) -> dict:
        return vars(self)
