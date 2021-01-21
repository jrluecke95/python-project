from hero import Hero
import random

class Assassin(Hero):
    def __init__(self, name="assassin", health=15, power=6, armor=0, evasion=0, ability="15 percent chance for an instant kill", items=[], wand_charge=5):
        super().__init__(name, health, power, armor, evasion, ability, items)
        self.wand_charge = 5

    def attack(self, enemy):
        answer = int(input("""
        Would you like to try a sneak attack?
        1. yes
        2. no"""))
        if answer == 1:
            chance = random.random * 100
            if chance < 15:
                enemy.health = 0
            else:
                print("you were caught! no damage dealt")
        else:
            return self.power
