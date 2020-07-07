
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
                    # ignore line ends
                    if Character == "\n":
                        continue
                    # add character to map
                    Columns.append(Character)
                    # place character at map entry
                    if Character == "E":
                        CharacterPosition["X"] = X
                        CharacterPosition["Y"] = Y
                    X += 1
                # add line to map
                MapMap.append(Columns)
                Y += 1
def DrawMap():
    """
        Draw Map on console from 2 dimensional list
    """

    # draw Map
    for Y in range(len(MapMap)):
        for X in range(len(MapMap[Y])):        
            print(f'{MapElements[MapMap[Y][X]]["Image"]}', end="" )
        print()

def pointchanger (y,x,sample,map):
    map[y][x] = sample

MapElements = {
    " " : {
        "Name" : "Ground",
        "Image" : " ",
        "CanWalk" : True},
    "*" : {
        "Name" : "Sand",
        "Couleur" : "\u001b[33m",
        "Image" : "░",
        "CanWalk" : True},
    "T" : {
        "Name" : "Tree",
        "Couleur" : "\u001b[0m",
        "Image" : "♣",
        "CanWalk" : True},
    "M" : {
        "Name" : "Montain",
        "Couleur" : "\u001b[0m",
        "Image" : "▲",
        "CanWalk" : True},
    "S" : {
        "Name" : "Potable Water ",
        "Couleur" : "\u001b[0m",
        "Image" : "~",
        "CanWalk" : False},
    "=" : {
        "Name" : "Bridge",
        "Couleur" : "\u001b[0m",
        "Image" : "═",
        "CanWalk" : True},
    "~" : {
        "Name" : "Sea",
        "Couleur" : "\u001b[0m",
        "Image" : "ʬ",
        "CanWalk" : False},
    }

    # print(Variables.MapMap)
CharacterPosition = {"X" : 0, "Y" : 0}
MapMap = []
CharacterPosition = {"X" : 0, "Y" : 0}
#pointchanger(1,1,"☻",MapMap)
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