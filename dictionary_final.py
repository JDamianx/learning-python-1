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
sentence=input("Enter your sentence: ")
words=sentence.split(" ")
count={}
for word in words:
    count[word]=count.get(word,0)+1
print(count)