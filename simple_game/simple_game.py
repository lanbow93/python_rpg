from game_classes import Human, Monster

# Weapon name, attack value
weapons = {"sword": 1, "mace": 3, "broadsword": 5, "wand": 1, "grimoire": 3, "staff": 5, "bow": 1, "dagger": 3, "poisoned dagger": 5, "ooze": 1, "claws": 5, "fire": 5}
#armor name, defense value
armor_defense = {"chainmail": 1, "metal plating": 2, "diamond armor": 3, "novice robe": 1, "apprentice robe": 2, "master robe": 3, "cloak": 1, "veil of mystery": 2, "reaper's robe": 3, "goo": 1, "fur": 2, "scales": 3 }
# Inital starting stats and equipment Class: (Weapon, Armor, Health)
creature = {"warrior": ("sword", "chainmail", 20), "wizard": ("wand", "novice robe", 10), "rouge": ("bow", "cloak", 15),"slime": ("ooze", "goo", 5 ), "wolf": ("fur", "claws", 15 ), "dragon": ("scales", "fire breath", 30 )
}
#20 random monster names to choose from
monster_proper_nouns = ["Drakonis", "Morbos", "Zephyrion", "Nyxar", "Xalos", "Vexalor", "Gloomfang", "Zaroth", "Vorgrath", "Lunaris", "Azgul", "Rendragor", "Sylvaris", "Zoltan", "Necronyx", "Frostbite", "Dreadmaw", "Venomshade", "Shadowclaw", "Ragnarok"]


def gameplay(user):
    print(f"Currently your weapon is a {user.weapon} and your armour is {user.armor}")

def character_creation(name):
    print("Choose your starter class:\n\n1. Warrior, 2. Wizard, 3. Rouge")
    user_input = input("Enter Selection: ")
    if (user_input == "1"):
        user = Human(name, "warrior")
        print(f"Welcome to the adventure, ${name}")
        gameplay(user)
    elif (user_input == "2"):
        user = Human(name, "wizard")
        print(f"Welcome to the adventure, ${name}")
        gameplay(user)
    elif ( user_input == "3"):
        user = Human(name, "rouge")
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
    
