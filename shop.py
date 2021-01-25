
from hero import Hero
from paladin import Paladin



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
            # below if loop enters shop and prints list before next user input checker
            if choose_shop == 1:
                print("Here is what we have for you today\n")
                item_names = list(hero.items.keys())
                counter = 1
                for item in item_names:
                    print(f"{counter}: {item}")
                    counter += 1
                # this while loop checks to see if choice is in range
                while True:
                    try:
                        item_choice_num = int(input("Which item would you like to purchase today? Type 0 if you decide you don't want anything")) - 1
                        if item_choice_num in range(len(item_names)): 
                            item_choice_name = item_names[item_choice_num]
                            print(f"You have selected {item_choice_name}")
                            break
                        elif item_choice_num == -1:
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Sorry that wasn't a valid selection")
                # outside of previous while loop this if statement checks if they have enough coins and if not it goes back to shop main menu by default because it is in larger while loop
                if item_choice_num == -1:
                    break
                item_cost = hero.items[item_choice_name]["cost"]
                if hero.coins >= item_cost:
                    print(f"you bought a {item_choice_name}")
                    hero.coins -= item_cost
                    print(f"you now have {hero.coins} coins")
                    hero.get_item(item_choice_name)
                    hero.print_inventory()
                    break
                else:
                    print("sorry you do not have enough coins for that")
            elif choose_shop == 2:
                break
            else:
                raise ValueError
        except ValueError:
            print("sorry that wasn't a valid selection")

hero = Paladin()

shop(hero)