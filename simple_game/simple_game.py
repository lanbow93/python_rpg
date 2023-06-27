from game_classes import Human, Monster
import random
import os

#20 random monster names to choose from
monster_proper_nouns = ["Drakonis", "Morbos", "Zephyrion", "Nyxar", "Xalos", "Vexalor", "Gloomfang", "Zaroth", "Vorgrath", "Lunaris", "Azgul", "Rendragor", "Sylvaris", "Zoltan", "Necronyx", "Frostbite", "Dreadmaw", "Venomshade", "Shadowclaw", "Ragnarok"]

# Inital starting stats and equipment Class: (Weapon, Armor, Health)
creature = {"warrior": ("sword", "chainmail", 20), "wizard": ("wand", "novice robe", 10), "rouge": ("bow", "cloak", 15),"slime": ("ooze", "goo", 5 ), "wolf": ("fur", "claws", 15 ), "dragon": ("scales", "fire breath", 30 )
}

# Weapon name, attack value
weapons = {"sword": 1, "mace": 3, "broadsword": 5, "wand": 1, "grimoire": 3, "staff": 5, "bow": 1, "dagger": 3, "poisoned dagger": 5, "ooze": 1, "claws": 5, "fire": 5}
#armor name, defense value
armors = {"chainmail": 1, "metal plating": 2, "diamond armor": 3, "novice robe": 1, "apprentice robe": 2, "master robe": 3, "cloak": 1, "veil of mystery": 2, "reaper's robe": 3, "goo": 1, "fur": 2, "scales": 3 }
potions = {"lesser health potion": 10, "greater health potion": 20}

shop_weapons = {"warrior": ["mace", 10, "broadsword", 20], "wizard": ["grimoire", 10, "staff", 20], "rouge": ["dagger", 10, "poisoned dagger", 20]}
shop_armors = {"warrior": ["metal plating", 10, "diamond armor", 20], "wizard": ["apprentice robe", 10, "master robe", 20], "rouge":["veil of mystery", 10, "reaper's robe", 20]}
shop_potions = {"warrior": ["lesser health potion", 10, "greater health potion", 20], "wizard": ["lesser health potion", 10, "greater health potion", 20], "rouge":["lesser health potion", 10, "greater health potion", 20]}

def attempt_item_purchase(selection, user, item_type):
    user_class = user.being_class
    if(item_type == "weapon"):
        selection_index = shop_weapons[user_class].index(selection)
        weapon = shop_weapons[user.being_class][selection_index]
        price = shop_weapons[user.being_class][selection_index + 1]
        if (price > user.get_gold()):
            os.system("clear")
            input("You do not have enough gold for this purchase.\nPress enter to continue\n")
            shop(user)
        else:
            os.system("clear")
            user.change_gold((-1 * price))
            user.set_weapon(weapon)
            user.change_inventory("add", weapon)
            print(user.get_inventory())
            input(f"You have purchased the {weapon}.\nRemaining Balance: {user.get_gold()}\nPress enter to continue\n")
            # Removing the weapons from shop availability
            shop_weapons[user.being_class].pop(selection_index + 1)
            shop_weapons[user.being_class].pop(selection_index)
            gameplay(user)
    elif(item_type == "armor"):
            selection_index = shop_armors[user_class].index(selection)
            armor = shop_armors[user.being_class][selection_index]
            price = shop_armors[user.being_class][selection_index + 1]
            if (price > user.get_gold()):
                os.system("clear")
                input("You do not have enough gold for this purchase.\nPress enter to continue\n")
                shop(user)
            else:
                os.system("clear")
                user.change_gold((-1 * price))
                user.set_armor(armor)
                user.change_inventory("add", armor)
                input(f"You have purchased the {armor}.\nRemaining Balance: {user.get_gold()}\nPress enter to continue\n")
                # Removing the armors from shop availability
                shop_armors[user.being_class].pop(selection_index + 1)
                shop_armors[user.being_class].pop(selection_index)
                gameplay(user)
    elif(item_type == "potions"):
        selection_index = shop_potions[user_class].index(selection)
        potion = shop_potions[user.being_class][selection_index]
        price = shop_potions[user.being_class][selection_index + 1]
        # Gold validation statement
        if (price > user.get_gold()):
            os.system("clear")
            input("You do not have enough gold for this purchase.\nPress enter to continue\n")
            shop(user)
        else:
            os.system("clear")
            user.change_gold((-1 * price))
            user.change_inventory("add", potion)
            input(f"You have purchased the {potion}.\nRemaining Balance: {user.get_gold()}\nPress enter to continue\n")
            gameplay(user)

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

