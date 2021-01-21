from character import Character
import random

class Dragon(Character):
    def __init__(self, name="dragon", health=40, power=5, armor=3, evasion=0, ability = "he's a dragon - that's all that needs to be said"):
        super().__init__(name, health, power, armor, evasion, ability)

    def attack(self):
        chance = random.random() * 100
        if chance < 10:
            print(f"{self.name} swooped down and bit your arm off! that's gotta hurt")
            return int(self.power * 4)
        elif 10 <= chance < 30:
            print(f"{self.name} breathed fire on you from his perch - only a light singe")
            return int(self.power)
        else:
            print(f"{self.name} circles above biding his time until the next attack") 
            return 0
