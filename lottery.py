import random

guess = int(input("Give a number(0-9): "))
system = random.randint(0,9)
game = 'yes'
while game[0] == 'y':
    print(f"You guessed,{guess}, and the system generated, {system}")
    if guess == system:
        print("Winner!")
    elif guess != system:
        print("You lose!")
        print("Try again")
        game = input("Another game?(type y or n)")
    else:
        game == 'n'
    

