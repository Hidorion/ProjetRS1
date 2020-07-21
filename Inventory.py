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
    "Tuple" : (0, 2, 8),
    "1.2" : "Filthy Water",
    "Usable" : True,
    "Tuple" : (random.randint(-6,-2), 0, 0),
    "1.3" : "Clear Water",
    "Usable" : True,
    "Tuple" : (0, 0, 12),
    "1.4" : "Camp Bed",
    "Usable" : True,
    "Tuple" : (2, 0, 1),
    "1.5" : "Aloe Vera",
    "Usable" : True,
    "Tuple" : (8, 1, 0),
    "1.6" : "Agrum",
    "Usable" : True,
    "Tuple" : (4, -1, -1),
    "1.7" : "Red Berries",
    "Usable" : True,
    "Tuple" : (0, 4, 1),
    "1.8" : "Banana",
    "Usable" : True,
    "Tuple" : (0, 10, 0),
    "1.1" : "Weird Fruit",
    "Usable" : True,
    "Tuple" : (-3, 10, -1)
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

