from character import Character
from hero import Hero
from paladin import Paladin
from wizard import Wizard
from assassin import Assassin
from zombie import Zombie
from shadow import Shadow
from goblin import Goblin
from dragon import Dragon

# this will be the main menu

# make a character class for universal traits
# make a hero class for heroes
# make an enemy class for enemies
# weapons and items? 
# make a room class??


def main_menu():
    print("Welcome to the game! Which hero would you like to select? Each hero has it's own strengths and weaknesses, so choose wisely")
    answer = int(input("""
    1. Paladin
    2. Wizard
    3. Assassin
    choice >>> """))
    if answer == 1:
        hero = Paladin()
    if answer == 2:
        hero = Wizard()
    if answer == 3:
        hero = Assassin()
    print(f"Great choice! You have selected {hero.name}!")
    print(hero.check_status())
    print()
    print()

# begins the journey into the rooms
    rooms_list = ["A door covered in... brains?", "A door that has the silhouette of someone on it", "A door that has the outline of some tiny thing on it.. who knows"]
    while hero.is_alive() == True:
        if len(rooms_list) > 0:
            for i in range(len(rooms_list)):
                print(f"{i + 1}: {rooms_list[i]}")
            choice = int(input("""
            You stand in a big room lookoing at 3 different doors
            each with a different challenge behind it
            which one do you choose? 
            choice >>> """))
            if choice == 1:
                enemy = Zombie()
            elif choice == 2:
                enemy = Shadow()
            else:
                enemy = Goblin()
            print(f"You encounter a {enemy.name} in this room , what would you like to do?")
        while hero.is_alive() == True:
            action_choice = int(input("""
        1. Attack
        2. Do Nothing
        3. Enter the shop that's in this room for some reason
        4. Flee
        choice>>> """))
            print(hero.check_status())
            print(enemy.check_status())
            if action_choice == 1:
                enemy.take_damage(hero.name)
                hero.take_damage(enemy)
            elif action_choice == 2:
                hero.take_damage(enemy)
            elif action_choice == 3:
                print("you enter the shop")
            else: 
                print("coward")
                break
            if enemy.is_alive() == False:
                print(f"you did it! you killed the {enemy.name}")
                del rooms_list[choice - 1]
                break
            if hero.is_alive() == False:
                print("you died:/")



                
    dragon = Dragon()
    while hero.is_alive() == True:
        print("You defeated all of the enemies, and a dragon crashes through the roof!")
        print("Running is futile - you have no choice except to stand and fight")
        while hero.is_alive and dragon.is_alive() == True:
            hero.take_damage(dragon)
            dragon.take_damage(hero)
        if dragon.is_alive() == False:
            print("You did it! you slayed all everyone in this area! the villagers thank you.")
        if hero.is_alive() == False:
            print("you died:/")
            



main_menu()



# num = int(input(""))

# def open_shop():
#     print("Welcome to the shop! Which item would you like?")