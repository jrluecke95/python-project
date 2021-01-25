items = {"healing potion": {"effect type": "heal", "effect amount": 5, "quantity": 1, "cost": 5}, "poision potion": {"effect type": "damage", "effect amount": 5, "quantity": 1, "cost": 5}, "bow and arrow": {"effect type": "damage", "effect amount": 5, "quantity": 1, "cost": 10}, "piece of armor": {"effect type": "add armor", "effect amount": 5, "quantity": 1, "cost": 3}, "smoke screen": {"effect type": "add evasion", "effect amount": 5, "quantity": 1, "cost": 5}}

for item in items:
    print(items[item]['quantity'])