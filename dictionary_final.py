# Zadanie 5 — Sumowanie wartości o tych samych kluczach

# Masz dwa słowniki:

# a = {"jabłka": 3, "banany": 2, "gruszki": 5}
# b = {"banany": 4, "gruszki": 1, "śliwki": 7}


# Połącz je tak, żeby wartości się sumowały, a brakujące klucze się po prostu dodały.
# Czyli wynik powinien być taki:

# {'jabłka': 3, 'banany': 6, 'gruszki': 6, 'śliwki': 7}


# 💡 Wskazówka tylko logiczna (bez kodu):
# musisz przelecieć po b.items() i dla każdego klucza:

# dodać go do a, jeśli go nie ma,

# jeśli już jest, to zwiększyć jego wartość.
# *******************************************************************************************

# a = {"jabłka": 3, "banany": 2, "gruszki": 5}
# b = {"banany": 4, "gruszki": 1, "śliwki": 7}

# for k,v in b.items():
#     if k in a:
#         a[k]+=v
#     else:
#         a[k]=v
# print(a)


# *******************************************************************************************
# *******************************************************************************************
# Zadanie — liczenie liter w słowie

# Użytkownik wpisuje jakieś słowo, np.

# banan


# Program ma zliczyć, ile razy każda litera występuje,
# i wypisać wynik w formie słownika:

# {'b': 1, 'a': 2, 'n': 3}


# 💡 Możesz użyć .get(), żeby przy każdym obiegu pętli dodać +1 do odpowiedniej litery.

# Nie ma ifów, nie ma kombinacji — tylko pętla i .get().

# *******************************************************************************************
# {'b': 1, 'a': 2, 'n': 3}
# word=input("Input word: ")
# count={}
# for letter in word:
#     count[letter]=count.get(letter,0)+1
# print(count)


# *******************************************************************************************
# *******************************************************************************************
# sentence=input("Enter your sentence: ")
# words=sentence.split(" ")
# count={}
# for word in words:
#     count[word]=count.get(word,0)+1
# print(count)
# *******************************************************************************************
# *******************************************************************************************
# punkty = {
#     "Damian": 95,
#     "Bartek": 68,
#     "Kuba": 81,
#     "Michał": 47
# }
# max_punkty=max(punkty, key=punkty.get) # type:ignore
# print(max_punkty)

# *******************************************************************************************
# *******************************************************************************************
# Zadanie 1 (rozgrzewka)

# Masz taki słownik:

# owoce = {"jabłka": 3, "banany": 5, "śliwki": 2}


# Dodaj do niego nowy klucz "gruszki" o wartości 4.
# Potem zwiększ ilość bananów o 2.
# *******************************************************************************************
# owoce = {"jabłka": 3, "banany": 5, "śliwki": 2}
# owoce["gruszki"]=4
# owoce["banany"]+=2
# print(owoce)
# *******************************************************************************************
# *******************************************************************************************
# Zadanie 2 — wersja z get()

# Masz taki ciąg znaków:

# word = "programowanie"


# Twoim zadaniem jest policzyć, ile razy występuje każda litera i zapisać to w słowniku count,
# czyli żeby wynik wyglądał np. tak:
# {'p': 1, 'r': 2, 'o': 2, 'g': 1, ...}

# Podpowiedź:

# utwórz pusty słownik count = {}

# przeleć pętlą for po każdej literze

# użyj count.get(litera, 0) żeby zwiększać licznik
# *******************************************************************************************
# word = "programowanie"
# count={}
# for letter in word:
#     count[letter]=count.get(letter,0)+1
# print(count)

# *******************************************************************************************
# *******************************************************************************************
# Zadanie 3

# Masz dwa słowniki:

# a = {"jabłka": 3, "banany": 2, "gruszki": 5}
# b = {"banany": 4, "gruszki": 1, "śliwki": 7}


# Połącz je tak, żeby w nowym słowniku były wszystkie owoce, a jeśli jakiś się powtarza — dodaj wartości.
# Czyli np. banany → 2 + 4 = 6.
# *******************************************************************************************
a = {"jabłka": 3, "banany": 2, "gruszki": 5}
b = {"banany": 4, "gruszki": 1, "śliwki": 7}
# for k,v in b.items():
#     if k in a:
#         a[k]+=v
#     else:
#         a[k]=v
# print(a)
# for k,v in b.items():
#     c={k:a.get(k,0)+b.get(k,0) for k in a|b}

# print(c)


# *******************************************************************************************
# *******************************************************************************************
# Zadanie 1 — „długość słów”

# Masz listę:

# slowa = ["python", "jest", "mega", "sztosem"]


# Napisz dict comprehension, które stworzy słownik w formacie:

# {"python": 6, "jest": 4, "mega": 4, "sztosem": 7}

# *******************************************************************************************
# slowa = ["python", "jest", "mega", "sztosem"]
# number_of_letters={k:len(k) for k in slowa}
# print(number_of_letters)
# *******************************************************************************************
# *******************************************************************************************
# Zadanie 2 — filtr w comprehension

# Masz znowu tę samą listę:

# slowa = ["python", "jest", "mega", "sztosem"]


# Zrób dict comprehension, które zbuduje słownik tylko dla słów dłuższych niż 4 litery,
# czyli wynik ma być:

# {"python": 6, "sztosem": 7}


# Podpowiedź:
# na końcu comprehension możesz dodać warunek, np.

# {k: coś for k in slowa if ...}
# *******************************************************************************************
# slowa = ["python", "jest", "mega", "sztosem"]
# filtered={k:len(k) for k in slowa if len(k)>4}
# print(filtered)
# *******************************************************************************************
# *******************************************************************************************
# Zadanie 3 — podatek od pensji

# Masz słownik z pensjami pracowników:

# pensje = {"Damian": 7200, "Bartek": 5100, "Kuba": 4600, "Michał": 8000}


# Twoje zadanie:

# policz 10% podatek dla każdego,

# zwróć nowy słownik, gdzie klucz to imię, a wartość to kwota po potrąceniu podatku.

# czyli wynik ma wyglądać np. tak:

# {'Damian': 6480.0, 'Bartek': 4590.0, 'Kuba': 4140.0, 'Michał': 7200.0}
# *******************************************************************************************
# pensje = {"Damian": 7200, "Bartek": 5100, "Kuba": 4600, "Michał": 8000}
# after_tax={k:v-(v*0.1) for k,v in pensje.items()}
# print(after_tax)
# *******************************************************************************************
# *******************************************************************************************
# Zadanie 4 — selektywny podatek

# Masz znowu:

# pensje = {"Damian": 7200, "Bartek": 5100, "Kuba": 4600, "Michał": 8000}


# Twoje zadanie:

# potrąć 10% podatku tylko tym, którzy zarabiają więcej niż 5000,

# pozostali mają bez zmian,

# wynik to nowy słownik w formacie:

# {'Damian': 6480.0, 'Bartek': 4590.0, 'Kuba': 4600, 'Michał': 7200.0}]
pensje = {"Damian": 7200, "Bartek": 5100, "Kuba": 4600, "Michał": 8000}
after_tax={k:v-(v*0.1)if v>5000 else v for k,v in pensje.items()}
print(after_tax)