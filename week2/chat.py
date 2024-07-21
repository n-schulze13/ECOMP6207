# welcome user and get name
def main():
    name = input("Welcome to my chatbot! What is your name?")
    chat(name)

# what do they want to chat about?
def chat(name):
    while True:
        try:
            choice = input(f"Hello, {name}, great to meet you! What would you like to talk about? Choose s for sports, w for weather, or j for jokes!")
            if choice == "s":
                sports(name)
                break
            elif choice == "w":
                weather(name)
                break
            elif choice == "j":
                jokes(name)
                break
            elif choice == "cancel":
                print("Okay, see ya!")
                break
            else:
                print("Please enter an s, w, or j to continue or say 'cancel'")
        except TypeError:
            print("Please enter a letter!")

# sports
def sports(name):
    sport = input(f"I love sports! What is your favorite sport, {name}?")
    if sport.lower() == "soccer":
        print("Soccer is my favorite sport too!")
    else:
        print("That's awesome! Sports are a great passtime that keep you active too!")
    outro(name)
# weather
def weather(name):
    w = input(f"The weather always seems to raise some opinions. Do you prefer the cold or the warm, {name}?")
    if w.lower() == "cold":
        print("Oh wow, me too! People think I'm crazy...my processor just gets so warm sometimes that I need a bit of a chill!")
    else:
        print("Nice! I prefer the cold, but the warm is nice too!")
    outro(name)
# jokes
def jokes(name):
    joke = input(f"Hey {name}, Which joke do you want - 1 or 2?")
    if joke == "1":
        print("There are 10 types of pepole in this world. Those who understand binary, and those who don't.")
    elif joke == "2":
        print("What did the computer say when their friend asked if they were hungry? 'Oh, yea, I could have a byte.'")
    else:
        print("That wasn't a 1 or a 2! Here's an extra-special joke just for you: What did the spider do on the computer? He made a WEBsite!")
    outro(name)

# outro
def outro(name):
    print(f"Wow! It was great to chat with you, but I have to get going now. Feel free to chat again anytime, {name}!")

if __name__ == "__main__":
    main()