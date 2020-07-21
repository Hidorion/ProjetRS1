import Variables
import GettingMap
import Clear
import GettingPlayer
import Cesar
import Inventory
import Fizzbuzz
import Sphinx
from Variables import Santé

def ActiveDoors(Y,X):
    """
        Permet d'activer les portes quand on arrive dessus.
    """
    if Y == 3 and X == 35:
        input("Tu te retrouve face à une porte étrange, tu décides de t'approcher. ")
        Cesar.CesarGame()
    elif Y == 20 and X == 8:
        input(Variables.FizzbuzzMessage)
        Fizzbuzz.FizzBuzzGame(Fizzbuzz.ListOfPlayers)
    elif Y == 5 and X == 74:
        input("Un Sphinx se dresse devant la fôret. Il te demande de t'avancer devant lui'. ")
        Sphinx.SphinxPrep("TheSphinx.txt")
    else:
        pass

def Movement():
    Variables.Santé=Variables.Santé + Variables.BasicMove[0]
    Variables.Faim=Variables.Faim + Variables.BasicMove[1]
    Variables.Soif=Variables.Soif + Variables.BasicMove[2]

def GetCharacterAction():
    """
        Ask for character action
    """

    # list of possible actions
    PossibleActions = ["Z", "Q", "S", "D","R","I","HELP","MAP"]

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
        Movement()
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
        Variables.GameMessage = f"\nVous regardez votre inventaire\n {Inventory.Keys} \n {input()} \n"
    elif Action == "MAP":
        Variables.GameMessage = f"\nVous regardez votre carte et sa légende\n {GettingMap.MapsLegend} \n"
        input("\n")
    elif Action == "HELP":
        Variables.GameMessage = f"\nZ pour aller vers le Nord, S pour le Sud, D pour l'Est et Q pour l'Ouest\nR pour vous reposer, I pour consulter votre Inventaire, MAP pour ouvrir la légende de la carte\n {input()} \n"
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
