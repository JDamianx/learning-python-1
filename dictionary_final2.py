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
# ***********************************************************************************************
# Zadanie 1 — podstawowe łączenie danych

# Masz dwa słowniki z informacjami o użytkowniku:

# person = {'name': 'Ala', 'age': 23}
# contact = {'email': 'ala@example.com', 'phone': '123-456-789'}


# Zadanie:
# ➡️ Połącz je w jeden słownik person_info, używając update().
# ➡️ Nie zmieniaj oryginalnych słowników (person, contact mają zostać takie same).
# # ***********************************************************************************************

# person = {'name': 'Ala', 'age': 23}
# contact = {'email': 'ala@example.com', 'phone': '123-456-789'}
# person_info={}
# # person_info.update(person)
# # person_info.update(contact) # stare wersje pythona, pojedynczo
# person_info.update(**person, **contact) # od pythona 3.5
# print(person_info)

# # ***********************************************************************************************
# # ***********************************************************************************************
# Zadanie: “Aktualizacja bazy uczniów”

# Masz bazę danych o uczniach — każdy ma:

# imię,

# informacje kontaktowe (contact),

# oceny (grades).

# 🧠 Punkt startowy:
# students = {
#     "Ala": {
#         "contact": {"email": "ala@oldmail.com", "phone": "111-111-111"},
#         "grades": {"math": 80, "english": 90}
#     },
#     "Olek": {
#         "contact": {"email": "olek@school.com", "phone": "222-222-222"},
#         "grades": {"math": 70, "english": 75}
#     }
# }


# I dostajesz aktualizację danych z nowego pliku (np. formularz ucznia):

# update_data = {
#     "Ala": {
#         "contact": {"email": "ala@newmail.com"},
#         "grades": {"physics": 100}
#     },
#     "Olek": {
#         "grades": {"english": 85, "math": 72}
#     }
# }

# 🎯 Twoje zadanie:

# Zaktualizuj students danymi z update_data, tak żeby:

# 1️⃣ stare dane się zachowały (nie nadpisuj całych sekcji!),
# 2️⃣ tylko podklucze (contact, grades) się zmieniły,
# 3️⃣ dodaj nowe przedmioty, jeśli ich wcześniej nie było.

# 💬 Oczekiwany wynik:
# {
#   'Ala': {
#     'contact': {'email': 'ala@newmail.com', 'phone': '111-111-111'},
#     'grades': {'math': 80, 'english': 90, 'physics': 100}
#   },
#   'Olek': {
#     'contact': {'email': 'olek@school.com', 'phone': '222-222-222'},
#     'grades': {'math': 72, 'english': 85}
#   }
# }
# # ***********************************************************************************************
# students = {
#     "Ala": {
#         "contact": {"email": "ala@oldmail.com", "phone": "111-111-111"},
#         "grades": {"math": 80, "english": 90}
#     },
#     "Olek": {
#         "contact": {"email": "olek@school.com", "phone": "222-222-222"},
#         "grades": {"math": 70, "english": 75}
#     }
    
# }
# update_data = {
#     "Ala": {
#         "contact": {"email": "ala@newmail.com"},
#         "grades": {"physics": 100}
#     },
#     "Olek": {
#         "grades": {"english": 85, "math": 72}
#     }
# }
# new_student={}
# new_student.update(students)
# for name,updates in update_data.items():
#     if name in new_student:
#         for section, new_data in updates.items():
#             new_student[name][section].update(new_data)
#         else:
#             new_student[name]=updates
# print(new_student)
# # ***********************************************************************************************
# # ***********************************************************************************************
# Zadania:

# Wypisz email ucznia.

# Wypisz ocenę z angielskiego.

# Zmień numer telefonu na "987".

# Dodaj nowy przedmiot: "physics": 6.
# # ***********************************************************************************************
# student = {
#     "name": "Ala",
#     "info": {
#         "contact": {"email": "ala@wp.pl", "phone": "123"},
#         "grades": {"math": 5, "english": 4}
#     }
# }
# print(student["info"]["contact"]["email"])
# print(student["info"]["grades"]["english"])
# student["info"]["contact"]["phone"]="987"
# print(student["info"]["contact"]["phone"])
# student["info"]["grades"]["physics"]="6"
# print(student["info"]["grades"]["physics"])
# # ***********************************************************************************************
# # ***********************************************************************************************
# Zadanie 2 – aktualizacja danych ucznia

