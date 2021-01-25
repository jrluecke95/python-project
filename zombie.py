from character import Character
import random

class Zombie(Character):
    def __init__(self, name="zombie", health=1, power=3, armor=0, evasion=0, ability = "can only die form head shots", bounty=10):
        super().__init__(name, health, power, armor, evasion, ability)
        self.bounty = bounty
    
    def take_damage(self, enemy):
        chance = random.random() * 100
        if chance < 10:
            print(f"headshot! {self.name} is dead.")
            self.health = 0
        else:
            print("You need a headshot to kill this zombie!")