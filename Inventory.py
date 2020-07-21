import random
PlayerInventory = []*10


BaseItems = {
    "2.1" : "Laptop and Charger",
    "Usable" : False,
    "2.2" : "Pocket Map",
    "Usable" : True,
    "2.3" : "Swiss army Knife",
    "Usable" : True,
    "2.4" : "Flask",
    "Usable" : True,
    "NbUse" : 4,
    }

LootableItems = {
    "1.1" : "Watermelon",
    "Usable" : True,
    "Energy" : 0,
    "Starve" : 2,
    "Thurst" : 8,
    "NbUse"  : 4,
    "1.2" : "Filthy Water",
    "Usable" : True,
    "Energy" : random.randint(-6,-2),
    "Starve" : 0,
    "Thurst" : 0,
    "1.3" : "Clear Water",
    "Usable" : True,
    "Energy" : 0,
    "Starve" : 0,
    "Thurst" : 12,
    "1.4" : "Camp Bed",
    "Usable" : True,
    "Energy" : 2,
    "Starve" : 0,
    "Thurst" : 1,
    "1.5" : "Aloe Vera",
    "Usable" : True,
    "Energy" : 8,
    "Starve" : 1,
    "Thurst" : 0,
    "1.6" : "Agrum",
    "Usable" : True,
    "Energy" : 4,
    "Starve" : -1,
    "Thurst" : -1,
    "1.7" : "Red Berries",
    "Usable" : True,
    "Energy" : 0,
    "Starve" : 4,
    "Thurst" : 1,
    "1.8" : "Banana",
    "Usable" : True,
    "Energy" : 0,
    "Starve" : 10,
    "Thurst" : 0,
    "1.1" : "Weird Fruit",
    "Usable" : True,
    "Energy" : -3,
    "Starve" : 10,
    "Thurst" : -1,
    }
    
Keys = {
    "3.1" : ["Bronze Key", True, False],
    "3.2" : ["Silver Key", True, False],
    "3.3" : ["Golden Key", True, False],
    "3.4" : ["USB Key", True, False]
    }

IslandInventory = {
    "BaseItems" : BaseItems,
    "LootableItems" : LootableItems,
    "Keys" : Keys
}

if Keys["3.1"][2] and Keys["3.2"][2] and Keys["3.3"][2]:
    Keys["3.4"][2] = True