from character import Character

class Hero(Character):
    def __init__(self, items={}, name="", health=0, power=0, armor=0, evasion=0, ability="", coins=0):
        super().__init__(name, health, power, armor, evasion, ability)
        self.items = {"healing potion": {"effect type": "heal", "effect amount": 5, "quantity": 1, "cost": 5}, "poision potion": {"effect type": "damage", "effect amount": 5, "quantity": 1, "cost": 5}, "bow and arrow": {"effect type": "damage", "effect amount": 5, "quantity": 1, "cost": 10}, "piece of armor": {"effect type": "add armor", "effect amount": 5, "quantity": 1, "cost": 3}, "smoke screen": {"effect type": "add evasion", "effect amount": 5, "quantity": 1, "cost": 5}}
        self.coins = coins

    def print_inventory(self):
        for item in self.items:
            print(f"You have {self.items[item]['quantity']} {item}'s")
    
    def full_stats(self):
        return(f"{self.name} has {self.health} health, {self.power} power, {self.armor} armor, {self.evasion} evasion, {self.coins} coins, and has {self.ability}.")

    def get_item(self, item):
        item_choice = self.items[item]
        if item == ('bow and arrow'):
            item_choice["quantity"] += 5
        else:
            item_choice["quantity"] += 1
    
    def use_item(self, item):
        item_choice = self.items[item]
        item_choice["quantity"] -= 1
        return item_choice["effect amount"]