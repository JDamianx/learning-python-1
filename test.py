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
# months_31_days=[month for month in range(1,8,2)]+[month for month in range(8,13,2)] not in use
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

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 12]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end=" ")
    result = days_in_month(yr, mo)
    if result==-1:
        print("Błędny numer miesiąca")
        continue
    if result == test_results[i]:
        print(f"OK {result}")
    else:
        print(f"Failed {result}")
    
