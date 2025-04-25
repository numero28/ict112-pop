# A simple menses calculator
import datetime
from datetime import timedelta

print("""
MENSES CALCULATOR
=================
""")

try:
    print("Enter last menses date details")
    day = int(input("Enter day:(1 - 30) "))
    month = int(input("Enter month:(1 - 12)"))
    year = int(input("Enter year: (eg. 2025)"))

    last_menstrual_period = datetime.date(year, month, day)
    cycle_length = int(input("Enter cycle length: "))
    duration = int(input("Enter duration: "))    
    next_period = last_menstrual_period + timedelta(days=cycle_length - 1)
    end_date = next_period + timedelta(days=duration - 1)
    ovulation_day  = last_menstrual_period + timedelta(days=(cycle_length / 2))
    fertile_window_begin = ovulation_day - timedelta(days=4)
    fertile_window_end = ovulation_day + timedelta(days=1)

    print()
    print(f"Last menses date:\n\t{last_menstrual_period}")    
    print(f"Next period date:\n\t{next_period}")
    print(f"End date:\n\t{end_date}")
    print(f"Ovulation date:\n\t{ovulation_day}")
    print(f"Fertile window:\n\t{fertile_window_begin} to {fertile_window_end}")
    print(f"Safe periods:\n\t{last_menstrual_period + timedelta(days=duration+1)} to \
{fertile_window_begin - timedelta(days=1)} and \n\t{fertile_window_end + timedelta(days=1)} to \
{next_period - timedelta(days=1)}")
except ValueError:
    print("Enter correct integer values")
