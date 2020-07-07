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
                MazeMap.append(Columns)
                Y += 1
def DrawMaze():
    """
        Draw maze on console from 2 dimensional list
    """

    # draw maze
    for Y in range(len(MazeMap)):
        for X in range(len(MazeMap[Y])):
            if (Y == CharacterPosition["Y"]
                and X == CharacterPosition["X"]):
                # this is character position, draw it
                print(CharacterSymbol, end="")
            else:
                # no character here, draw maze
                print(MazeElements[MazeMap[Y][X]]["Image"], end="")
        print()

    # show message if any
    #if GameMessage != "":
    #    print(GameMessage)
    #    GameMessage = ""
    #else:
    #    print()
MazeElements = {
    " " : {
        "Name" : "Ground",
        "Image" : " ",
        "CanWalk" : True},
    "*" : {
        "Name" : "Sand",
        "Image" : "▒",
        "CanWalk" : True},
    "T" : {
        "Name" : "Tree",
        "Image" : "T",
        "CanWalk" : True
        },
    "M" : {
        "Name" : "Montain",
        "Image" : "M",
        "CanWalk" : True},
    "S" : {
        "Name" : "Potable Water",
        "Image" : "S",
        "CanWalk" : False},
    "=" : {
        "Name" : "Bridge",
        "Image" : "=",
        "CanWalk" : True},
    "~" : {
        "Name" : "Sea",
        "Image" : "~",
        "CanWalk" : False}
    }

    # print(Variables.MazeMap)
CharacterPosition = {"X" : 0, "Y" : 0}
MazeMap = []
CharacterSymbol = "☻"
CharacterPosition = {"X" : 0, "Y" : 0}