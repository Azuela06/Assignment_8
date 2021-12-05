import random

computer = random.randint(0,100)
Start = True
while Start:
    Guess = int(input("Guess a number from 0-100: "))
    print(f"{Guess}, {computer}")
    if Guess == computer:
        print ("Congratulations! You have guessed it correctly")
        break
    elif Guess > computer:
        print ("The number generated is lower than that")
    else:
        Guess < computer
        print ("The number generated is greater than that")