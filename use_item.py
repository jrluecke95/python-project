from hero import Hero
from paladin import Paladin
from item_fucntions import heal
from item_fucntions import damage
from item_fucntions import add_armor
from item_fucntions import add_evasion

def use_item(hero_choice, enemy_choice):
    hero = hero_choice
    enemy = enemy_choice
    while True:
        try:
            use_item_choice = int(input("""
            Would you like to use an item this attack?
            1. yes
            2. no - this enemy seems like a chump
            choice >>> """))
            if use_item_choice == 1:
                print("Which item would you like to use?")
                while True:
                    try:
                        item_names = list(hero.items.keys())
                        counter = 1
                        for item in item_names:
                            print(f"{counter}: You have {hero.items[item]['quantity']} {item}'s")
                            counter += 1
                        which_item = int(input("choice >>> ")) - 1
                        if which_item in range(len(item_names)):
                            item_name = item_names[which_item]
                            if hero.items[item_name]['quantity'] > 0:
                                if hero.items[item_name]["effect type"] == 'heal':
                                    heal(hero, hero.use_item(item_name))
                                    print(f"You used {item_name} and gained {hero.items[item_name]['effect amount']} of health")
                                    break
                                elif hero.items[item_name]["effect type"] == 'damage':
                                    damage(enemy, hero.use_item(item_name))
                                    print(f"You used {item_name} and did {hero.items[item_name]['effect amount']} extra damge")
                                    break
                                elif hero.items[item_name]["effect type"] == 'add armor':
                                    add_armor(hero, hero.use_item(item_name))
                                    print(f"You used {item_name} and gained {hero.items[item_name]['effect amount']} armor")
                                    break
                                elif hero.items[item_name]["effect type"] == 'add evasion':
                                    add_evasion(hero, hero.use_item(item_name))
                                    print(f"You used {item_name} and gained {hero.items[item_name]['effect amount']} evasion")
                                    break
                            else:
                                print("you don't have any of those!")
                                return 0
                        else:
                            raise ValueError
                    except ValueError:
                        print("sorry that wasn't a valid selection")
            elif use_item_choice == 2:
                print("really? no item? good luck... moron")
                return 0
            else:
                raise ValueError
        except ValueError:
            print("sorry that wasn't a valid selection")

