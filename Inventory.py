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
    print(f"{BaseItems['0.1'][3]} {BaseItems['0.1'][0]}\n{BaseItems['0.2'][3]} {BaseItems['0.2'][0]}\n{BaseItems['0.3'][3]} {BaseItems['0.3'][0]}\n{Statut}{BaseItems['0.4'][3]} {BaseItems['0.4'][0]}\n ")
    print(f"{PlayerInventory}\n")
    if Keys["2.1"][2]:#Bronze
        print(Keys["2.1"][3],Keys["2.1"][0])
    if Keys["2.2"][2]:#Silver
        print(Keys["2.2"][3],Keys["2.2"][0])
    if Keys["2.3"][2]:#Gold
        print(Keys["2.3"][3],Keys["2.3"][0])
    if Keys["2.4"][2]:#USB
        print(Keys["2.4"][3],Keys["2.4"][0])
    

def UseObject (IdEntered):
    """
        This function allows the player to interact with its inventory
    """
    if IdEntered == "":
        print()
    elif IdEntered in BaseItems:
        if IdEntered == "0.1": #Computer
            Dice.DiceGame(Variables.PlayerName)
        elif IdEntered == "0.2": #Map
            GettingMap.MapsLegend
        elif IdEntered == "0.3": #Knife
            Variables.GameMessage = "Le couteau est plein de sable et est complètement inutilisable"
        elif IdEntered == "0.4": #Flask
            if BaseItems["0.4"][1]:
                Variables.Soif += LootableItems["1.3"][3][2]
                print("Tu as bu ta bouteille")
                BaseItems["0.4"][1] = False
            else :
                print("Ta bouteille est vide mais tu peux la remplir près du pont")
    elif IdEntered in Keys:
        if IdEntered == "2.1": #Bronze
            if Keys[IdEntered][2]:
                Variables.GameMessage ="Tu regardes ta clé en bronze"
            else :
                Variables.GameMessage ="Il faut continuer de chercher"
        if IdEntered == "2.2": #Silver
            if Keys[IdEntered][2]:
                Variables.GameMessage ="Tu regardes ta clé d'argent"
            else :
                Variables.GameMessage ="Il faut continuer de chercher"
        if IdEntered == "2.3": #Gold
            if Keys[IdEntered][2]:
                Variables.GameMessage ="Tu regardes ta clé en or"
            else :
                Variables.GameMessage ="Il faut continuer de chercher"
        if IdEntered == "2.4": #USB
            if Keys[IdEntered][2]:
                Variables.GameMessage ="Tu regardes ta clé USB"
            else :
                Variables.GameMessage ="Il faut continuer de chercher"
    elif IdEntered in LootableItems and LootableItems[IdEntered][1] and LootableItems[IdEntered][4] > 0: #Looted item
        Variables.Santé += LootableItems[IdEntered][3][0]
        Variables.Faim += LootableItems[IdEntered][3][1]
        Variables.Soif += LootableItems[IdEntered][3][2]
        LootableItems[IdEntered][4] -= 1
        PlayerInventory.pop()
    else :
        input("Tu as des hallucinations non ? Parce que tu n'as pas cet objet. ")

def GetObjectInBag ():
    """
        This function was creating yearning to be the one that put objects to the inventory but it's creator never find a descent way to make it.
    """
    if PlayerInventory[0] <= MaxPodInventory:
        if LootableItems["1.4"][4] == 1:
            LootableItems["1.4"][4] = "1"
            PlayerInventory.append(LootableItems["1.4"][0])
            PlayerInventory[0] += LootableItems["1.4"][2]

MaxPodInventory = 10
PlayerInventory = [0 , f"/{MaxPodInventory}"] #Player's inventory [0] = Number of Pods


BaseItems = {
    # ID : [0 Name, 1 Usable ?,2 Pods, 3 ID]
    "0.1" : ["Laptop and Charger", True, 0, "0.1"],
    "0.2" : ["Pocket Map", True, 0, "0.2"],
    "0.3" : ["Swiss army Knife", True, 0, "0.3"],
    "0.4" : ["Flask", False, 0, "0.4"]
    }

LootableItems = {
    # ID : [0 Name, 1 Usable ?, 2 Pods, 3 Effects (Health, Food, Water), 4 Stock 5 ID]
    "1.1" : ["Watermelon", True, 1, (0, 2, 8), 0,"1.1"],
    "1.2" : ["Filthy Water", True, 1, (random.randint(-6,-2), 0, 0), 0,"1.2"],
    "1.3" : ["Clear Water", True, 1, (0, 0, 12), 0,"1.3"],
    "1.4" : ["Camp Bed", False, 1, (10, 3, 0), 0,"1.4"],
    "1.5" : ["Aloe Vera", True, 1, (8, 1, 0), 0,"1.5"],
    "1.6" : ["Agrum", True, 1, (4, -1, -1), 0,"1.6"],
    "1.7" : ["Red Berries", True, 0.5, (0, 4, 1), 0,"1.7"],
    "1.8" : ["Banana", True, 1, (0, 10, 0), 0,"1.8"],
    "1.9" : ["Weird Fruit", True, 1, (-3, 10, -1), 0,"1.9"],
    "1.10" : ["Big Leather Bag", False, 0, 20, 0,"1.10"]
    }
    
Keys = {
    #ID : [ 0 Name, 1 Usable ? 2 In bag ? 3 ID]
    "2.1" : ["Bronze Key", False, False,"2.1"],
    "2.2" : ["Silver Key", False, False,"2.2"],
    "2.3" : ["Golden Key", False, False,"2.3"],
    "2.4" : ["USB Key", False, False,"2.4"]
    }

