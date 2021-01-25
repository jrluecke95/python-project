from hero import Hero
import random

class Paladin(Hero):
    def __init__(self, items={}, name="paladin", health=1000000, power=5, armor=2, evasion=0, ability="10 percent chance of double damage", coins=10):
        super().__init__(items, name, health, power, armor, evasion, ability, coins)

    def attack(self):
        if random.random() * 100 < 10:
            return self.power * 2
        else:
            return self.power