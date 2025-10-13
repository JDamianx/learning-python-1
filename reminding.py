# nums = [1, 2, 3]
# nums.append(4)
# nums[0] = 10
# print(nums[0:3]) # slicing

# t = (1, 2, 3)
# print(t)

# p=[1,2,3,4]
# print(p)

# person = {"name": "Martyna", "age": 27}
# print(person["age"])
# ************************************************************************************************************
# ************************************************************************************************************
# Zadanie 1: Podstawowe operacje
# Napisz program, który:
# Poprosi użytkownika o jego imię, wiek i miasto.
# Wypisze na ekranie zdanie w stylu:
# Cześć Damian, masz 28 lat i mieszkasz w Krakowie!
# Ale jeśli użytkownik poda wiek jako np. „dwadzieścia”, 
# program ma się nie wywalić —
#  tylko spokojnie powiedzieć, że podał niepoprawny wiek 
# (czyli musisz zrobić prostą obsługę błędu przy int()).
# Spróbuj użyć try / except ValueError: – tak jak w 4.7, ale bardzo prosto.
# Jak napiszesz swój kod, wklej go tutaj, 
# a ja ci go sprawdzę linia po linii i powiem,
#  jak można go ulepszyć albo co działa świetnie.
# Jedziemy — napisz swój kod.
# ********************************************************************************
# try:
#     name=input("Podaj imie: ")
#     age=int(input("podaj  wiek: "))
#     city=input("podaj miasto: ")
#     print(f"Cześć {name}, masz {age} lat i mieszkasz w {city}")
# except ValueError:
#     print("podałeś niepoprawny wiek")


# **************************************************************************************************************
# **************************************************************************************************************
# Zadanie 2: Liczba dodatnia, ujemna czy zero

# Napisz program, który:

# Pobiera od użytkownika liczbę (może być ujemna, dodatnia lub zero).

# Sprawdza:

# jeśli liczba > 0 → wypisz "Liczba dodatnia",

# jeśli liczba < 0 → wypisz "Liczba ujemna",

# jeśli liczba == 0 → wypisz "To jest zero."

#  Jeśli użytkownik poda coś, co nie jest liczbą — obsłuż to try/except, żeby nie wywaliło błędu.
# Zwróć uwagę, żeby konwersję int() wstawić do bloku try, a nie całego programu (bo potem warunki nie potrzebują try).

# # Jak to zrobisz, wklej swój kod — sprawdzimy razem i poprawimy ewentualne detale stylu.

# **************************************************************
# try:
#     number=int(input("Podaj liczbę całkowitą: "))   
#     if number>0:
#         print("Liczba dodatnia!")
#     elif number==0:
#         print("To jest zero!")
#     else:
#         print("Liczba jest ujemna!")
# except ValueError:
#     print("Nie wprowadziłeś liczby!")
# **********************************************************************************************************************************
# **********************************************************************************************************************************
# POWTÓRKA Z PĘTLI (etap 1)
# Zadanie 1: podstawowa pętla for

# Napisz pętlę for, która:

# wypisze liczby od 1 do 10 włącznie,

# ale zamiast zwykłego print(i) niech wypisuje w stylu:
# Liczba nr 1
# Liczba nr 2
# ...
# Liczba nr 10
# Pamiętaj: range() kończy się przed drugim argumentem.
# Po tym, jak to zrobisz, przejdziemy od razu do pętli w pętli — np. tabliczka mnożenia 1–5, albo licznik współrzędnych (x, y).
# Napisz najpierw to pierwsze (Zadanie 1) i wklej kod.
# **************************************************************************************************************************************
# **************************************************************************************************************************************
# Etap 2 — pętla w pętli

# Teraz coś ciekawszego.
# Zadanie 2: mini tabliczka mnożenia

# Napisz program, który:

# użyje dwóch pętli for (jedna w drugiej),

# wypisze wyniki mnożenia liczb od 1 do 5,
# np. w stylu:

# 1 x 1 = 1
# 1 x 2 = 2
# ...
# 5 x 5 = 25


# Hint:
# pierwsza pętla to liczba a,
# druga pętla to liczba b,
# a w środku print(f"{a} x {b} = {a*b}").