# Masz dwa słowniki:

# student = {
#     "name": "Ala",
#     "info": {
#         "contact": {"email": "ala@wp.pl", "phone": "123"},
#         "grades": {"math": 5, "english": 4}
#     }
# }

# update_info = {
#     "info": {
#         "contact": {"email": "ala@newmail.com"},
#         "grades": {"physics": 6, "english": 5}
#     }
# }


# 🧠 Zadanie:
# Zaktualizuj student danymi z update_info,
# tak aby:

# nie stracić starych danych (phone, math),

# zaktualizować email i english,
# }
# dodać physics.
# # ***********************************************************************************************
'''import copy 
student = {
    "name": "Ala",
    "info": {
        "contact": {"email": "ala@wp.pl", "phone": "123"},
        "grades": {"math": 5, "english": 4}
    }
}

update_info = {
    "info": {
        "contact": {"email": "ala@newmail.com"},
        "grades": {"physics": 6, "english": 5}
    },
    "test":{
        "test1":{"test2":"test3"}
    }

}
updated_student={}
updated_student=copy.deepcopy(student)
for name, updates in update_info.items():
    if name in updated_student:
        for section, details in updates.items():
            updated_student[name][section].update(details)
    else:
        updated_student[name]=updates
print(updated_student)
print(student)'''
# # ***********************************************************************************************
# # ***********************************************************************************************
# profile = {
#     "id": 101,
#     "info": {
#         "name": "Ala",
#         "contact": {"email": "ala@wp.pl", "phone": "123"},
#     },
#     "skills": {
#         "python": {"level": "junior", "years": 1},
#         "english": {"level": "B2"}
#     }
# }

# patch = {
#     "info": {
#         "contact": {"email": "ala@newmail.com"},  # ma zaktualizować email, NIE usuwać phone
#     },
#     "skills": {
#         "python": {"years": 2},                    # ma nadpisać tylko 'years', zachować 'level'
#         "linux": {"level": "beginner"}             # ma dodać zupełnie nową sekcję
#     },
#     "meta": {
#         "updated_at": "2025-10-28"
#     }
# }
# Wymagania
# Nie modyfikuj profile. Zwróć nowy słownik.

# Scalaj głęboko tylko słowniki (dict→dict). Inne typy nadpisuj (np. jeśli byłaby liczba lub string).

# Zachowaj istniejące dane, gdy ich nie dotyka patch (np. numer telefonu).

# Mini-testy (możesz wkleić obok swojej funkcji)

# result = merge_profile(profile, patch)

# 1) oryginał nienaruszony
# assert profile["info"]["contact"]["email"] == "ala@wp.pl"

# # 2) email zaktualizowany w wyniku, phone zachowany
# assert result["info"]["contact"]["email"] == "ala@newmail.com"
# assert result["info"]["contact"]["phone"] == "123"

# # 3) python: years nadpisany, level zachowany
# assert result["skills"]["python"]["years"] == 2
# assert result["skills"]["python"]["level"] == "junior"

# # 4) nowa sekcja 'linux' dodana
# assert result["skills"]["linux"]["level"] == "beginner"

