def heal(hero, amount):
    hero.health += amount

def damage(enemy, amount):
    enemy.health -= amount

def add_evasion(hero, amount):
    hero.evasion += amount

def add_armor(hero, amount):
    hero.armor += amount

# if item choice == said item in dictionary then exceute function that pairs with it with hero and key value of inner dictionary as parameters