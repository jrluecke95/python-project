from character import Character

class Hero(Character):
    def __init__(self, name, health, power, armor, evasion, ability, items=[], coins=0):
        super().__init__(name, health, power, armor, evasion, ability)
        self.items = items
        self.coins = coins

    def get_item(self, item):
        self.items.append(item)

    