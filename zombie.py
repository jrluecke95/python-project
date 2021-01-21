from character import Character
import random

class Zombie(Character):
    def __init__(self, name, health, power, armor, evasion, ability = "can only die from a headshot"):
        super().__init__(name, health, power, armor, evasion, ability)
    
    def take_damage(self):
        chance = random.random * 100
        if chance < 10:
            self.health = 0