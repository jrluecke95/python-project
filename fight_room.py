from character import Character
from hero import Hero
from paladin import Paladin
from wizard import Wizard
from assassin import Assassin
from zombie import Zombie
from shadow import Shadow
from goblin import Goblin
from dragon import Dragon
from use_item import use_item

def fight_room(hero_choice, enemy_choice):
    hero = hero_choice
    enemy = enemy_choice
    print(f"You encounter a {enemy.name} in this room, what would you like to do?")
    print(enemy.full_stats())
    while hero.is_alive() == True:
        try:
            action_choice = int(input("""
1. Attack
2. Do Nothing
3. Flee

choice>>> """))
            if action_choice == 1:
                use_item(hero, enemy)
                enemy.take_damage(hero)
                hero.take_damage(enemy)
                print()
            elif action_choice == 2:
                hero.take_damage(enemy)
                print()
            elif action_choice == 3: 
                print("coward")
                return False
            else:
                raise ValueError
            print(hero.check_vitals())
            print(enemy.check_vitals())
        except ValueError:
            print("sorry! that wasn't a valid choice")
        if enemy.is_alive() == False:
            print(f"you did it! you killed the {enemy.name} and got {enemy.bounty} gold coins from its lifeless corpse")
            hero.coins += enemy.bounty
            return True
        if hero.is_alive() == False:
            print("you died:/")
            return False