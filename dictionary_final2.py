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
items = [1, "a", 2.5, "b", True, None, 3]
types = {}

for i in items:
    t = type(i).__name__
    types[t] = types.get(t, 0) + 1

print(types)