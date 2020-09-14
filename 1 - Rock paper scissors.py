import random
import time

print("Welcome to Rock Paper and Scissors by Logic Decode")
playername = input("Enter your name: ")

playerscore = 0
computerscore = 0

max_score = int(input('Enter Max Score: '))

option = ["Rock", "Paper", "Scissors"]

while playerscore != max_score and computerscore != max_score:
    print(playername,"Score:", playerscore, "\tComputer Score:",computerscore)
    playerinput = input("Rock, Paper or Scissors? ")
    computerinput = random.choice(option)
    print("ROCK!")
    time.sleep(0.5)
    print("PAPER!")
    time.sleep(0.5)
    print("SCISSORS!")
    time.sleep(0.5)
    print("Computer Choice =>",computerinput)
    if playerinput.lower() == computerinput.lower():
        print("TIE!")
    elif playerinput.lower() == "rock":
        if computerinput.lower() == "paper":
            computerscore += 1
            print("You Lost!", computerinput, "Cover", playerinput)
        else:
            playerscore += 1
            print("You Won!", playerinput, "Smashes", computerinput)
    elif playerinput.lower() == "paper":
        if computerinput.lower() == "scissor":
            computerscore += 1
            print("You Lost!", computerinput, "Cut", playerinput)
        else:
            playerscore += 1
            print("You Won!", playerinput, "Covers", computerinput)
    elif playerinput.lower() == "scissors":
        if computerinput.lower() == "rock":
            computerscore += 1
            print("You Lost!", computerinput, "Smashes", playerinput)
        else:
            playerscore += 1
            print("You Won!", playerinput, "Cut", computerinput)
    else:
        print("Wrong Input, Check your spelling")
    print("-----------------------------------------------")

if playerscore == max_score:
    print("YEAH!", playername, "Won the Game!")
else:
    print("OOPS!", playername, "Lost the Game!")
