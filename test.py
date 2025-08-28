# def f(x):
#     print(x + 1)
#     return x + 2

# y = f(3)
# print(y)
# def greet(name):
#     return "Hello " + name

# print(greet("Alice"))
# print(name)
# def a():
#     print("a start")
#     b()
#     print("a end")

# def b():
#     print("b start")
#     c()
#     print("b end")

# def c():
#     print("c running")

# a()

# numbers=[2,6]
# def average(x):
#     if not x:
#         return None
#     return sum(x)/len(x)
# avrg_numbers=average(numbers)
# print(avrg_numbers)

# def make_score_keeper():
#     score = 0

#     def add(points):
#         # TODO: zwiększ score o points
#         # użyj nonlocal, żeby nie robić nowej zmiennej
#         nonlocal score
#         score+=points
#         return score

#     # return add

#     # def reset_score():
#     #     nonlocal score
#     #     score=0
#     #     return score
# game_score = make_score_keeper()
# print(game_score(10))  # -> 10

# print(game_score(5))   # -> 15
# print(game_score(7))   # -> 22

# def message(what, number):
#     print("Enter", what, "number", number)
 
# message("telephone", 11)
# message("price", 5)
# message(5, 5)
 
# def square_print(x):
#     print(x * x)

# def square_return(x):
#     return x * x

# print("== square_print ==")
# a = square_print(4)   # to tylko wydrukuje
# print("a:", a)

# print("\n== square_return ==")
# b = square_return(4)  # to zwróci wartość
# print("b:", b)
# print("b + 10:", b + 10)

# def say_hello(name):
#     return "Hello "+name
# result=say_hello("kloc")
# print(result)

# def say_hello(name):
#     print(f"Hello:{name}")
# result=say_hello("ala")
# print(result)

# def make_hello(name):
#     return "hello"+name
# msg=make_hello("asia")
# print("msg:",msg)

# def debug_hello(name):
#     print("Generating hello for", name)
#     return "hello "+ name
# val=debug_hello("asia")
# print("val:", val)

# def introduction(first_name="Kacl", last_name="Smith"):
#     print("Hello, my name is", first_name, last_name)
# introduction("kama")

# def list_sum(lst):
#     s = 0
 
#     for elem in lst:
#         s += elem
 
#     return s
# print(list_sum(5))

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
months_31_days=[month for month in range(1,8,2)]+[month for month in range(8,13,2)]
months_30_days=[month for month in range(2,7,2)if month!=2]+[month for month in range(9,12,2)]


def days_in_month(year,month):
    if not(1<=month<=12):
        return -1
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
    
