from character import Character
from hero import Hero
from paladin import Paladin
from wizard import Wizard
from assassin import Assassin
from zombie import Zombie
from shadow import Shadow
from goblin import Goblin
from dragon import Dragon

def hero_choice():
    print("Welcome to the game! Which hero would you like to select? Each hero has it's own strengths and weaknesses, so choose wisely")
    while True:
        try:
            answer = int(input("""
            1. Paladin
            2. Wizard
            3. Assassin
            choice >>> """))
            if answer == 1:
                hero = Paladin()
                break
            if answer == 2:
                hero = Wizard()
                break
            if answer == 3:
                hero = Assassin()
                break
            else:
                raise ValueError
        except ValueError:
            print("sorry! that wasn't a valid selection")
    print(f"Great choice! You have selected {hero.name}!")
    print(hero.check_status())
    return hero

def room_choice(hero_choice):
    hero = hero_choice
    rooms_dict = {1: "A door covered in... brains?", 2: "A door that has the silhouette of someone on it", 3: "A door that has the outline of some tiny thing on it.. who knows"}
    while hero.is_alive() is True and len(rooms_dict) > 0:
        for room in rooms_dict:
            print(f"{room}: {rooms_dict[room]}")
        while True:
            try:
                choice = int(input(f"""
        You stand in a big room lookoing at {len(rooms_dict)} different doors
        each with a different challenge behind it
        which one do you choose? 
        choice >>> """))
                if choice == 1:
                    enemy = Zombie()
                    break
                elif choice == 2:
                    enemy = Shadow()
                    break
                elif choice == 3:
                    enemy = Goblin()
                    break
                else:
                    raise ValueError
            except:
                print("Sorry! that wasn't a valid selection")
        win = fight_room(hero, enemy)
        if win == 1:
            del rooms_dict[choice]
        else:
            pass
    if len(rooms_dict) <= 0:
        fight_dragon(hero)

def fight_room(hero_choice, enemy_choice):
    hero = hero_choice
    enemy = enemy_choice
    while hero.is_alive() == True:
        print(f"You encounter a {enemy.name} in this room , what would you like to do?")
        try:
            action_choice = int(input("""
            1. Attack
            2. Do Nothing
            3. Enter the shop that's in this room for some reason
            4. Flee
            choice>>> """))
            print(hero.check_status())
            print(enemy.check_status())
            if action_choice == 1:
                item_effect = item_attack(hero)
                if item_effect > 0:
                    hero.health += item_effect
                    print(f"You used an item and healed by {item_effect} points!")
                elif item_effect < 0:
                    enemy.health += item_effect
                    print(f"You used an item and did {abs(item_effect)} damage to the {enemy.name}")
                elif item_effect == 0:
                    print("no item was used this attack")
                enemy.take_damage(hero)
                hero.take_damage(enemy)
            elif action_choice == 2:
                hero.take_damage(enemy)
            elif action_choice == 3:
                shop(hero)
            elif action_choice == 4: 
                print("coward")
                return 0
            else:
                raise ValueError
        except ValueError:
            print("sorry! that wasn't a valid choice")
        if enemy.is_alive() == False:
            print(f"you did it! you killed the {enemy.name} and got {enemy.bounty} gold coins from their lifeless corpse")
            hero.coins += enemy.bounty
            return 1
        if hero.is_alive() == False:
            print("you died:/")
            return 0


def fight_dragon(hero_choice):
    hero = hero_choice
    dragon = Dragon()
    while hero.is_alive() == True:
        print("You defeated all of the enemies, and a dragon crashes through the roof!")
        print("Running is futile - you have no choice except to stand and fight")
        while hero.is_alive() == True and dragon.is_alive() == True:
            try:
                use_item_choice = int(input("""
            Do you want to check your inventory?
            1. yes
            2. no
            choice >>> """))
                if use_item_choice == 1:
                    hero.print_inventory()
                    item_effect = item_attack(hero)
                    if item_effect > 0:
                        hero.health += item_effect
                        print(f"You used an item and healed by {item_effect}points!")
                    elif item_effect < 0:
                        dragon.health += item_effect
                        print(f"you used an item and did {abs(item_effect)} damage to the dragon")
                    elif item_effect == 0:
                        print("no item was used... against a dragon.")
                    hero.take_damage(dragon)
                    dragon.take_damage(hero)
                    break
                elif use_item_choice == 2:
                    hero.take_damage(dragon)
                    dragon.take_damage(hero)
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

            
# have to check the inner item choice loop in addition to the broader do you wnat an item choice
def shop(hero_choice):
    hero = hero_choice
    while True:
        try:
            choose_shop = int(input("""
        Welcome to the shop! Would you like to purcahse something today?
        1. Yes
        2. No - just needed a break from the battle
        choice >>> """))
            if choose_shop == 1:
                print("Here is what we have for you today\n")
                counter = 1
                for item in hero.items:
                    print(f"{counter}: {item[0]}")
                    counter += 1
# need to check the item chioce to make sure it's valid before i can calc cost 
                item_choice = int(input("Which item would you like to purchase today? "))
                cost = item[item_choice - 1][2]
                if item_choice in range(len(hero.items) + 1) and hero.coins >= cost:
                    hero.get_item(item_choice - 1)
                    print(f"you bought a {hero.items[item_choice - 1][0]}")
                    hero.coins -= cost
                    hero.print_inventory()
                    print(hero.coins)
                else:
                    print("sorry that wasn't a valid choice!")
            elif choose_shop == 2:
                break
            else:
                raise ValueError
        except ValueError:
            print("sorry that wasn't a valid selection")

shop(Paladin())

def open_inventory(hero_choice):
    hero = hero_choice
    while True:
        counter = 0
        for item in hero.items:
            print(f"{counter + 1}: {item[2]} {item[0]}")
            counter += 1
        use_item_choice = int(input("Which item would you like to use this time? "))
        if use_item_choice in range(len(hero.items)):
            if hero.items[use_item_choice -1][2] > 0:
                hero.use_item(use_item_choice - 1)
                break
            else:
                print(f"sorry! you're all out of {hero.items[use_item_choice - 1][0]}")
                break
        else:
            print("sorry that wasn't an option")
            break

def item_attack(hero_choice):
    hero = hero_choice
    use_item_choice = int(input("""
    Would you like to use an item this attack?
    1. yes
    2. no - this enemy seems like a chump
    choice >>> """))
    if use_item_choice == 1:
        print("Which item would you like to use?")
        counter = 1
        for item in hero.items:
            print(f"{counter}: You have {item[2]} {item[0]}")
            counter += 1
        which_item = int(input("choice >>> "))
        if hero.items[which_item -1][2] > 0:
            return(hero.use_item(which_item - 1))
        else:
            print("you don't have any of those!")
            return 0
    else:
        print("really? no item? good luck... moron")
        return 0

    
def play_game():
    room_choice(hero_choice())

# play_game()



    