# CreatureClass : Weapon, Armor, Health
creature = {"warrior": ("sword", "chainmail", 20), "wizard": ("wand", "novice robe", 10), "rouge": ("bow", "cloak", 15),"slime": ("ooze", "goo", 5 ), "wolf": ("fur", "claws", 15 ), "dragon": ("scales", "fire breath", 30 )
}

class Being():
    def __init__(self, name, being_class):
        self.name = name
        self.being_class = being_class
        self.weapon = creature[being_class][0]
        self.armor = creature[being_class][1]
        self.health = creature[being_class][2]

    def get_name(self):
        return self.name

    def get_class(self):
        return self.being_class
    
    def get_weapon(self):
        return self.weapon
    
    def set_weapon(self, chosen_weapon):
        self.weapon = chosen_weapon

    def get_armor(self):
        return self.armor
    
    def set_amror(self, chosen_armor):
        self.armor = chosen_armor

    def get_health(self):
        return self.health
    
    def change_health(self, amount):
        self.health += amount

class Human(Being):
    def __init__(self, name, being_class):
        super().__init__(name, being_class)
        self.experience = 0
        self.gold = 0
        

    
    def get_experience(self):
        return self.experience
    
    def change_experience(self, value):
        self.experience += value
    
    def get_gold(self):
        return self.gold
    
    def change_gold(self, value):
        self.gold += value


user = Human("Lance", "wizard")

