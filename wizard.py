from hero import Hero

class Wizard(Hero):
    def __init__(self, name="wizard", health=15, power=6, armor=0, evasion=0, ability="a wand that has 5 charges that do double damage", items=[], wand_charge=5):
        super().__init__(name, health, power, armor, evasion, ability, items)
        self.wand_charge = 5

    def attack(self):
        if self.wand_charge > 0:
            attack_style = int(input(f"""
            You have {self.wand_charge} wand charges left:
            1. use a wand charge
            2. regular attack"""))
            if attack_style == 1:
                return self.power * 2
            else:
                return self.power
        else:
            return self.power