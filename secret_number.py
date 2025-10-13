secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
user_input = int(input("Enter your guess: "))
while user_input != secret_number:
    print("Nope. Try again!")
    user_input = int(input("Enter your guess: "))
print("Well done, muggle! You are free now.")
 