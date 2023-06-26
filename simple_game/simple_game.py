from game_classes import Human, Monster
import random
import os

# Weapon name, attack value
weapons = {"sword": 1, "mace": 3, "broadsword": 5, "wand": 1, "grimoire": 3, "staff": 5, "bow": 1, "dagger": 3, "poisoned dagger": 5, "ooze": 1, "claws": 5, "fire": 5}
#armor name, defense value
armor_defense = {"chainmail": 1, "metal plating": 2, "diamond armor": 3, "novice robe": 1, "apprentice robe": 2, "master robe": 3, "cloak": 1, "veil of mystery": 2, "reaper's robe": 3, "goo": 1, "fur": 2, "scales": 3 }
# Inital starting stats and equipment Class: (Weapon, Armor, Health)
creature = {"warrior": ("sword", "chainmail", 20), "wizard": ("wand", "novice robe", 10), "rouge": ("bow", "cloak", 15),"slime": ("ooze", "goo", 5 ), "wolf": ("fur", "claws", 15 ), "dragon": ("scales", "fire breath", 30 )
}
#20 random monster names to choose from
monster_proper_nouns = ["Drakonis", "Morbos", "Zephyrion", "Nyxar", "Xalos", "Vexalor", "Gloomfang", "Zaroth", "Vorgrath", "Lunaris", "Azgul", "Rendragor", "Sylvaris", "Zoltan", "Necronyx", "Frostbite", "Dreadmaw", "Venomshade", "Shadowclaw", "Ragnarok"]

shop_weapons = {"warrior": ["mace", 10, "broadsword", 20], "wizard": ["grimoire", 10, "staff", 20], "rouge": ["dagger", 10, "poisoned dagger", 20]}
shop_armor = {"warrior": ["metal plating", 10, "diamond armor", 20], "wizard": ["apprentice robe", 10, "master robe", 20], "rouge":["veil of mystery", 10, "reaper's robe", 20]}

def attempt_weapon_purchase(selection_index, user):
    weapon = shop_weapons[user.being_class][selection_index]
    price = shop_weapons[user.being_class][selection_index + 1]
    print(f"{weapon} costs ${price}")
def generate_enemy(user):
    monster_name = monster_proper_nouns[random.randint(0, len(monster_proper_nouns))]
    if(user.get_experience() < 10):
        return Monster(monster_name, "slime")
    elif(user.get_experience() < 20 and user.get_experience() >= 10):
        return Monster(monster_name, "wolf")
    elif(user.get_experience() >= 20):
        return Monster(monster_name, "dragon")

def fight(user):
    encounter = generate_enemy(user)
    print(f"You have encountered a {encounter.being_class} named {encounter.get_name}")
    user_selection = input(f"What will you do?\n 1. Attack  2. Run Away")

    if(user_selection == "1"):
        pass
    else:
        gameplay(user)


def shop(user):
    os.system("clear")
    print("Shop\n1. Weapon\n2. Armor\n3. Potion\n4. Exit")
    user_selection = input("Enter Selection: ")
    if (user_selection == "1"):
        os.system("clear")
        print("Weapon Options:\n")
        list_count = 1
        weapon_selection = []
        for i in range(0,len(shop_weapons[user.being_class]),2):
            print(f"{list_count}. {shop_weapons[user.being_class][i+1]} Gold - {shop_weapons[user.being_class][i].upper()}")
            list_count += 1
            weapon_selection.append(shop_weapons[user.being_class][i])
        print(weapon_selection)
        attempt_weapon_purchase(int(input("\nEnter Selection: "))-1, user)
    elif (user_selection == "2"):
        print("Armor:")
    elif (user_selection == "3"):
        print("Potions:")
    elif (user_selection == "4"):
        gameplay(user)
    else:
        os.system("clear")
        input("Selection you have chosen was invalid.\nPress enter to continue\n")
        shop(user)


def gameplay(user):
    os.system("clear")
    print(f"Currently your weapon is a {user.weapon} and your armour is {user.armor}\n")
    print(
'''~~Main Menu~~
1. Go Fight
2. Shop
3. Quit
    ''')
    user_selection = input("Enter Selection: ")
    if (user_selection == "1"):
        fight(user)
    elif (user_selection == "2"):
        shop(user)
    elif (user_selection == "3"):
        exit()
    else:
        input("Selection you have chosen was invalid.\nPress enter to continue\n")
        gameplay(user)

def character_creation(name):
    os.system("clear")
    print("Choose your starter class:\n\n1. Warrior 2. Wizard 3. Rouge")
    user_input = input("Enter Selection: ")
    if (user_input == "1"):
        user = Human(name, "warrior")
        print(f"Welcome to the adventure, {name}")
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
        os.system("clear")
        input("Selection you have chosen was invalid.\nPress enter to continue\n")
        character_creation(name)
    


def start_game():
    print("Welcome to the Basic RPG Game\n\nChoose one of the options below\n1. Start Game\n2. End Game")
    user_input = input("Enter Selection: ")
    os.system("clear")
    if (user_input == "1"):
        user_name = input("Enter Character Name: ")
        character_creation(user_name)
    elif (user_input == "2"):
        print("Thank you for playing")
    else:
        os.system("clear")
        input("Selection you have chosen was invalid.\nPress enter to continue\n")
        start_game()



start_game()
    
