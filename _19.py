import datetime

begin = datetime.date(1901, 1, 1)
current_date = begin
end = datetime.date(2000, 12, 31)

one_day = datetime.timedelta(days=1)

total_sundays_first = 0

def is_sunday_first(date):
    return date.weekday() == 6 and date.day == 1

for n in range((end-begin).days):
    if is_sunday_first(current_date):
        total_sundays_first += 1
    current_date += one_day

print(total_sundays_first)
