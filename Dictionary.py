# Zadanie treningowe

# Napisz program, który:

# Tworzy słownik o nazwie osoba z danymi:

# {"imie": "Damian", "miasto": "Kraków", "auto": "Vito"}

# Wypisuje miasto tej osoby

# Dodaje klucz "zawod" o wartości "kierowca"

# Zmienia wartość "auto" na "Toyota"

# Wypisuje wszystkie klucze i wartości w formacie:

# imie → Damian
# miasto → Kraków
# auto → Toyota
# zawod → kierowca

# info={"imie": "Damian", "miasto": "Kraków", "auto": "Vito"}
# print(info["miasto"])
# info["zawod"]="kierowca"
# info["auto"]="Toyota"
# for n,v in info.items():
#     print(n,"->",v)

# **********************************************************************************************************
# **********************************************************************************************************
# Zadanie 1 – Licznik wystąpień słów

# Napisz program, który:

# Wczyta tekst od użytkownika.

# Policz, ile razy każde słowo wystąpiło.

# Wynik zapisz w słowniku w formacie:
# {słowo: liczba_wystąpień}

# Wypisz słownik.

# 💡 Podpowiedź:

# użyj split(), żeby rozdzielić słowa

# sprawdzaj if słowo in dict, żeby zwiększyć licznik

# Przykład:

# Podaj tekst: damian lubi python bo damian uczy się python


# ✅ Wynik:

# {'damian': 2, 'lubi': 1, 'python': 2, 'bo': 1, 'uczy': 1, 'się': 1}
# **********************************************************************************************************
# sentence=input("Wpisz tekst do policzenia ilości wystąpień: ")
# words=sentence.split()
# word_count={}
# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1
# print(word_count)
# **********************************************************************************************************
# **********************************************************************************************************

# info = {"imie": "Damian","wiek":"12"}
# print(info.get("wiek", "Brak danych"))
# print(info.get("imie", "Brak danych"))
# **********************************************************************************************************
# **********************************************************************************************************
# zadanie: „Sprawdź dane użytkownika”

# Masz słownik:

# user = {"imie": "Damian", "miasto": "Kraków"}

# 🔹 Zrób program, który:

# Poprosi użytkownika o wpisanie klucza, np. "wiek", "miasto", "auto", itd.

# Sprawdzi, czy taki klucz istnieje w słowniku.

# Jeśli istnieje → wypisze wartość.

# Jeśli nie istnieje → wypisze "Brak danych" (użyj .get()).

# 💡 Przykładowe działanie:
# Podaj klucz: miasto
# Kraków

# Podaj klucz: wiek
# Brak danych

# **********************************************************************************************************

# user = {"imie": "Damian", "miasto": "Kraków"}
# guess=input("Zgadnij klucz: ")
# print(user.get(guess,"Brak danych"))

# **********************************************************************************************************
# **********************************************************************************************************
# Zadanie 1 — sklep

# Masz:

# ceny = {"jabłko": 3, "banan": 4, "gruszka": 5}


# Program:

# pyta użytkownika o nazwę owocu,

# wypisuje cenę, jeśli istnieje,

# albo "Brak w sklepie" jeśli nie ma.

# **********************************************************************************************************
# ceny = {"jabłko": 3, "banan": 4, "gruszka": 5}
# fruit=input("Podaj nazwę owocu: ")
# print(ceny.get(fruit,"Brak w sklepie"))
# **********************************************************************************************************
# **********************************************************************************************************
# Zadanie 2 — loginy
# loginy = {"damian": "qwerty", "bartek": "abc123"}


# Użytkownik wpisuje login → wypisz hasło, jeśli istnieje,
# w przeciwnym razie "Nie znaleziono użytkownika".

# **********************************************************************************************************
# loginy = {"damian": "qwerty", "bartek": "abc123"}
# login=input("Wpisz login: ")
# print(loginy.get(login,"Nie znaleziono użytkownika"))

# **********************************************************************************************************
# **********************************************************************************************************
# Zadanie 3 — kraj i stolica
# kraje = {"Polska": "Warszawa", "Francja": "Paryż", "Niemcy": "Berlin"}


