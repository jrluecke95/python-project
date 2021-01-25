from hero import Hero
from paladin import Paladin
from wizard import Wizard
from assassin import Assassin
from use_item import use_item
from dragon import Dragon

def fight_dragon(hero_choice):
    hero = hero_choice
    dragon = Dragon()
    print("""
    
    You defeated all of the enemies.
    You step outisde to get a breath of fresh air...
    You hear a distant noise and then BOOM!!!!!
    A dragon lands in front of you and lets out a roar")
    
    Running is futile - you have no choice except to stand and fight""")
    while hero.is_alive() == True and dragon.is_alive() == True:
        try:
            use_item_choice = int(input("""
Do you want to check your inventory?
1. yes
2. no

choice >>> """))
            if use_item_choice == 1:
                hero.print_inventory()
                item_effect = use_item(hero, dragon)
                if item_effect == 0:
                    print("no item was used... against a dragon.")
                dragon.take_damage(hero)
                hero.take_damage(dragon)
                break
            elif use_item_choice == 2:
                dragon.take_damage(hero)
                hero.take_damage(dragon)
            else:
                raise ValueError
        except ValueError:
            print("sorry that wasn't a valid selection!")
        if dragon.is_alive() == False:
            print("You did it! you slayed all everyone in this area! the villagers thank you.")
            break
        if hero.is_alive() == False:
            print("you died:/")
            break