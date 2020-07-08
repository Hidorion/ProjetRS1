from os import replace
import Variables
import random


def LoadMapFromFile(FileName):
    """
        Loads a generic map from specified file name
    """
    with open(FileName, "r", encoding="utf-8") as MyFile:
            Y = 0
            for Line in MyFile:
                Columns = []
                X = 0
                for Character in Line:
                    if Character == "\n": # ignore line ends
                        continue
                    Columns.append(Character) # add character to map
                    X += 1
                Variables.MapMap.append(Columns) # add line to map
                Y += 1

def DrawMap():
    """
        Draw Map on console from 2 dimensional list
    """
    for Y in range(len(Variables.MapMap)):
        for X in range(len(Variables.MapMap[Y])):        
            if (Y == Variables.PlayerPosition["Y"] and X == Variables.PlayerPosition["X"]):
                print(Variables.PlayerIcon, end="")
            else:# no player here, draw maze
                print(f'{MapElements[Variables.MapMap[Y][X]]["Image"]}', end="" )
        print()

def PointChanger (y,x,sample,carte):
    carte[y][x] = sample
    return carte
    
def DoorSpawn ():
    """
        On fait apparaitre les portes.
    """
    PointChanger(3,random.randint(31,39),"9",Variables.MapMap) #On ajoute la Porte pour le César Code
    PointChanger(random.randint(15,20),8,"8",Variables.MapMap) #On ajoute la Porte pour le FizzBuzz
    PointChanger(5,random.randint(72,76),"7",Variables.MapMap) #On ajoute la Porte pour le Sphinx


MapElements = {
    " " : {
        "Name" : "Ground",
        "Image" : " ",
        "CanWalk" : True},
    "*" : {
        "Name" : "Sand",
        "Image" : "░",
        "CanWalk" : True},
    "T" : {
        "Name" : "Tree",
        "Image" : "♣",
        "CanWalk" : True},
    "M" : {
        "Name" : "Montain",
        "Image" : "▲",
        "CanWalk" : True},
    "S" : {
        "Name" : "Potable Water ",
        "Image" : "~",
        "CanWalk" : False},
    "=" : {
        "Name" : "Bridge",
        "Image" : "═",
        "CanWalk" : True},
    "~" : {
        "Name" : "Sea",
        "Image" : "ʬ",
        "CanWalk" : False},
    "9" : {
        "Name" : "Door Cesar",
        "Image" : "○",
        "CanWalk" : True},
    "8" : {
        "Name" : "Door Fizz Buzz",
        "Image" : "●",
        "CanWalk" : True},
    "7" : {
        "Name" : "??????",
        "Image" : "◌",
        "CanWalk" : True},
    }

    # print(Variables.MapMap)




#pointchangerpointchanger(2,random.randint(50,90),"○",MapMap) #Position César Code
#pointchangerpointchanger(random.randint(10,16),92,"◌",MapMap) #Position Sphinx Nombre Mystérieux

""" 
Eau potable = ~
Eau de mer = ʬ
Montagne = M
Sable = ░
Plaine = " "
Porte 1 César = ○
Porte 2 ????  = ◌
Porte 3 FB-ZZ = ●
Objet consommable = ©
Objet récupérable = ʘ
Grande Porte = ۩
Arbre = ♣
Pont = ═
"""