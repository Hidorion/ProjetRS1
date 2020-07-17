import Variables
import GettingMap
import Clear
import GettingPlayer
import Cesar
import Inventory

def ActiveDoors(Y,X):
    if Y == 3 and X == 35:
        input("Tu te retrouve face à une porte étrange, tu décides de t'approcher. ")
        Cesar.CesarGame()
    else:
        pass

def GetCharacterAction():
    """
        Ask for character action
    """
    
    # list of possible actions
    PossibleActions = ["Z", "Q", "S", "D","R","I","HELP"]

    # wait for a valid action
    Action = ""
    while Action not in PossibleActions:
        Action = input("Que veux tu faire ? ").upper()

    # execute action
    Clear.ClearConsole()
    
    

    ExecuteCharacterAction(Action)
    GettingMap.DrawMap()
    GettingPlayer.GivingPlayersStats()

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
    elif Action == "I":
        Variables.GameMessage = f"\nVous regardez votre inventaire\n {Inventory.Keys} "
    elif Action == "HELP":
        Variables.GameMessage = "\nZ pour aller vers le Nord, S pour le Sud, D pour l'Est et Q pour l'Ouest\nR pour vous reposer et I pour consulter votre Inventaire"
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
    ActiveDoors(Variables.PlayerPosition["Y"],Variables.PlayerPosition["X"])
