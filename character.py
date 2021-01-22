import random

class Character:
    def __init__(self, name="", health=0, power=0, armor=0, evasion=0, ability=""):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        self.evasion = evasion
        self.ability = ability

    def check_status(self):
        return(f"{self.name} has {self.health} health, {self.power} power, {self.armor} armor, {self.evasion} evasion and has {self.ability}.")

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self):
        return int(self.power)

    def take_damage(self, enemy):
        if random.random() * 100 < self.evasion - 1:
            print(f"{self.name} dodged {enemy.name}'s attack!")
        else:
            net_damage = (enemy.attack() - int(self.armor))
            if net_damage > 0:
                self.health -= net_damage
                print(f"{self.name} took {net_damage} from {enemy.name}")
            else:
                print(f"{enemy.name} did no damage to {self.name} this attack")