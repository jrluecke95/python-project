from hero import Hero
import random

class Assassin(Hero):
    def __init__(self, items={}, name="assassin", health=150000, power=6, armor=0, evasion=0, ability="15 percent chance for a sneak attack that deals 100 damage", coins=0):
        super().__init__(items, name, health, power, armor, evasion, ability, coins)

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

# class Hero(Character):
#     def __init__(self, items={"healing potion": {"health_impact": 5, "quantity": 1}, "poision potion": {"health impact": 5, "quantity": 0}, "bow and arrow": {"health_impact": 5, "quantity": 0}}, name="", health=0, power=0, armor=0, evasion=0, ability="", coins=0):
#         super().__init__(name, health, power, armor, evasion, ability)
#         self.items = items 
#         self.coins = coins

hero = Assassin()
# accessing names of items in list
# print(list(hero.items.keys())) 
item_names = list(hero.items.keys())


# accessing attribute of items in list
for item in item_names:
    print(hero.items[item].keys())

