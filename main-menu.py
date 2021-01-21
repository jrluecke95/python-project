Paladin
Wizard
Assassin

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
    3. Assassin"""))
    if answer == 1:
        hero = Paladin()
    if answer == 2:
        hero = Wizard()
    if answer == 3:
        hero = Assassin()
    print(f"Great choice! You have selected {hero.name}!")
    print(hero.check_status())


num = int(input(""))

def open_shop():
    print("Welcome to the shop! Which item would you like?")