from character import Character

class Goblin(Character):
    def __init__(self, name="goblin", health=5, power=2, armor=0, evasion=0, ability = "has honestly not much - this guy kinda sucks", bounty=5):
        super().__init__(name, health, power, armor, evasion, ability)
        self.bounty = bounty

goblin = Goblin()
print(type(goblin.armor))