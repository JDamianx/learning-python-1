def is_year_leap(year):
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False
    # return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    # different version without if conditions(one line)

months_30_days=[month for month in range(2,7,2)if month!=2]+[month for month in range(9,12,2)]
# We can simplify these lists, but I chose to use list comprehension.
def days_in_month(year,month):
    if not(1<=month<=12):
        return -1
    # checks if month is valid
    if month==2:
        if is_year_leap(year)==True:
            return 29
        else:
            return 28
    if month in months_30_days:
        return 30
    else:
        return 31
# ********************************************************************************
# NEW FUNCTION/NEXT FEATURE
def day_of_year(year, month, day):
    # validation
    if not (1<=month<=12):
        raise ValueError("Invalid month")
    max_day = days_in_month(year,month)
    if not (1<=day<=max_day):
        raise ValueError("Invalid day for this month")
    day_counter=0
    for m in range(1, month):
        day_counter+=days_in_month(year,m)
    return day_counter + day
            
    
    
print(day_of_year(2025, 8, 28))
# *********************************************************************************