import random

random_number = random.randint(1,10)
guess = ""

while guess != random_number:

    guess = input("Pick a number from 1 to 10: ")
    guess = int(guess)  

    if guess == random_number:
        print("You got it!")
    elif guess < random_number:
        print("Too low")
    else:
        print("Too high")
        
print(random_number)