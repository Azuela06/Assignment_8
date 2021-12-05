import random

user = input("What is your name user number 1?: ")
print(f"Hello, welcome to another guessing game {user}")

computer = random.randint(0,100)
Start = True
while Start:
    Guess = int(input("Guess a number from 0-100: "))
    if Guess == computer:
        print ("Congratulations! You have guessed it correctly")
        break
    elif Guess > computer:
        print ("The number generated is lesser than that")
    else:
        Guess < computer
        print ("The number generated is greater than that")