creature = {"warrior": ("sword", "chainmail"), "wizard": ("wand", "robe"), "rouge": ("bow", "cloak"),"slime": ("ooze", "goo"), "wolf": ("fur", "claws"), "dragon": ("scales", "fire breath")
}

class Being():
    def __init__(self, name, being_class):
        self.name = name
        self.being_class = being_class
        print(type(getattr(creature, being_class)))
        self.weapon = getattr(creature, being_class)[0]
        self.armor = getattr(creature, being_class)[1]

    def get_name(self):
        return self.name
    
    def get_weapon(self):
        return self.weapon
    
    def get_armor(self):
        return self.armor
    
    def get_class(self):
        return self.being_class

user = Being("Lance", "wizard")

print(user.get_name(), user.get_weapon(), user.get_armor(), user.get_class())
