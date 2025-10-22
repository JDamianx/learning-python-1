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
c=a|b
print(c)