import random

user_wins = 0

options = ["heads","tails"]

while True:
    user_input = input("Types Heads/Tails or Q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,1)
    coin_flip = options[random_number]
    print("Computer picked: ", coin_flip)

    if user_input != coin_flip:
        print("Wrong!")

    elif user_input == coin_flip:
        print("Correct!")
        user_wins += 1

print("You won", user_wins, "times.")
print("Goodbye!")
    

