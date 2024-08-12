# dice game
import random
import time

# start game
def main():
    diceSides = input("How many sides per die?: ")
    diceSides = int(diceSides)
    number_dice = input("Enter the number of dice: ")
    number_dice = int(number_dice)
    ready = input("Ready to start? Hit any key to continue. ")

    # user rolls
    user_rolls = roll_dice(number_dice, diceSides)
    print("First user roll: ", user_rolls)
    uChoice = input("Would you like to reroll? Enter - for each die you want to keep, and r for each that you want a reroll: ")
    while len(uChoice) < number_dice:
        print(f"You must enter {number_dice} choices")
        uChoice = input("Would you like to reroll? Enter - for each die you want to keep, and r for each that you want a reroll: ")
    for i in range(len(uChoice)):
        if uChoice[i] == "r":
            reroll(uChoice, user_rolls, diceSides)
    print("New user rolls: ", user_rolls)
 

    # computer rolls
    print("Computers turn!")
    computer_rolls = roll_dice(number_dice, diceSides)
    print ("Computer first roll: ", computer_rolls)
    cChoice = compStrat2(number_dice, computer_rolls, diceSides)
    print("Computer Choice: ", cChoice)
    reroll(cChoice, computer_rolls, diceSides)
    print("New computer rolls: ", computer_rolls)

    find_winner(computer_rolls, user_rolls)


# dice roller
def roll_dice(n, sides):
    dice = []
    for i in range(n):
        dice.append(random.randint(1,sides))
    return dice

# reroll
def reroll(choice, dice, sides):
    print("Rerolling...please hold...")
    time.sleep(random.randint(2,5))
    for i in range(len(choice)):
        if choice[i] == "r":
            dice[i] = random.randint(1,sides)

# find winner
def find_winner(cdice_list, udice_list):
    cTotal = sum(cdice_list)
    uTotal = sum(udice_list)
    print("Computer total: ", cTotal)
    print("User total: ", uTotal)
    if uTotal > cTotal:
        print("User wins")
    elif cTotal > uTotal:
        print("Computer wins")
    else:
        print("Tie game")

# simple computer strategy
def compStrat1(n):
    print("Computer is thinking...")
    time.sleep(random.randint(2,5))
    choices = ""
    for i in range(n):
        choices = choices + "r"
    return choices

# advanced computer strategy
def compStrat2(n, cRolls, sides):
    print("Computer is thinking...")
    time.sleep(random.randint(2,5))
    choices = ""
    for i in range(n):
        if cRolls[i] < (.5*sides):
            choices = choices + "r"
        else:
            choices = choices + "-"
    return choices

if __name__ == "__main__":
    main()