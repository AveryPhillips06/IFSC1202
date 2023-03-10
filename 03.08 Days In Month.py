
def getDaysInMonth(month, year):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 and month > 12:
        return -1
    if LeapYear(year):
        if month == 2:
            return 29
        else:
            return 28
    return month_days[month-1]