def inventory_selection(user, item):
    # If item is a weapon
    if item in weapons.keys():
        print(f"Weapon Selected: {item}")
    # If item is armor
    if item in armors.keys():
        print(f"Armor Selected: {item}")
    # If item is a potion
    if item in potions.keys():
        user_health = user.get_health()
        base_health = creature[user.being_class][2]
        restore_amount = potions[item]
        if(user_health == base_health):
            print("Health is at full. Stop being greedy")
            view_inventory(user)
        elif(user_health + restore_amount  > base_health):
            user.change_health(base_health-user_health)
            print(user.get_health())
            print("Health has been restored to full")
            view_inventory(user)
        else:
            user.change_health(restore_amount)
            print(user.get_health())
            print(f"Health has been restored to {user.get_health()}")
            view_inventory(user)

    else:
        print("You didn't select a listed item")
    
def view_inventory(user):
    inventory = user.get_inventory()
    list_count = 1
    print("Q. Quit")
    for item in inventory:
        print(f"{list_count}. {item.upper()}")
        list_count += 1
    user_selection = input("Enter Selection: ")
    if(user_selection == "Q" or user_selection == "q"):
        gameplay(user)
    if(user_selection.isdigit() and int(user_selection) <= len(inventory)):
        inventory_selection(user, inventory[int(user_selection) - 1])
    else:
        input("Selection you have chosen was invalid.\nPress enter to continue\n")
        view_inventory(user)
        
def shop(user):
    os.system("clear")
    print("Shop\n1. Weapon\n2. Armor\n3. Potion\n4. Exit")
    user_selection = input("Enter Selection: ")
    if (user_selection == "1"):
        os.system("clear")
        print("Weapon Options:\n")
        list_count = 1
        weapon_selection = []
        #Iterate through weapons and list in shop
        for i in range(0,len(shop_weapons[user.being_class]),2):
            print(f"{list_count}. {shop_weapons[user.being_class][i+1]} Gold - {shop_weapons[user.being_class][i].upper()}")
            list_count += 1
            weapon_selection.append(shop_weapons[user.being_class][i])
        print(weapon_selection)
        attempt_item_purchase(weapon_selection[int(input("\nEnter Selection: "))-1], user, "weapon")
    elif (user_selection == "2"):
        os.system("clear")
        print("Armor Options:\n")
        list_count = 1
        armor_selection = []
        #Iterate through armors and list in shop
        for i in range(0,len(shop_armors[user.being_class]),2):
            print(f"{list_count}. {shop_armors[user.being_class][i+1]} Gold - {shop_armors[user.being_class][i].upper()}")
            list_count += 1
            armor_selection.append(shop_armors[user.being_class][i])
        print(armor_selection)
        attempt_item_purchase(armor_selection[int(input("\nEnter Selection: "))-1], user, "armor")
    elif (user_selection == "3"):
        os.system("clear")
        print("Potion Options:\n")
        list_count = 1
        potions_selection = []
        # Iterate through potions and list in shop. 
        for i in range(0,len(shop_potions[user.being_class]),2):
            print(f"{list_count}. {shop_potions[user.being_class][i+1]} Gold - {shop_potions[user.being_class][i].upper()}")
            list_count += 1
            potions_selection.append(shop_potions[user.being_class][i])
        print(potions_selection)
        attempt_item_purchase(potions_selection[int(input("\nEnter Selection: "))-1], user, "potions")
    elif (user_selection == "4"):
        gameplay(user)
    else:
        os.system("clear")
        input("Selection you have chosen was invalid.\nPress enter to continue\n")
        shop(user)

def gameplay(user):
    os.system("clear")
    print(f"Weapon: {user.get_weapon().upper()} | Armor: {user.get_armor().upper()} | Money: {user.get_gold()} | Health: {user.get_health()}\n")
    print(
'''~~Main Menu~~
1. Go Fight
2. Shop
3. View Inventory
4. Quit
    ''')
    user_selection = input("Enter Selection: ")
    if (user_selection == "1"):
        fight(user)
    elif (user_selection == "2"):
        shop(user)
    elif (user_selection == "3"):
        view_inventory(user)
    elif (user_selection == "4"):
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
    
