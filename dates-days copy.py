from datetime import datetime

current_date = datetime.today()
def get_days_from_today(date):
     formated_date = datetime.strptime(date, "%Y-%m-%d")
     difference = formated_date -current_date
     return difference.days
print(get_days_from_today('2025-06-29'))