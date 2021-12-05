import random

name = input("Player, enter your name: ")
game = 'y'
while game[0] == 'y':
    guess1,guess2,guess3 = input("Give 3 numbers(0-9): ").split(',') #Put a comma each number fls.
    guess = int(guess1),int(guess2),int(guess3)
    system = random.randint(0,9),random.randint(0,9),random.randint(0,9)
    print(f"You guessed {guess}, and the system generated {system}")
    if guess == system:
        print("Winner!")
        game = input("Another game?(type y or n):")
    elif guess != system:
        print("You lose!")
        print(f"Try again, {name}")
        game = input("Another game?(type y or n):")
    else:
        game = input("Another game?(type y or n):")
        game == 'n'
        break  