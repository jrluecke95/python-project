from hero import Hero

class Wizard(Hero):
    def __init__(self, items={}, name="wizard", health=150000, power=6, armor=0, evasion=0, ability="a wand that does double damage when used", coins=0, wand_charge=5):
        super().__init__(items, name, health, power, armor, evasion, ability, coins)
        self.wand_charge = 5

    def attack(self):
        if self.wand_charge > 0:
            attack_style = int(input(f"""
            You have {self.wand_charge} wand charges left:
            1. use a wand charge
            2. regular attack"""))
            if attack_style == 1:
                self.wand_charge -= 1
                return self.power * 2
            else:
                return self.power
        else:
            return self.power