# Zadanie 1 — Zamiana kluczy z wartościami

# Masz:

# kody = {"PL": "Polska", "FR": "Francja", "DE": "Niemcy"} 


# Stwórz nowy słownik, gdzie klucze i wartości są zamienione miejscami,
# czyli ma wyjść:
{'Polska': 'PL', 'Francja': 'FR', 'Niemcy': 'DE'}
# ******************************************************************************************
# kody = {"PL": "Polska", "FR": "Francja", "DE": "Niemcy"} 
# nowe_kody={v:k for k,v in kody.items()}
# print(nowe_kody)
# ******************************************************************************************
# ******************************************************************************************
# 🧩 Zadanie 2 — Filtr punktów

# Masz:

# punkty = {"Damian": 95, "Bartek": 68, "Kuba": 81, "Michał": 47}


# Utwórz nowy słownik tylko z tymi osobami, które mają 70+ punktów.
# ******************************************************************************************
# punkty = {"Damian": 95, "Bartek": 68, "Kuba": 81, "Michał": 47}
# top_punkty = {}
# for imie, wynik in punkty.items():
#     if wynik > 70:
#         top_punkty[imie] = wynik
# print(top_punkty)
# ******************************************************************************************
# ******************************************************************************************
# Zadanie 4 — Najczęstsze słowo

# Masz:

# tekst = "python jest super i python jest fajny bo python jest prosty"


# Policz, ile razy każde słowo występuje, i wypisz to, które pojawia się najczęściej.
# ➡️ wynik:

# Najczęstsze słowo: python (3 razy)
# ******************************************************************************************
tekst = "python jest super i python jest fajny bo python jest prosty"
words=tekst.split()
word_count={}
for word in words:
    word_count[word]=word_count.get(word,0)+1
# most_used_word=max(word_count, key=word_count.get)
max_value=max(word_count.values())
best=[w for w, v in word_count.items() if v==max_value]




print("Najczęściej używany wyraz to:",best,"i został użyty:",max_value )