# Użytkownik wpisuje nazwę kraju.
# Program ma wypisać jego stolicę, a jeśli kraju nie ma → "Nie znam takiego kraju"

# **********************************************************************************************************
# kraje = {"Polska": "Warszawa", "Francja": "Paryż", "Niemcy": "Berlin"}
# kraj=input("Wpisz nazwe kraju: ")
# print(kraje.get(kraj,"Nie znam takiego kraju"))
# **********************************************************************************************************
# **********************************************************************************************************
# 1️⃣ Dictionary comprehension — tworzenie słownika w jednej linijce

# To taki „generator” słownika, podobny do list comprehension.

# slowa = ["python", "dict", "code"]
# dlugosci = {s: len(s) for s in slowa}
# print(dlugosci)


# ➡️ wynik:

# {'python': 6, 'dict': 4, 'code': 4}


# czyli:

# “dla każdego słowa z listy zrób klucz = słowo, wartość = jego długość”

# 💡 Idealne do przekształcania danych z list.
# **********************************************************************************************************
# slowa = ["python", "dict", "code"]
# dlugosci = {s: len(s) for s in slowa}
# print(dlugosci)
# 2️⃣ Odwracanie słownika (zamiana kluczy z wartościami)
# kraje = {"Polska": "Warszawa", "Niemcy": "Berlin"}
# stolice = {v: k for k, v in kraje.items()}
# print(stolice)
# **********************************************************************************************************
# 3️⃣ Łączenie słowników w jeden (Python 3.9+)

# Od wersji Pythona 3.9 możesz po prostu:

# a = {"imie": "Damian","miasto":"Rzeszów"}
# b = {"miasto": "Kraków"}
# c = a | b
# print(c)

# Lub nadpisywanie:

# c = a | {"imie": "Bartek"}


# 💡 To szybsze niż update() i nie zmienia oryginału.
# **********************************************************************************************************
# 🧱 5️⃣ Zagnieżdżone słowniki

# Masz dane „w środku danych”:

# baza = {
#     "Damian": {"wiek": 28, "auto": "Toyota"},
#     "Bartek": {"wiek": 26, "auto": "BMW"}
# }

# print(baza["Bartek"]["auto"])  # BMW
# # **********************************************************************************************************
# 6️⃣ Zliczanie wystąpień (pro sposób z modułu collections)

# Nie musisz robić pętli — Python ma to gotowe:

# from collections import Counter
# slowa = ["damian", "lubi", "python", "damian", "python", "python"]
# print(dict(Counter(slowa)))
# # **********************************************************************************************************
# # **********************************************************************************************************
# Zadanie 1 — Licznik długości słów

# Masz listę:

# slowa = ["python", "dict", "code", "damian", "ai"]


# Stwórz słownik, w którym:

# klucz = słowo

# wartość = długość tego słowa

# 💡 wynik powinien być:
# {'python': 6, 'dict': 4, 'code': 4, 'damian': 6, 'ai': 2}
# # **********************************************************************************************************
# slowa = ["python", "dict", "code", "damian", "ai"]
# licznik_liter={}
# for slowo in slowa:
#     licznik_liter[slowo]=len(slowo)
# print(licznik_liter)

# # **********************************************************************************************************
# # # **********************************************************************************************************
# Zadanie 2 — Najlepszy zawodnik

# Masz:

# punkty = {"Damian": 80, "Bartek": 65, "Kuba": 92, "Michał": 88}


# Wypisz imię zawodnika, który ma najwięcej punktów, w formacie:

# Najlepszy: Kuba (92 pkt)
# # # **********************************************************************************************************
# punkty = {"Damian": 80, "Bartek": 65, "Kuba": 92, "Michał": 88}
# najlepszy = max(punkty, key=punkty.get)
# print("Najlepszy:", najlepszy, "(", punkty[najlepszy], "pkt)")

punkty = {"Damian": 80, "Bartek": 65, "Kuba": 92, "Michał": 88}

najlepszy = max(punkty, key=punkty.get())
print("Najlepszy:", najlepszy, "(", punkty[najlepszy], "pkt)")