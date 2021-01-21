from character import Character
import random

class Shadow(Character):
    def __init__(self, name="shadow", health=10, power=3, armor=0, evasion=60, ability = "has a 60 percent evasion chance"):
        super().__init__(name, health, power, armor, evasion, ability)