# # 5) nowa gałąź 'meta' dodana
# assert result["meta"]["updated_at"] == "2025-10-28"
# # ***********************************************************************************************
'''import copy
profile = {
    "id": 101,
    "info": {
        "name": "Ala",
        "contact": {"email": "ala@wp.pl", "phone": "123"},
    },
    "skills": {
        "python": {"level": "junior", "years": 1},
        "english": {"level": "B2"}
    }
}

patch = {
    "info": {
        "contact": {"email": "ala@newmail.com"},  # ma zaktualizować email, NIE usuwać phone
    },
    "skills": {
        "python": {"years": 2},                    # ma nadpisać tylko 'years', zachować 'level'
        "linux": {"level": "beginner"}             # ma dodać zupełnie nową sekcję
    },
    "meta": {
        "updated_at": "2025-10-28"
    }
}
def merge_profile(profile, patch):
    updated_profile=copy.deepcopy(profile)
    for section, updates in patch.items():
        if section in updated_profile:
            for key,value in updates.items():
                if key in updated_profile[section] and isinstance(updated_profile[section][key],dict) and isinstance(value, dict):
                    updated_profile[section][key].update(value)
                else:
                    updated_profile[section][key] = value
        else:
            updated_profile[section]=updates
    return updated_profile
print(merge_profile(profile, patch))

result = merge_profile(profile, patch)
# testy:
# 1) oryginał nienaruszony
assert profile["info"]["contact"]["email"] == "ala@wp.pl"

# 2) email zaktualizowany w wyniku, phone zachowany
assert result["info"]["contact"]["email"] == "ala@newmail.com"
assert result["info"]["contact"]["phone"] == "123"

# 3) python: years nadpisany, level zachowany
assert result["skills"]["python"]["years"] == 2
assert result["skills"]["python"]["level"] == "junior"

# 4) nowa sekcja 'linux' dodana
assert result["skills"]["linux"]["level"] == "beginner"

# 5) nowa gałąź 'meta' dodana
assert result["meta"]["updated_at"] == "2025-10-28"'''
# # ***********************************************************************************************
# # ***********************************************************************************************
# Zadanie 2.0 — “merge_settings”

# Masz dwa słowniki:

# config = {
#     "app": {
#         "theme": {"mode": "light", "font": "Roboto"},
#         "language": "en"
#     },
#     "user": {
#         "name": "Damian",
#         "email": "damian@oldmail.com"
#     },
#     "security": {
#         "2FA": False
#     }
# }

# update = {
#     "app": {
#         "theme": {"mode": "dark"},   # ma nadpisać tylko 'mode', zachować 'font'
#         "language": "pl"             # ma nadpisać cały klucz
#     },
#     "user": {
#         "email": "damian@newmail.com",
#         "notifications": {"email": True, "sms": False}
#     },
#     "security": {
#         "2FA": True,
#         "backup_codes": 5
#     },
#     "meta": {"updated": "2025-10-28"}
# }

# 🧠 Twoje zadanie:

# Napisz funkcję:

# def merge_settings(config, update):
#     ...


# która:

# nie modyfikuje oryginalnego config,

# zwraca nowy słownik po połączeniu obu,

# zachowuje stare dane, jeśli nie są aktualizowane,

# dodaje nowe, jeśli ich nie było.

# ***********************************************************************************************
import copy
config = {
    "app": {
        "theme": {"mode": "light", "font": "Roboto"},
        "language": "en"
    },
    "user": {
        "name": "Damian",
        "email": "damian@oldmail.com"
    },
    "security": {
        "2FA": False
    }
}

patch = {
    "app": {
        "theme": {"mode": "dark"},   # ma nadpisać tylko 'mode', zachować 'font'
        "language": "pl"             # ma nadpisać cały klucz
    },
    "user": {
        "email": "damian@newmail.com",
        "notifications": {"email": True, "sms": False}
    },
    "security": {
        "2FA": True,
        "backup_codes": 5
    },
    "meta": {"updated": "2025-10-28"}
}
def merge_settings(config, update):
    updated_config=copy.deepcopy(config)
    for section,updates in update.items():
        if section in updated_config:
            for key, value in updates.items():
                if key in updated_config[section] and isinstance(updated_config[section][key],dict) and isinstance(value, dict):
                    updated_config[section][key].update(value)
                else:
                    updated_config[section][key]=value
        else:
            updated_config[section]=updates
    return updated_config

merged = merge_settings(config, patch)

assert merged["app"]["theme"]["mode"] == "dark"
assert merged["app"]["theme"]["font"] == "Roboto"
assert merged["user"]["email"] == "damian@newmail.com"
assert merged["user"]["notifications"]["sms"] == False
assert merged["security"]["2FA"] == True
assert merged["security"]["backup_codes"] == 5
assert merged["meta"]["updated"] == "2025-10-28"
assert config["user"]["email"] == "damian@oldmail.com"  # oryginał nietknięty