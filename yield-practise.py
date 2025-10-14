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
def even_numbers(n):
    for i in range(0,n+1,2):
        yield i
for x in even_numbers(10):
    print(x)

# powinno wypisać
# 0 2 4 6 8 10