from random import randint

print("rock...")
print("paper...")
print("scissors...")

player1 = input("Player, make your move: ")

rand_num = randint(0,2)
if rand_num == 0: 
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"

print(f"Computer plays: {computer}")

if player1 == computer:
    print("Its a tie")

elif player1 == "rock":
    if computer == "scissors":
        print("player 1 wins")
    elif computer == "paper":
        print("computer wins")

elif player1 == "paper":
    if computer == "scissors":
        print("computer wins")
    elif computer == "rock":
        print("player 1 wins")

elif player1 == "scissors":
    if computer == "paper":
        print("player 1 wins")
    elif computer == "rock":
        print("computer wins")

else:
    print("Please enter valid move")