import Variables



def LoadMapFromFile(FileName):
    """
        Loads a generic map from specified file name
    """
    with open(FileName, "r", encoding="utf-8") as MyFile:
            # Y = 0
            for Line in MyFile:
                Columns = []
                # X = 0
                for Character in Line:
                    if Character == "\n": # ignore line ends
                        continue
                    Columns.append(Character) # add character to map
                    # X += 1
                Variables.MapMap.append(Columns) # add line to map
                # Y += 1

def DrawMap():
    """
        Draw Map on console from 2 dimensional list
    """
    for Y in range(len(Variables.MapMap)):
        for X in range(len(Variables.MapMap[Y])):        
            if (Y == Variables.PlayerPosition["Y"] and X == Variables.PlayerPosition["X"]):
                print(Variables.PlayerIcon, end="")
            else:# no player here, draw maze
                print(f'{MapElements[Variables.MapMap[Y][X]]["Color Start"]}{MapElements[Variables.MapMap[Y][X]]["Image"]}{MapElements[Variables.MapMap[Y][X]]["Color End"]}', end="" )
        print()

def PointChanger (y,x,sample,carte):
    carte[y][x] = sample
    return carte
    
def DoorSpawn ():
    """
        We span the doors.
    """
    PointChanger(3,35,"9",Variables.MapMap) #We add the door for the César Code
    PointChanger(20,8,"8",Variables.MapMap) #We add the door for the FizzBuzz
    PointChanger(5,74,"7",Variables.MapMap) #We add the door for the Sphinx

def ObjectsSpawn():
    """
        Spawning Objects
    """
    PointChanger(21,74,"5",Variables.MapMap)


MapElements = {
    " " : {
        "Name" : "Ground",
        "Image" : " ",
        "CanWalk" : True,
        "Color Start" : "",
        "Color End" : "",
        "Message" : ""},
    "*" : {
        "Name" : "Sand",
        "Image" : "░",
        "CanWalk" : True,
        "Color Start" : "\u001b[33m",
        "Color End" : "\u001b[0m",
        "Message" : ""},
    "T" : {
        "Name" : "Tree",
        "Image" : "♣",
        "CanWalk" : True,
        "Color Start" : "\u001b[38;5;70m",
        "Color End" : "\u001b[0m",
        "Message" : ". Vous passez à travers les arbres avec aisance"},
    "M" : {
        "Name" : "Mountain",
        "Image" : "▲",
        "CanWalk" : False,
        "Color Start" : "\u001b[0m",
        "Color End" : "\u001b[0m",
        "Message" : ". La montagne est trop abrute pour être grimpée"},
    "S" : {
        "Name" : "Potable Water ",
        "Image" : "~",
        "CanWalk" : False,
        "Color Start" : "\u001b[36m",
        "Color End" : "\u001b[0m",
        "Message" : ". L'eau y est clair. Le courant est cependant trop fort pour t'y baigner ou remplir ta bouteille"},
    "=" : {
        "Name" : "Bridge",
        "Image" : "═",
        "CanWalk" : True,
        "Color Start" : "\u001b[38;5;94m",
        "Color End" : "\u001b[0m",
        "Message" : ". Un pont naturel mais stable"},
    "~" : {
        "Name" : "Sea",
        "Image" : "≈",
        "CanWalk" : False,
        "Color Start" : "\u001b[34m",
        "Color End" : "\u001b[0m",
        "Message" : ". La Mer est trop agitée pour s'y baigner"},
    "9" : {
        "Name" : "Door Cesar",
        "Image" : "○",
        "CanWalk" : True,
        "Color Start" : "\u001b[31m",
        "Color End" : "\u001b[0m",
        "Message" : ". Veux tu tenter d'obtenir la Clé d'Argent ?"},
    "8" : {
        "Name" : "Door Fizz Buzz",
        "Image" : "●",
        "CanWalk" : True,
        "Color Start" : "\u001b[31m",
        "Color End" : "\u001b[0m",
        "Message" : ". Veux tu tenter d'obtenir la Clé Dorée ?"},
    "7" : {
        "Name" : "??????",
        "Image" : "ᴥ",
        "CanWalk" : True,
        "Color Start" : "\u001b[31m",
        "Color End" : "\u001b[0m",
        "Message" : ". Veux tu tenter d'obtenir la Clé de Bronze ?"},
    "6" : {
        "Name" : "Grande Porte",
        "Image" : "۩",
        "CanWalk" : True,
        "Color Start" : "\u001b[31m",
        "Color End" : "\u001b[0m",
        "Message" : ". Veux tu tenter d'ouvrir la Grande Porte ? "},
    "5" : {
        "Name" : "Grande Porte",
        "Image" : "©",
        "CanWalk" : True,
        "Color Start" : "\u001b[38m",
        "Color End" : "\u001b[0m",
        "Message" : ". Tu viens de trouver quelque chose "}
    }


# Legend for the player for he can get what the map means
MapsLegend = "\nEau potable = ~\nLa mer = ≈\nMontagne = ▲\nSable = ░\nPlaine = " "\nPorte 1 = ○\nPorte 2 = ᴥ\nPorte 3 = ●\nGrande Porte = ۩\nArbre = ♣\nPont = ═"
""" 
Objet consommable = ©
Objet récupérable = ʘ

"""