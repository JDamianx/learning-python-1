# Zadanie dla ciebie (praktyczne, ale mądre):

# Spróbuj napisać dict comprehension, które buduje słownik z długości nazw zwierząt:

# animals = ["kot", "chomik", "pies", "żyrafa"]

# # twoje zadanie: zrób słownik {nazwa: długość}


# 👉 potem odpowiedz:

# jaki będzie wynik,

# jak Python buduje to krok po kroku,

# jak byś zrobił to samo przy użyciu listy krotek (tuple) i funkcji dict().
# ***********************************************************************************************

# animals = ["kot", "chomik", "pies", "żyrafa"]
# animal_cout={animal: len(animal) for animal in animals}
# print(animal_cout)
# ***********************************************************************************************
# ***********************************************************************************************
# Chcesz zobaczyć magię z kolejnym poziomem trudności?

# Spróbujmy coś bardziej „życiowego” — czyli comprehension z warunkiem (if) i małą transformacją danych.
# Zobacz przykład:

# animals = ["kot", "chomik", "pies", "żyrafa", "lew", "boa"]

# long_animals = {a: len(a) for a in animals if len(a) > 3}
# print(long_animals)


# 🧩 Pytania do ciebie:

# Jakie będą klucze w long_animals?

# Jak Python przetwarza tę instrukcję logicznie?

# Co by się zmieniło, gdybyś użył if na końcu zamiast po wartości, np.:

# {len(a): a for a in animals if len(a) > 3}


# — jakie będą wtedy klucze, jakie wartości i czemu to robi dużą różnicę?
# ***********************************************************************************************

# animals = ["kot", "chomik", "pies", "żyrafa", "lew", "boa"]

# long_animals = {a: len(a) for a in animals if len(a) > 3}
# # {len(a): a for a in animals if len(a) > 3} PO ODWROCENIU NADPISUJE WARTOSC DLA KLUCZA"6"
# print(long_animals)
# ***********************************************************************************************
# ***********************************************************************************************
# animals = {"kot", "pies"}
# print(animals.__sizeof__())
# print(dict.fromkeys(animals).__sizeof__())

# ***********************************************************************************************
# ***********************************************************************************************
# TL;DR (to, co warto zapisać do notatek)

# Index = hash & (size-1) (size = potęga 2, liczba slotów).

# Kolizje → „następne sloty z zawijaniem” (w rzeczywistości trochę sprytniej).

# Zbyt pełne? → resize (zwykle ×2) + rehash → nadal średnio O(1).

# REPL = interaktywna konsola do eksperymentów.

# Małe różnice w __sizeof__ są normalne (nagłówki/align/pola).
# ***********************************************************************************************
# ***********************************************************************************************
# Masz listę z duplikatami:

# nums = [1,2,2,3,3,3,4,4,4,4]


# Zbuduj set z nums. Jaki wynik i dlaczego?

# Zbuduj dict mapujący liczbę → liczność za pomocą comprehension (podpowiedź: dwa przebiegi lub get):

# counts = {n: ??? for n in set(nums)}


# Co się stanie, jeśli zamienisz klucz i wartość?

# Odpowiedz krótko. Jak to złapiesz, wracasz do Cisco z turbo-intuicją o tuple/set/dict.
# ***********************************************************************************************
# nums = [1,2,2,3,3,3,4,4,4,4]
# counts={n: None for n in set(nums)}
# print(set(counts))
# ***********************************************************************************************
# ***********************************************************************************************
# Mini-ćwiczenie (żeby to się zapisało w mózgu)

# Spróbuj napisać comprehension, które liczy wystąpienia tylko liczb parzystych z listy nums.
# Czyli wynik ma wyglądać tak:

# {2: 2, 4: 4}


# Zrób to najpierw z .count(), potem z .get() (czyli „manualnie”).
# ***********************************************************************************************
# from collections import Counter
# nums = [1,2,2,3,3,3,4,4,4,4]
# counts={n:nums.count(n) for n in set(nums) if n%2==0} # wersja z .count()
# count={}
# for n in nums:
#     count[n]=count.get(n,0)+1 # wersja z .get()
# count=Counter(nums) # wersja z collections Counter
# print(count)


# ***********************************************************************************************
# ***********************************************************************************************
# Liczenie liter w zdaniu (twój własny mini-Counter)
# ***********************************************************************************************
# sentence = "harvard python rocks"
# counts = {}
# for char in sentence:
#     if char != " ":
#         counts[char] = counts.get(char, 0) + 1
# print(counts)
# ***********************************************************************************************
# ***********************************************************************************************
# Grupowanie słów po pierwszej literze
# ***********************************************************************************************
# words = ["apple", "ant", "banana", "berry", "cherry"]
# groups = {}

# for w in words:
#     first = w[0]
#     groups[first] = groups.get(first, []) + [w]

# print(groups)
# ***********************************************************************************************
# Zliczanie typów danych w liście
# ***********************************************************************************************
# items = [1, "a", 2.5, "b", True, None, 3]
# types = {}

# for i in items:
#     t = type(i).__name__
#     types[t] = types.get(t, 0) + 1

# print(types)
# ***********************************************************************************************
# ***********************************************************************************************
# Zliczanie słów w tekście (wersja prawdziwego kodera)
# ***********************************************************************************************
# text = "Python is great and Python is simple"
# counts = {}
# for word in text.lower().split():
#     counts[word] = counts.get(word, 0) + 1

