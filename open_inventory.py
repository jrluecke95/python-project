# def open_inventory(hero_choice):
#     hero = hero_choice
#     while True:
#         counter = 0
#         for item in hero.items:
#             print(f"{counter + 1}: {item[2]} {item[0]}")
#             counter += 1
#         try:
#             use_item_choice = int(input("Which item would you like to use this time? "))
#             if use_item_choice in range(len(hero.items)):
#                 if hero.items[use_item_choice -1][2] > 0:
#                     return hero.use_item(use_item_choice - 1)
#                     # break
#                 else:
#                     print(f"sorry! you're all out of {hero.items[use_item_choice - 1][0]}")
#                     break
#             else:
#                 raise ValueError
#         except ValueError:
#             print("sorry that wasn't a valid selection")