import random

while True:
    rnd = random.randint(1, 101)
    tries = 0

    while True:
        user_num = int(input("Please enter a number between 1-100: "))
        tries += 1
        if user_num > rnd:
            print("Your number is too big...")
        elif user_num < rnd:
            print("Your number is too small...")
        else:
            print("BINGO")
            print(f"Amount of tries: {tries}")
            break

    restart = input("Would you like to play again? (yes/no): ")
    if restart.lower() == 'yes':
        continue
    else:
        print("Thanks for playing!")
        break