# print(counts)
# ***********************************************************************************************
# ***********************************************************************************************
# Tworzenie mapy „ostatni indeks wystąpienia”
# ***********************************************************************************************
# nums = [5, 2, 5, 3, 2, 5]
# positions = {}

# for idx, n in enumerate(nums):
#     positions[n] = idx

# print(positions)
# ***********************************************************************************************
# ***********************************************************************************************
# Wzorzec
# d[x] = d.get(x, 0) + 1	licznik (sumowanie wartości)
# d[x] = d.get(x, []) + [nowy]	grupowanie elementów
# `d[x] = d.get(x, set())	dodawanie unikalnych wartości
# d[x] = coś	nadpisywanie (nie wymaga get)
# ***********************************************************************************************
# ***********************************************************************************************
# Zadanie: analiza transakcji w sklepie

# Masz listę zakupów, gdzie każda pozycja to (klient, produkt):

# purchases = [
#     ("Ala", "jabłko"),
#     ("Olek", "gruszka"),
#     ("Ala", "banan"),
#     ("Olek", "jabłko"),
#     ("Ala", "gruszka"),
#     ("Basia", "banan"),
#     ("Olek", "banan"),
#     ("Basia", "jabłko"),
# ]


# Chcemy dowiedzieć się trzech rzeczy:

# 1️⃣ Ile każdy klient zrobił zakupów?
# (np. Ala: 3, Olek: 3, Basia: 2)

# 2️⃣ Ile razy kupiono każdy produkt?
# (np. jabłko: 3, banan: 3, gruszka: 2)

# 3️⃣ Jakie produkty kupił każdy klient — jako lista (np. Ala: ['jabłko', 'banan', 'gruszka']).
# Twoje zadanie

# Spróbuj sam napisać kod, który:

# tworzy trzy słowniki: client_counts, product_counts, client_items

# w jednej pętli for name, item in purchases:

# po zakończeniu drukuje każdy z nich.

# ***********************************************************************************************

# purchases = [
#     ("Ala", "jabłko"),
#     ("Olek", "gruszka"),
#     ("Ala", "banan"),
#     ("Olek", "jabłko"),
#     ("Ala", "gruszka"),
#     ("Basia", "banan"),
#     ("Olek", "banan"),
#     ("Basia", "jabłko"),
# ]
# client_counts={}
# for name, item in purchases:
#     client_counts[name]=client_counts.get(name,0)+1 # zliczanie .get()
# print(client_counts)
# print("******************************************************")

# product_counts={}
# for name, item in purchases:
#     product_counts[item]=product_counts.get(item,0)+1 # histogram 
# print(product_counts)
# print("******************************************************")

# client_items={}
# for name, item in purchases:
#     client_items[name]=client_items.get(name, [])+ [item] # grupowanie
# print(client_items)
# ***********************************************************************************************
# ***********************************************************************************************
# Zadanie: Analizator zakupów klientów (wersja pro)

# Masz dane transakcji z małego sklepu internetowego:

# purchases = [
#     ("Ala", "jabłko", 3),
#     ("Olek", "gruszka", 1),
#     ("Ala", "banan", 2),
#     ("Olek", "jabłko", 5),
#     ("Ala", "gruszka", 1),
#     ("Basia", "banan", 4),
#     ("Olek", "banan", 3),
#     ("Basia", "jabłko", 2),
# ]


# Każdy wpis to (klient, produkt, ilość).

# 🎯 Chcemy policzyć:

# 1️⃣ łączną liczbę zakupów każdego klienta
# → np. {'Ala': 6, 'Olek': 9, 'Basia': 6}

# 2️⃣ łączną sprzedaż każdego produktu
# → np. {'jabłko': 10, 'gruszka': 2, 'banan': 9}

# 3️⃣ jakie produkty kupował każdy klient (bez duplikatów)
# → np. {'Ala': {'jabłko', 'banan', 'gruszka'}, ...}
# ***********************************************************************************************
from collections import defaultdict

purchases = [
    ("Ala", "jabłko", 3),
    ("Olek", "gruszka", 1),
    ("Ala", "banan", 2),
    ("Olek", "jabłko", 5),
    ("Ala", "gruszka", 1),
    ("Basia", "banan", 4),
    ("Olek", "banan", 3),
    ("Basia", "jabłko", 2),
]

# 1️⃣ Łączna liczba zakupów każdego klienta
client_total = defaultdict(int)

# 2️⃣ Łączna sprzedaż każdego produktu
product_total = defaultdict(int)

# 3️⃣ Produkty kupowane przez każdego klienta
client_products = defaultdict(set)

for name, item, qty in purchases:
    client_total[name] += qty           # zlicza ilość zakupionych sztuk
    product_total[item] += qty           # zlicza łączną sprzedaż produktu
    client_products[name].add(item)      # dodaje produkt do zbioru (unikalne)

print("🧾 Ilość zakupów klientów:")
print(dict(client_total))

print("\n🍎 Sprzedaż produktów:")
print(dict(product_total))

print("\n🛒 Produkty kupowane przez klientów:")
print({k: list(v) for k, v in client_products.items()})
