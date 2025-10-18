# Zadanie 1 — prosty input
# 🔹 Napisz program, który:
# Poprosi użytkownika o liczbę.
# Spróbuje podzielić 100 przez tę liczbę.
# Obsłuży błędy:
# dzielenie przez zero,
# wprowadzenie tekstu zamiast liczby.
# 💡 Podpowiedź: użyj try, except ZeroDivisionError, except ValueError.
# Przykład działania:
# Podaj liczbę: 0
# Nie dziel przez zero!

# Podaj liczbę: abc
# To nie jest liczba!
# Podaj liczbę: 4
# Wynik: 25.0

# try:
#     number=int(input("Podaj liczbe: "))
#     result=100/number
# except ZeroDivisionError:
#     print("nie dzielimy przez zero! ")
# except ValueError:
#     print("to nie liczba! ")
# else:
#     print(result)
# finally:
#     print("koniec programu!")
# *******************************************************************************************************
# *******************************************************************************************************
# Zadanie 2 — lista i IndexError

# Masz listę:

# lista = [10, 20, 30]


# 🔹 Poproś użytkownika o numer indeksu.
# 🔹 Spróbuj wypisać element o tym indeksie.
# 🔹 Jeśli użytkownik poda indeks spoza zakresu — złap IndexError.
# 🔹 Jeśli wpisze coś, co nie jest liczbą — złap ValueError.

# lista = [10, 20, 30]
# try:
#     select=int(input("Podaj numer indexu: "))
#     print(lista[select])
# except IndexError:
#     print("podałeś nieistniejący numer indexu!")
# except ValueError:
#     print("to nie jest liczba")
# else:
#     print("Sukces!")
# *******************************************************************************************************
# *******************************************************************************************************

# Zadanie 3 — otwieranie pliku

# 🔹 Spróbuj otworzyć plik o nazwie dane.txt.
# 🔹 Jeśli plik nie istnieje — złap FileNotFoundError i wypisz komunikat
# "Nie znaleziono pliku!".
# 🔹 W finally wypisz "Zakończono operację pliku.".
# try:
#     file=open("dane.txt")
# except FileNotFoundError:
#     print("nie znaleziono takiego pliku!")
# finally:
#     print("zakończono operację!")
# *******************************************************************************************************
# *******************************************************************************************************

# Zadanie 4 — łączony except

# 🔹 Zrób program, który prosi użytkownika o:

# licznik (liczba A)

# mianownik (liczba B)

# 🔹 Spróbuj wykonać dzielenie A / B.
# 🔹 Złap oba błędy (ValueError i ZeroDivisionError) w jednym except, np.:
# try:
#     a=int(input("Wprowadź licznik: "))
#     b=int(input("Wprowadź mianownik: "))
#     result=a/b
# except ValueError:
#     print("nie wprowadziłeś cyfry!")
# except ZeroDivisionError:
#     print("nie dziel przez zero")
# else:
#     print(result)
# finally:
#     print("koniec programu!-")

# *******************************************************************************************************
# *******************************************************************************************************
# Zadanie 5

# Napisz program, który:

# Prosi użytkownika o podanie liczby.

# Próbuje policzyć 10 / liczba.

# Jeśli coś pójdzie nie tak, złapie błąd za pomocą Exception as e

# Wypisze typ błędu i treść błędu.

# Na końcu zawsze wypisze "Koniec programu."
try:
    number=int(input("podaj liczbę: "))
    result=10/number
except Exception as e:
    print("Błąd typu:",type(e).__name__)
    print("Treść błędu:",e)
else:
    print(result)
finally:
    print("Koniec programu!")