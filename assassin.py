from hero import Hero
import random

class Assassin(Hero):
    def __init__(self, name="assassin", health=150000, power=6, armor=0, evasion=0, ability="15 percent chance for a sneak attack that deals 100 damage", items={}, coins=0):
        super().__init__(name, health, power, armor, evasion, ability, items, coins)

    def attack(self):
        answer = int(input("""
        Would you like to try a sneak attack?
        1. yes
        2. no
        choice >>> """))
        if answer == 1:
            chance = random.random() * 100
            if chance < 15:
                return 100
            else:
                print("you were caught! no damage dealt")
                return 0
        else:
            return self.power
