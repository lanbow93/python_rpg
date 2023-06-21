from game_classes import Being

user = Being("Lance", "wizard")

print(f"Name: {user.get_name()}\nHealth: {user.get_health()}\nWeapon: {user.get_weapon()}\nArmor: {user.get_armor()}")

running = True

while (running):
    print("Welcome to the Basic RPG Game\n\nChoose one of the options below\n1. Start Game\n2. End Game")
    user_input = input("Enter Selection: ")
    if (user_input == "1"):
        print("Game Has started")
        running = False
    elif (user_input == "2"):
        print("Thank you for playing")
        running = False
    else:
        input("Selection you have chosen was invalid.\nPress enter to continue\n")
