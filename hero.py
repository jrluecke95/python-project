from character import Character

class Hero(Character):
    def __init__(self, items=[], name="", health=0, power=0, armor=0, evasion=0, ability=0, coins=0):
        super().__init__(name, health, power, armor, evasion, ability)
        self.items = [["healing potion", 5, 1], ["poison potion", -5, 0], ["bow and arrow", -5, 0]]
        self.coins = coins

    def get_item(self, item):
        item_choice = self.items[item]
        if item_choice == 2:
            item_choice[2] = 5
        else:
            item_choice[2] += 1
    
    def use_item(self, item):
        item_choice = self.items[item]
        item_choice[2] -= 1
        return item_choice[1]

    def print_inventory(self):
        for item in self.items:
            print(f"You have {item[2]} {item[0]}'s that provide {item[1]} hit points for your next task")
    
    def check_status(self):
        return(f"{self.name} has {self.health} health, {self.power} power, {self.armor} armor, {self.evasion} evasion, {self.coins} coins, and has {self.ability}.")
