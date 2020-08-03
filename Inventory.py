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
    print(BaseItems)
    print(PlayerInventory)
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
            print("remplissage bouteille")
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


PlayerInventory = [] #Player's inventory, max 10 pods

BaseItems = {
    # ID : [Name, Usable ?, Pods]
    "0.1" : ["Laptop and Charger", True, 0],
    "0.2" : ["Pocket Map", True, 0],
    "0.3" : ["Swiss army Knife", True, 0],
    "0.4" : ["Flask", True, 0]
    }

LootableItems = {
    # ID : [Name, Usable ?, Pods, Effects, Stock]
    "1.1" : ["Watermelon", True, 1, (0, 2, 8), 0],
    "1.2" : ["Filthy Water", True, 1, (random.randint(-6,-2), 0, 0), 0],
    "1.3" : ["Clear Water", True, 1, (0, 0, 12), 0],
    "1.4" : ["Camp Bed", False, 1, (2, 0, 1), 0],
    "1.5" : ["Aloe Vera", True, 1, (8, 1, 0), 0],
    "1.6" : ["Agrum", True, 1, (4, -1, -1), 0],
    "1.7" : ["Red Berries", True, 0.5, (0, 4, 1), 0],
    "1.8" : ["Banana", True, 1, (0, 10, 0), 0],
    "1.1" : ["Weird Fruit", True, 1, (-3, 10, -1), 0]
    }
    
Keys = {
    #ID : [Name, Usable ?]
    "2.1" : ["Bronze Key", False, False],
    "2.2" : ["Silver Key", False, False],
    "2.3" : ["Golden Key", False, False],
    "2.4" : ["USB Key", False, False]
    }

