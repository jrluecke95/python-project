from character import Character

class Hero(Character):
    def __init__(self, name, health, power, armor, evasion, ability, items=[]):
        super().__init__(name, health, power, armor, evasion, ability)
        self.items = items

    