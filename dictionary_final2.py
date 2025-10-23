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

animals = ["kot", "chomik", "pies", "żyrafa", "lew", "boa"]

long_animals = {a: len(a) for a in animals if len(a) > 3}
# {len(a): a for a in animals if len(a) > 3} PO ODWROCENIU NADPISUJE WARTOSC DLA KLUCZA"6"
print(long_animals)