# Zrób to w swoim stylu — jak chcesz, możesz dodać puste linie między sekcjami (np. po każdej kolumnie).
# *****************************************************************************************************
# mylist=[1,2,3,4,5]
# for a in mylist:
#     for b in mylist:
#         print(f"{a} * {b} = {a*b}")
# **************************************************************************************************************************************
# **************************************************************************************************************************************
# Zadanie 3: Kwadrat z gwiazdek

# Napisz program, który:

# Poprosi użytkownika o liczbę n (np. 5).

# Wypisze na ekranie kwadrat n x n z gwiazdek *, np.:

# *****
# *****
# *****
# *****
# *****
# Wskazówki:

# Zrób dwie pętle for – jedna do wierszy, druga do kolumn.

# Użyj end="" w print(), żeby gwiazdki były w jednym wierszu.

# Po każdej linii dodaj print() pusty, żeby przejść do następnej

# Zrób ten kod w swoim stylu (możesz dorzucić jakieś ozdobne napisy przed/po, jak chcesz).
# Jak skończysz, pokaż kod i sprawdzimy, czy śmiga idealnie.
# *****************************************************************************************************

# n=int(input("Podaj liczbę: "))

# for j in range (n):
#     for k in range(n):
#         print("* ",end="")
#     print()

# **************************************************************************************************************************************
# **************************************************************************************************************************************
# Zadanie 4: współrzędne (x, y)

# Napisz program, który:

# Użyje dwóch pętli for:

# x od 0 do 3

# y od 0 do 2

# Wypisze wszystkie możliwe pary (x, y) w formacie:

# Punkt: (0, 0)
# Punkt: (0, 1)
# Punkt: (0, 2)
# Punkt: (1, 0)
# ...
# Punkt: (3, 2)

# Wskazówka:
# To świetne ćwiczenie na myślenie w dwóch wymiarach, które potem wykorzystasz np. w grach, grafice, albo w tablicach 2D.

# Zrób to klasycznie pętlą w pętli — a jak zadziała, dorzucimy potem do tego coś sensowniejszego, np. warunki (filtr punktów albo odległość od środka).

# *****************************************************************************************************

# for x in range(0,4):
#     for y in range(0,3):
#         print(f"Punkt: ({x}, {y})")

# **************************************************************************************************************************************
# **************************************************************************************************************************************
# Zadanie 5: powtarzanie aż do poprawnego wejścia

# Zrób program, który:

# Pyta użytkownika o hasło (input()).

# Jeśli hasło to "python123", wypisuje "Zalogowano!" i przerywa pętlę.

# W przeciwnym razie — "Złe hasło, spróbuj ponownie."

# Pętla musi wykonać się minimum raz (czyli symulacja do...while).
# *****************************************************************************************************

# name=input("Wprowadź login: ")
# counter=0
# while True: 
    
#     password=input("Wprowadź hasło: ")
#     if password=="python123":
#         print("zalogowano!")
#         break
#     else:
#         counter+=1
#         print("złe hasło!")
#         if counter==3:
#             print("Chyba chcesz się włamać!!!")
#             break

# ************************************************************************************************************
# ************************************************************************************************************

# Zadanie 7: pętla for po liście

# Masz listę imion: 

# names = ["Damian", "Martyna", "Kuba", "Kacper"]

# Napisz program, który:

# przeleci po tej liście pętlą for,

# wypisze każde imię z numerem, np.

# 1. Damian
# 2. Martyna
# 3. Kuba
# 4. Kacper

# Spróbuj to zrobić bez użycia indeksów (range(len(...))), tylko z enumerate().
# *****************************************************************************************************

# names = ["Damian", "Martyna", "Kuba", "Kacper"]
# counter=0
# for name in names:
#     counter+=1
#     print(f"{counter}. {name}")
# *****************************************************************************************************
# WERSJA Z ENUMERATE
# names = ["Damian", "Martyna", "Kuba", "Kacper"]
# for name, i in enumerate(names, start=1):
#     print(i, name)
# ************************************************************************************************************
# ************************************************************************************************************

# Napisz własną funkcję my_enumerate(iterable, start=0), która działa tak samo jak enumerate() — czyli:

# przyjmuje listę (np. ["Damian", "Martyna", "Kuba"])

# zwraca pary (index, element)

# pozwala ustawić, od jakiej liczby zaczyna się numeracja (parametr start)

