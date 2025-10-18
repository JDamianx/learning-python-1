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
# *******************************************************************************************************
# *******************************************************************************************************
# Zadanie 2 — lista i IndexError

# Masz listę:

# lista = [10, 20, 30]


# 🔹 Poproś użytkownika o numer indeksu.
# 🔹 Spróbuj wypisać element o tym indeksie.
# 🔹 Jeśli użytkownik poda indeks spoza zakresu — złap IndexError.
# 🔹 Jeśli wpisze coś, co nie jest liczbą — złap ValueError.
# *******************************************************************************************************
# *******************************************************************************************************

# Zadanie 3 — otwieranie pliku

# 🔹 Spróbuj otworzyć plik o nazwie dane.txt.
# 🔹 Jeśli plik nie istnieje — złap FileNotFoundError i wypisz komunikat
# "Nie znaleziono pliku!".
# 🔹 W finally wypisz "Zakończono operację pliku.".
# *******************************************************************************************************
# *******************************************************************************************************

# Zadanie 4 — łączony except

# 🔹 Zrób program, który prosi użytkownika o:

# licznik (liczba A)

# mianownik (liczba B)

# 🔹 Spróbuj wykonać dzielenie A / B.
# 🔹 Złap oba błędy (ValueError i ZeroDivisionError) w jednym except, np.: