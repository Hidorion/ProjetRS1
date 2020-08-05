##### MODULES #####
import random

##### DATA #####
import GettingMap
import Dice
import Variables



def ShowInventory ():
    """
        This function should show the inventory
    """
    if BaseItems['0.4'][1] :
        Statut = "Filled up "
    else :
        Statut = "Empty "
    print(f"{BaseItems['0.1'][0]} (0.1)\n{BaseItems['0.2'][0]} (0.2)\n{BaseItems['0.3'][0]} (0.3)\n{Statut}{BaseItems['0.4'][0]} (0.4)\n ")
    print(f"{PlayerInventory}\n")
    if Keys["2.1"][2]:
        print(Keys["2.1"][0])
    if Keys["2.2"][2]:
        print(Keys["2.2"][0])
    if Keys["2.3"][2]:
        print(Keys["2.3"][0])
    if Keys["2.4"][2]:
        print(Keys["2.4"][0])
    

def UseObject (IdEntered):
    """
        This function allows the player to interact with its inventory
    """
    if not IdEntered:
        Variables.GameMessage = "Tu as des hallucinations non ?"
    if IdEntered in BaseItems:
        if IdEntered == "0.1":
            Dice.DiceGame(Variables.PlayerName)
        elif IdEntered == "0.2":
            GettingMap.MapsLegend
        elif IdEntered == "0.3":
            Variables.GameMessage = "Le couteau est plein de sable et est complètement inutilisable"
        elif IdEntered == "0.4":
            if BaseItems["0.4"][1]:
                Variables.Soif += LootableItems["1.3"][3][2]
                print("Tu as bu ta bouteille")
                BaseItems["0.4"][1] = False
            else :
                print("Ta bouteille est vide mais tu peux la remplir près du pont")
    if IdEntered in Keys:
        if IdEntered == "2.1":
            if Keys[IdEntered][2]:
                Variables.GameMessage ="Tu regardes ta votre clé en bronze"
            else :
                Variables.GameMessage ="Il faut continuer de chercher"
        if IdEntered == "2.2":
            if Keys[IdEntered][2]:
                Variables.GameMessage ="Tu regardes ta clé d'argent"
            else :
                Variables.GameMessage ="Il faut continuer de chercher"
        if IdEntered == "2.3":
            if Keys[IdEntered][2]:
                Variables.GameMessage ="Tu regardes ta clé en or"
            else :
                Variables.GameMessage ="Il faut continuer de chercher"
        if IdEntered == "2.4":
            if Keys[IdEntered][2]:
                Variables.GameMessage ="Tu regardes ta clé USB"
            else :
                Variables.GameMessage ="Il faut continuer de chercher"

def GetObjectInBag ():
    """
        This function was creating yearning to be the one that put objects to the inventory but it's creator never find a descent way to make it.
    """
    if LootableItems["1.10"][4] == 1: #Max 10 pods or 20 if you win the big leather bag
        MaxPodInventory = 20
    else:
        MaxPodInventory = 10
    if PlayerInventory[0] <= MaxPodInventory:
        if LootableItems["1.4"][4] == 1:
            LootableItems["1.4"][4] = "1"
            PlayerInventory.append(LootableItems["1.4"][0])
            PlayerInventory[0] += LootableItems["1.4"][2]

MaxPodInventory = 10
PlayerInventory = [0 , f"/{MaxPodInventory}"] #Player's inventory [0] = Number of Pods


BaseItems = {
    # ID : [0 Name, 1 Usable ?,3 Pods]
    "0.1" : ["Laptop and Charger", True, 0],
    "0.2" : ["Pocket Map", True, 0],
    "0.3" : ["Swiss army Knife", True, 0],
    "0.4" : ["Flask", False, 0]
    }

LootableItems = {
    # ID : [0 Name, 1 Usable ?, 2 Pods, 3 Effects, 4 Stock]
    "1.1" : ["Watermelon", True, 1, (0, 2, 8), 0],
    "1.2" : ["Filthy Water", True, 1, (random.randint(-6,-2), 0, 0), 0],
    "1.3" : ["Clear Water", True, 1, (0, 0, 12), 0],
    "1.4" : ["Camp Bed", False, 1, (10, 3, 0), 0],
    "1.5" : ["Aloe Vera", True, 1, (8, 1, 0), 0],
    "1.6" : ["Agrum", True, 1, (4, -1, -1), 0],
    "1.7" : ["Red Berries", True, 0.5, (0, 4, 1), 0],
    "1.8" : ["Banana", True, 1, (0, 10, 0), 0],
    "1.9" : ["Weird Fruit", True, 1, (-3, 10, -1), 0],
    "1.10" : ["Big Leather Bag", False, 0, 10, 0]
    }
    
Keys = {
    #ID : [ 0 Name, 1 Usable ? 2 In bag ?]
    "2.1" : ["Bronze Key", False, False],
    "2.2" : ["Silver Key", False, False],
    "2.3" : ["Golden Key", False, False],
    "2.4" : ["USB Key", False, False]
    }