# Nie używaj enumerate() w środku 😏

# Na końcu przetestuj ją tak:

# for i, name in my_enumerate(["Damian", "Martyna", "Kuba"], start=1):
#     print(i, name)

# def my_enumerate(iterable, start=0):
#     index = start
#     result = []
#     # for element in iterable:
#     #     result.append((index,element))
#     #     index+=1
#     # return result    
#     for element in iterable:
#         yield(index,element)
#         index+=1

# for i, name in my_enumerate(["Damian", "Martyna", "Kuba"], start=1):
#     print(i, name)
# ************************************************************************************************************
# ************************************************************************************************************
# Zadanie 8: Lista zakupów z możliwością usuwania

# Masz startową listę zakupów:

# shopping = ["chleb", "masło", "mleko", "cola", "chipsy"]

# Twój program ma:

# wypisać listę w formacie:

# 1. chleb
# 2. masło
# 3. mleko
# 4. cola
# 5. chipsy

# użyj enumerate() z start=1

# zapytać użytkownika, który numer pozycji chce usunąć (input()).

# usunąć ten element z listy.

# wyświetlić nową listę po zmianie.

# Wskazówki:

# pamiętaj, że input() daje string → musisz przekonwertować na int,

# indeks w Pythonie zaczyna się od 0, a twoje numerowanie od 1,
# więc trzeba odjąć 1, żeby się zgadzało przy pop().
# ************************************************************************************************************
# shopping = ["chleb", "masło", "mleko", "cola", "chipsy"]
# for i, prod in enumerate(shopping,start=1):
#     print(f"{i}. {prod}")
          
# remover=int(input("Wybierz numer produktu do wyrzucenia z listy zakupów: "))
# remover-=1
# shopping.pop(remover)
# for i, prod in enumerate(shopping,start=1):
#     print(f"{i}. {prod}")

# ************************************************************************************************************
# ************************************************************************************************************

# Zadanie 9: Konsolowa lista zakupów (wersja 2.0)

# Twoja aplikacja ma działać tak:

# === LISTA ZAKUPÓW ===
# 1. chleb
# 2. masło
# 3. mleko
# 4. cola
# 5. chipsy

# Wybierz opcję:
# 1 - pokaż listę
# 2 - dodaj produkt
# 3 - usuń produkt
# 4 - zakończ

# Po wyborze:

# 1 – wypisuje listę (z numeracją przez enumerate())

# 2 – pyta o nazwę nowego produktu i dodaje go na koniec

# 3 – pyta o numer do usunięcia i usuwa go (pop() + komunikat co usunięto)

# 4 – kończy działanie (break)

# Jeśli ktoś wpisze coś innego → komunikat o błędzie i menu pokazuje się znowu

# Podpowiedzi logiczne (bez kodu):

# całość w while True:

# w środku if / elif / else dla wyboru akcji

# po każdej akcji warto dodać pusty print() żeby się ładnie oddzielało

# Zrób to sam — i jak już będzie działać, wklej cały kod tutaj.
# Wtedy go przelecimy razem i dopieścimy tak, żeby wyglądał produkcyjnie przed commitem 💪
# ************************************************************************************************************
shopping = ["chleb", "masło", "mleko", "cola", "chipsy"]
while True:
    print("=== LISTA ZAKUPÓW ===")
    print()
    print("1 - Pokaż listę zakupów")
    print()
    print("2 - Dodaj produkt")
    print()
    print("3 - Usuń produkt")
    print()
    print("4 - Zakończ program")
    choice=int(input("wybierz cyfrę: "))
    if choice==1:
        for i, prod in enumerate(shopping,start=1):
            print(f"{i}. {prod}")
    elif choice==2:
        newprod=input("Podaj nazwę produktu do dodania: ")
        shopping.append(newprod)
        print(f"Produkt {newprod} został dodany do koszyka.")
    elif choice==3:
        remover = int(input("Podaj numer przedmiotu do usunięcia z koszyka: "))
        removed_item=shopping.pop(remover-1)
        print(f"Pomyślnie usunięto produkt {removed_item}!")
    elif choice==4:
        print("Do zobaczenia!")
        break
    else:
        print("Niepoprawny wybór. Spróbuj ponownie.")
