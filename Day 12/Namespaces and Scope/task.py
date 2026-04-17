# enemies = 1
#
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")
#
# #Local Scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()
# print(potion_strength) #Gives an error because potion_strength is only locally defined in the function not globally

#Global Scope
player_health = 10 #Player health is a global variable and anything can access it

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
print(player_health)
