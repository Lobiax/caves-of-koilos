health = 100
weapon = False


def start_game():
    """
    Starts the game and prompts the user to type their adventurer's name.
    """
    adventurer = input("Please tell us the name of your adventurer")
    print(f"Greetings {adventurer}, many dangers await you in these caves.\n")
    print("Please proceed with caution")
    choose_path()


def choose_path():
    print("Choose the way forward\n")
    print("There are three doors in front of you. Left, middle and right\n")
    print("Use the left, up and right keys to choose between the doors")
    