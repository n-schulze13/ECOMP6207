# create a game part 1
import random

def main():
    print("Welcome to the beautiful coastline! With many beaches and cliffsides, there are many roads to travel. Where will you go?")
    print("*************************************************************************************************************************")
    fromStart()

def fromStart():
    choice = input("You are currently standing at an intersection overlooking the vast landscape of earth and sea in front of you. Where would you like to go - (L)eft or (R)ight?")
    if choice.lower() == "l":
        leftPath()
    elif choice.lower() == "r":
        rightPath()

def leftPath():
    beach = ["The sand is soft underfoot and the smell of the ocean fills your nose.", "Gulls cry in the air as they drift along the skyline.", "Small fishing boats bob in the distance as the tide rolls in and out."]   
    print("To the left we go!")
    print("As you crest the small hilltop to your left, you are greeted by the sights and sounds of the sea before you. There is a path that continues down to the beach and a path that curves back toward where you can from.")
    x = input("Would you like to go to the (B)each or back to the (S)tart?")
    if x.lower() == "b":
        print("As you approach the sandy shores, a warm sunrise peeks above the far-off horizon.")
        y = input("Would you like to (S)tay here a while or head (H)ome?")
        while y.lower() == "s":
            print(random.choice(beach))
            y = input("Would you like to (S)tay or head (H)ome?")
        if y.lower() == "h":
            print("With the morning sun warm on your back, you return home to go about your day")
            endGame()
    elif x.lower() == "s":
        fromStart()

def rightPath():
    cliff = ["1", "2", "3"]
    print("To the right we go!")
    print("Hiking up the path toward the cliffside, you are rewarded with an unbroken view of the misty skyline with wispy clouds rolling by.")
    choice = input("Would you like to continue toward the (C)liffs or go back to the (S)tart?")
    if choice.lower() == "c":
        print("As you reach the cliffs, a comforting breeze embraces you alongside an unmatched vista of the sunrise reflecting on the ocean below.")
        c = input("Would you like to (S)tay here a while or head (H)ome?")
        while c.lower() == "s":
            print(random.choice(cliff))
            #print a string. Re-ask question, print random new string.
        if c.lower() == "h":
            print("Spurred on by the breeze and fresh ocean air, you return home to go about your day")
            endGame()
    elif choice.lower() == "s":
        fromStart()


def endGame():
    print("Thank you for playing my little adventure game! Have a wonderful day.")

if __name__ == "__main__":
    main()