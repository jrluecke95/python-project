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

# make a character class for universal traits - done
# make a hero class for heroes = done
# make an enemy class for enemies - not necessary at this point 
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
    # rooms_list = ["A door covered in... brains?", "A door that has the silhouette of someone on it", "A door that has the outline of some tiny thing on it.. who knows"]
    rooms_dict = {1: "A door covered in... brains?", 2: "A door that has the silhouette of someone on it", 3: "A door that has the outline of some tiny thing on it.. who knows"}
    while hero.is_alive() == True and (len(rooms_dict) > 0) == True:
        if len(rooms_dict) > 0:
            for room in rooms_dict:
                print(f"{room}: {rooms_dict[room]}")
            choice = int(input(f"""
            You stand in a big room lookoing at {len(rooms_dict)} different doors
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
        while hero.is_alive() == True and (len(rooms_dict) > 0) == True:
            action_choice = int(input("""
        1. Attack
        2. Do Nothing
        3. Enter the shop that's in this room for some reason
        4. Flee
        choice>>> """))
            print(hero.check_status())
            print(enemy.check_status())
            if action_choice == 1:
                enemy.take_damage(hero)
                hero.take_damage(enemy)
            elif action_choice == 2:
                hero.take_damage(enemy)
            elif action_choice == 3:
                print("you enter the shop")
                # run shop function
            else: 
                print("coward")
                break
            if enemy.is_alive() == False:
                print(f"you did it! you killed the {enemy.name} and got {enemy.bounty} gold coins from their lifeless corpse")
                hero.coins += enemy.bounty
                del rooms_dict[choice]
                break
            if hero.is_alive() == False:
                print("you died:/")




    dragon = Dragon()
    while hero.is_alive() == True:
        print("You defeated all of the enemies, and a dragon crashes through the roof!")
        print("Running is futile - you have no choice except to stand and fight")
        while hero.is_alive() == True and dragon.is_alive() == True:
            hero.take_damage(dragon)
            dragon.take_damage(hero)
        if dragon.is_alive() == False:
            print("You did it! you slayed all everyone in this area! the villagers thank you.")
            break
        if hero.is_alive() == False:
            print("you died:/")
            break
            

def shop(person):
    shop_dict = {"poison potion": 5, "healing potion": 5, "bow and arrow": 10}
    shop_dict_values = list(shop_dict.values())
    shop_dict_keys = list(shop_dict.keys())
    while person.coins > 0:
        shop_answer = int(input("""
    Welcome to the shop! 
    What would you like to do here?
    1. Buy Something
    2. Just taking a break - i don't need anything
    choice >>> """))
        if shop_answer == 1:
            for item in shop_dict:
                print(f"{shop_dict_keys.index(item) + 1}: {item} costs {shop_dict[item]}")
            purchase = int(input("What item do you want? "))
            person.coins -= shop_dict_values[purchase-1]
            print(f"""you bought a {shop_dict_keys[purchase -1]} you have {person.coins} coins left""")
            if shop_dict_keys[purchase -1] in person.items:
                 person.items[shop_dict_keys[purchase -1]] += 1
            else:
                person.items[shop_dict_keys[purchase -1]] = 1
            print(person.items)
        else:
            print("see you later!")
    

def open_inventory(person):
    print("I see you need some help this fight")
    keys_list = list(person.items.keys())
    counter = 1
    for item in person.items:
        print(f"{counter}: you have {person.items[item]} {item}'s")
        counter += 1
    use_item_choice = int(input("""
    What would you like to do?
    1. Use item
    2. You don't need no stinking item
    choice >>> """))
    if use_item_choice == 1:
        inner_counter = 1
        for item in person.items:
            print(f"{inner_counter}: you have {person.items[item]} {item}'s")
            inner_counter += 1
        item_choice = int(input("What item would you like to use? "))
        used_item = keys_list[item_choice - 1]
        print(used_item)
    if used_item == "poison potion":
        person.items["poison potion"] -= 1
        print(person.items)
        return 5
    elif used_item == "healing potion":
        person.items["healing potion"] -= 1
        print(person.items)
        return 5
    

    # able to buy and "use" items - need to implement this into the battle portion of the game
    # need to figure out how to properly loop it so that you can use multiple items
    # should find a better way to use ending if loops at the end of use item function
    # could make each item and use of item it's own function


shop_dict = {"poison potion": 5, "healing potion": 5, "bow and arrow": 10}


hero = Paladin()
shop(hero)
open_inventory(hero)


# main_menu()



# num = int(input(""))

# def open_shop():
#     print("Welcome to the shop! Which item would you like?")