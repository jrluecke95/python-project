import random

class Character:
    def __init__(self, name, health, power, armor, evasion, ability):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        self.evasion = evasion
        self.ability = ability

    # def attack(self):
    #     return self.power

    # use item function?

    def check_status(self):
        return(f"{self.name} has {self.health} health, {self.power} power, {self.armor} armor, {self.evasion} evasion and has {self.ability}.")

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self):
        return self.power

    def take_damage(self, enemy):
        if random.random() * 100 < self.evasion - 1:
            print(f"{self.name} dodged {enemy.name}'s attack!")
        else:
            net_damage = enemy.attack() - self.armor
            self.health -= net_damage
            print(f"{self.name} took {net_damage} from {enemy.name}")

    # def helper_item(self, attribute):
    #     self.attribute += somehow get th amount of attribute?