from hero import Hero
import random

class Paladin(Hero):
    def __init__(self, name="paladin", health=1000000, power=5, armor=2, evasion=0, ability="10 percent chance of double damage", items={}, coins=10):
        super().__init__(name, health, power, armor, evasion, ability, items, coins)

    def attack(self):
        if random.random() * 100 < 10:
            return self.power * 2
        else:
            return self.power