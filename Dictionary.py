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

info={"imie": "Damian", "miasto": "Kraków", "auto": "Vito"}
print(info["miasto"])
info["zawod"]="kierowca"
info["auto"]="Toyota"
for n,v in info.items():
    print(n,"->",v)