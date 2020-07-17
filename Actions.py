import Variables
import GettingMap
import Clear
def GetCharacterAction():
    """
        Ask for character action
    """
    
    # list of possible actions
    PossibleActions = ["Z", "Q", "S", "D","R"]

    # wait for a valid action
    Action = ""
    while Action not in PossibleActions:
        Action = input("Que doit faire le personnage ? ").upper()

    # execute action
    Clear.ClearConsole()
    
    ExecuteCharacterAction(Action)
    
    GettingMap.DrawMap()


def ExecuteCharacterAction(Action):
    """
        Executes choosen action
    """
    
    # store new character position
    NewCharacterPositionX = Variables.PlayerPosition["X"]
    NewCharacterPositionY = Variables.PlayerPosition["Y"]

    # prepare action
    if Action == "Z":
        NewCharacterPositionY -= 1
        Variables.GameMessage = f"\nLe personnage se déplace vers le Nord {GettingMap.MapElements[Variables.MapMap[NewCharacterPositionY][NewCharacterPositionX]]['Message']}\n"
    elif Action == "S":
        NewCharacterPositionY += 1
        Variables.GameMessage = f"\nLe personnage se déplace vers le Sud {GettingMap.MapElements[Variables.MapMap[NewCharacterPositionY][NewCharacterPositionX]]['Message']}\n"
    elif Action == "Q":
        NewCharacterPositionX -= 1
        Variables.GameMessage = f"\nLe personnage se déplace vers l'Ouest {GettingMap.MapElements[Variables.MapMap[NewCharacterPositionY][NewCharacterPositionX]]['Message']}\n"
    elif Action == "D":
        NewCharacterPositionX += 1
        Variables.GameMessage = f"\nLe personnage se déplace vers l'Est' {GettingMap.MapElements[Variables.MapMap[NewCharacterPositionY][NewCharacterPositionX]]['Message']}\n"
    elif Action == "R":
        Variables.GameMessage = "\nLe personnage se repose\n"
    print(Variables.GameMessage)
        

    # check if action is allowed
    if not GettingMap.MapElements[
        Variables.MapMap[NewCharacterPositionY][NewCharacterPositionX]]["CanWalk"]:
        # new position blocks movement, can't move
        Variables.GameMessage = f"\n{GettingMap.MapElements[Variables.MapMap[NewCharacterPositionY][NewCharacterPositionX]]['Message']} !\n"
        print(Variables.GameMessage)
        return

    # execute action
    Variables.PlayerPosition["X"] = NewCharacterPositionX
    Variables.PlayerPosition["Y"] = NewCharacterPositionY