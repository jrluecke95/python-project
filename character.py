import random

class Character:
    def __init__(self, name, health, power, armor, evasion):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        self.evasion = evasion

    # def attack(self):
    #     return self.power

    # use item function?

    def check_status(self):
        print(f"{self.name} has {self.health}")

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def take_damage(self, enemy):
        if random.random() * 100 < self.evasion:
            net_damage = enemy.power - self.armor
            self.health -= net_damage
            print(f"{self.name} took {net_damage} from {enemy.name}")
        else:
            print(f"{self.name} dodged {enemy.name}'s attack!")

    # def helper_item(self, attribute):
    #     self.attribute += somehow get th amount of attribute?