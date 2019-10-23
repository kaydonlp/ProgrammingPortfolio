
import random


#player statistics
defense = 0
atk = 1
health = 100
mana = 50
inv = []
equipment = []
max_inv = 10
#Chest Setup
chest_inv = ("Gold",
             "Gems","Food",
             "Sword","Armor",
             "shield","Healing Potion",
             "Mana Potion","Arrows",
             "Crocs","Bows","Spear",
             "Helm","Pants","Boots",
             "Doom Hammer", "Dagger",
             "Excalibur", "Crsytal Orb", "Gloves",
             "Bracers","LA SPOOKACHINA COSTUME")

max_chest = 5
items = random.randint(2,max_chest)
chest = []
for i in range(items):
    chest.append(random.choice(chest_inv))


#LootChest

if inv:
    print(inv)
else:
    print("You have nothing in inventory")
    input("Open the chest to your items")
    for items in chest:
        inv.append(items)



print(inv)

for items in inv:
    if items == "Health Potion":
        health += 50
        inv.remove("Health Potion")
print(health)
for items in inv:
    if items == "Armor" :
        defense +=  5
        equipment.append(items)
        inv.remove("Armor")
print(defense)
for items in inv:
    if items == "Shield" :
        defense +=  10
        equipment.append(items)
        inv.remove("Shield")
print(defense)
for items in inv:
    if items == "Crocs" :
        defense +=  10
        equipment.append(items)
        inv.remove("Crocs")
print(defense)
for items in inv:
    if items == "Gloves":
        defense += 1
        equipment.append(items)
        inv.remove("Health Potion")
print(defense)
print(equipment)

# LARGE CHEST

chestBig_inv = ("Gold",
             "Gems","Food",
             "Sword","Armor",
             "shield","Healing Potion",
             "Mana Potion","Arrows",
             "Crocs","Bows","Spear",
             "Helm","Pants","Boots",
             "Doom Hammer", "Dagger",
             "Excalibur", "Crsytal Orb", "Gloves",
             "Bracers","LA SPOOKACHINA","Gold",
             "Gems","Food",
             "Sword","Armor",
             "shield","Healing Potion",
             "Mana Potion","Arrows",
             "Crocs","Bows","Spear",
             "Helm","Pants","Boots",
             "Doom Hammer", "Dagger",
             "Excalibur", "Crsytal Orb", "Gloves",
             "Bracers","LA SPOOKACHINA")

max_chest2 = 15
items = random.randint(5,max_chest2)
Bigchest = []
for i in range(items):
    chest.append(random.choice(chestBig_inv))
input("Press Enter to open Chest")

for i in chest:
    inv.append(i)

if  len(inv) > max_inv:
    x =len(inv) - max_inv
    print(inv)
    print("You need to remove" + str(x) +" Items")
    print(inv)
    while x > 0:
        item = input("What item would you like ot remove???")
        inv.remove(item)
        x -=1
        print(inv)
