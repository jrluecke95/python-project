from character import Character
from hero import Hero
from paladin import Paladin
from wizard import Wizard
from assassin import Assassin
from zombie import Zombie
from shadow import Shadow
from goblin import Goblin
from dragon import Dragon
from shop import shop
from use_item import use_item
from fight_dragon import fight_dragon
from fight_room import fight_room

def hero_choice():
    print("Welcome to the game! Which hero would you like to select? Each hero has it's own strengths and weaknesses, so choose wisely")
    print()
    print("You must clear 3 rooms, each with a different enemy, in order to move onto the boss fight.. enjoy")
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
    print(hero.full_stats())
    print()
    return hero

def room_choice(hero_choice):
    hero = hero_choice
    dragon_dead = False
    win = False
    rooms_dict = {"Room 1": "A door covered in... brains?", "Room 2": "A door that has the silhouette of someone on it", "Room 3": "A door that has the outline of some tiny thing on it.. who knows", "Room 4": "Shop"}
    cleared_rooms = []
    while hero.is_alive() is True and dragon_dead == False:
        try:
            rooms_string = ""
            for room in rooms_dict:
                rooms_string += f"{room}: {rooms_dict[room]}\n"
            choice = int(input(f"""
You stand in a big room lookoing at {len(rooms_dict)} different doors
each with a different challenge behind it
which one do you choose? 

{rooms_string}
choice >>> """))
            if choice == 1:
                enemy = Zombie()
                win = fight_room(hero, enemy)
            elif choice == 2:
                enemy = Shadow()
                win = fight_room(hero, enemy)
            elif choice == 3:
                enemy = Goblin()
                win = fight_room(hero, enemy)
            elif choice == 4:
                shop(hero)
            else:
                raise ValueError
        except ValueError:
            print("Sorry! that wasn't a valid selection")
        if win == True:
            cleared_rooms.append(rooms_dict[f'Room {choice}'])
            rooms_dict[f'Room {choice}'] += ' - cleared' 
        elif win == False:
            pass
        if len(cleared_rooms) >= 3:
            while True:
                boss_fight = int(input("""
        After clearing all 3 rooms a mysterious 4th door opens that seems to lead outside...
        What do you want to do?
        1. Walk through the door
        2. Go into the shop one last time
        3. Kill some more easy enemies to farm up coins for more items

        choice >>> """
        ))
                try:
                    if boss_fight == 1:
                        print("good luck!")
                        fight_dragon(hero)
                        dragon_dead = True
                        break
                    elif boss_fight == 2:
                        shop(hero)
                    elif boss_fight == 3:
                        break
                    else:
                        raise ValueError
                except:
                    print("sorry that wasn't a valid choice")
    
def play_game():
    room_choice(hero_choice())

play_game()


