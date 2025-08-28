user_word = input("Podaj słowo: ")

vowels = "AEIOUYaeiouy"

for letter in user_word:
    if letter in vowels:
        continue
    word_without_vowels=""
    print(letter, end="")
    print(word_without_vowels, end="")
    word_without_vowels= word_without_vowels + letter