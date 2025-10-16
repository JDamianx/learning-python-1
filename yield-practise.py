# # ETAP 1 – „yield w ruchu”

# Zrób nowy plik, np. yield_demo.py, i wklej to:

# def countdown(n):
#     print("Start odliczania!")
#     while n > 0:
#         yield(f"{n}")
#         n -= 1
#     print("Koniec!")

# for number in countdown(3):
#     print("Liczba:", number)

# ***************************************************************************************************
# ***************************************************************************************************
# Zadanie: Generator parzystych liczb

# Napisz funkcję even_numbers(n), która:

# używa yield,

# zwraca kolejne liczby parzyste od 0 do n włącznie,

# nie tworzy żadnej listy, tylko generuje wartości po kolei.

# Przykład działania:
# def even_numbers(n):
#     for i in range(0,n+1,2):
#         yield i
# for x in even_numbers(10):
#     print(x)

# # powinno wypisać
# 0 2 4 6 8 10

# ***************************************************************************************************
# ***************************************************************************************************
# Zadanie: Generator filtrujący liczby

# Napisz funkcję filter_greater_than(numbers, limit), która:

# przyjmuje listę numbers i wartość limit,

# używa yield,

# zwraca tylko te liczby z listy, które są większe niż limit.

# Przykład działania:

# nums = [1, 5, 7, 2, 9, 3]
# for n in filter_greater_than(nums, 5):
#     print(n)
# Oczekiwany wynik:
# 7
# 9
# Zrób to bez return i bez żadnych list — tylko yield.
# Napisz swoją wersję, a potem zobaczymy, czy działa dokładnie jak powinien prawdziwy generator 👀
# ***************************************************************************************************
# ***************************************************************************************************

# def filter_greater_than(numbers, limit):
#     for n in numbers:
#         if n>limit:
#             yield n
# nums = [1, 5, 7, 2, 9, 3]
# for n in filter_greater_than(nums, 5):
#     print(n)
# ***************************************************************************************************
# ***************************************************************************************************
# Zadanie: Generator wzrostu

# Napisz funkcję growth_trend(numbers), która:

# przyjmuje listę liczb,

# używa yield,

# przy każdej iteracji zwraca True, jeśli liczba jest większa niż poprzednia, albo False w przeciwnym razie.

# Czyli:
# for trend in growth_trend([3, 5, 4, 7, 7, 9]):
#     print(trend)

# wynik:
# True
# False
# True
# False
# True

# 🔹 Zasada:

# pierwszej liczby nie porównujemy (nie ma poprzedniej),
# porównujemy dopiero od drugiego elementu.

# Zrób to na spokojnie, tylko z yield, bez list pomocniczych.
# Jak gotowe — pokaż mi swój kod, a potem razem rozbierzemy go linijka po linijce.
# Dodana wartość porównywana obok Bool
# def growth_trend(numbers):
#     previous=numbers[0]
#     for number in numbers[1:]:
#         if number>previous:
#             yield (number,True)
#         else:
#             yield (number,False)
#         previous=number
# for trend in growth_trend([3, 5, 4, 7, 7, 9]):
#     print(trend)
# ***************************************************************************************************
# ***************************************************************************************************
# Generator który pobiera i oddaje dane
def echo():
    print("Startuję generator...")
    while True:
        value = yield
        print("Odebrałem:", value)

gen = echo()
next(gen)          # uruchamia generator do pierwszego yielda
gen.send("Damian")
gen.send("Martyna")
gen.send("Koniec")
