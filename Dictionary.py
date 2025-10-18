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
sentence=input("Wpisz tekst do policzenia ilości wystąpień: ")
words=sentence.split()
counts={}
for word in words:
    if word in counts:
        counts[word]+=1
    else:
        counts[word]=1
print(counts)