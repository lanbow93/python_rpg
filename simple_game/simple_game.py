from game_classes import Being

weapons = {"sword": 1, "mace": 3, "broadsword": 5, "wand": 1, "grimoire": 3, "staff": 5, "bow": 1, "dagger": 3, "poisoned dagger": 5, "ooze": 1, "claws": 5, "fire": 5}
creature = {"warrior": ("sword", "chainmail", 20), "wizard": ("wand", "novice robe", 10), "rouge": ("bow", "cloak", 15),"slime": ("ooze", "goo", 5 ), "wolf": ("fur", "claws", 15 ), "dragon": ("scales", "fire breath", 30 )
}


def gameplay(user):
    print(f"Currently your weapon is a {user.weapon} and your armour is {user.armor}")

def character_creation(name):
    print("Choose your starter class:\n\n1. Warrior, 2. Wizard, 3. Rouge")
    user_input = input("Enter Selection: ")
    if (user_input == "1"):
        user = Being(name, "warrior")
        print(f"Welcome to the adventure, ${name}")
        gameplay(user)
    elif (user_input == "2"):
        user = Being(name, "wizard")
        print(f"Welcome to the adventure, ${name}")
        gameplay(user)
    elif ( user_input == "3"):
        user = Being(name, "rouge")
        print(f"Welcome to the adventure, ${name}")
        gameplay(user)
    else:
        input("Selection you have chosen was invalid.\nPress enter to continue\n")
        character_creation(name)
    


def start_game():
    print("Welcome to the Basic RPG Game\n\nChoose one of the options below\n1. Start Game\n2. End Game")
    user_input = input("Enter Selection: ")
    if (user_input == "1"):
        user_name = input("Enter Character Name: ")
        character_creation(user_name)
    elif (user_input == "2"):
        print("Thank you for playing")
    else:
        input("Selection you have chosen was invalid.\nPress enter to continue\n")
        start_game()



start_game()
    
