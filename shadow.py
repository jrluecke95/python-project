from character import Character
import random

class Shadow(Character):
    def __init__(self, name="shadow", health=10, power=3, armor=0, evasion=80, ability = "has a 60 percent evasion chance", bounty=10):
        super().__init__(name, health, power, armor, evasion, ability)
        self.bounty = bounty