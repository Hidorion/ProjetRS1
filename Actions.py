##### MODULE #####
import random

##### DATA #####
import Variables
import GettingMap
import Clear
import GettingPlayer
import Cesar
import Inventory
import Fizzbuzz
import Sphinx
import BigDoor



def ActiveDoors(Y,X):
    """
        Allow the player to activate the doors when reached
    """
    if Y == 3 and X == 35: #Cesar
        input("Tu te retrouve face à une porte étrange, tu décides de t'approcher. ")
        Cesar.CesarGame()
        Clear.ClearConsole()
    elif Y == 20 and X == 8: #FizzBuzz
        input()
        print(Variables.FizzbuzzMessage)
        Fizzbuzz.MonkeyPrep("Text\monkeys.txt")
        Clear.ClearConsole()
    elif Y == 5 and X == 74: #Sphinx
        input("Un Sphinx se dresse devant la fôret. Il te demande de t'avancer devant lui'. ")
        Sphinx.SphinxPrep("Text\TheSphinx.txt")
        Clear.ClearConsole()
    elif Y == 2 and X == 20: #BigDoor
        input("Une lueur semble emergée derrière les arbres, tu décides d'y jeter un oeil. ")
        BigDoor.CheckKeys()
        Clear.ClearConsole()

def ActiveBottle(Y,X):
    """
        Allow the player to fill up his bottle 
    """
    if Y == 10 and X in (21,22,23,24,25): #Y 10 or 17 / X from 23 to 28
        if not Inventory.BaseItems["0.4"][1]:
            Inventory.BaseItems["0.4"][1] = True
            input("Tu profites d'être sur le pont pour remplir ta bouteille sans danger ")
    if Y == 17 and X in (21,22,23,24,25):
        if not Inventory.BaseItems["0.4"][1]:
            Inventory.BaseItems["0.4"][1] = True
            input("Tu profites d'être sur le pont pour remplir ta bouteille sans danger ")
        
def ActiveObject(Y,X):
    """
        Allow the player to get an object
    """
    ListOfStuff = ["1.1","1.5","1.6","1.7","1.8","1.9"] #0 to 5
    if Y == 21 and X == 74: #Test Object
        Stuff = ListOfStuff[random.randint(0,5)]
        Inventory.PlayerInventory.append(f"{Inventory.LootableItems[Stuff][5]} {Inventory.LootableItems[Stuff][0]}")
        Inventory.LootableItems[Stuff][4] += 1
        Inventory.PlayerInventory[0] += Inventory.LootableItems[Stuff][2]
        input(f"Tu viens de trouver ça : {Inventory.LootableItems[Stuff][0]} ")
        Clear.ClearConsole()
        GettingMap.PointChanger(21,74,"*",Variables.MapMap)

def Movement():
    """
        Impact the players while moving on the map
    """
    Variables.Santé=Variables.Santé + Variables.BasicMove[0]
    Variables.Faim=Variables.Faim + Variables.BasicMove[1]
    Variables.Soif=Variables.Soif + Variables.BasicMove[2]

def Resting():
    """
        Player is resting
    """
    if Inventory.LootableItems["1.4"][4] == 1: #Check if player got the bedcamp
        Variables.Resting = Inventory.LootableItems["1.4"][3]
    Variables.Santé=Variables.Santé + Variables.Resting[0]
    Variables.Faim=Variables.Faim + Variables.Resting[1]
    Variables.Soif=Variables.Soif + Variables.Resting[2]

def SavingProgress():
    """
        Saving the player's progressions
    """
    try:
        # open game file in write mode
        with open(Variables.GameFileName, "w", encoding="utf-8") as MyFile:
            # save maze
            for LineIndex, Line in enumerate(Variables.MapMap):
                MyFile.write("Map:")
                MyFile.writelines(Variables.MapMap[LineIndex])
                MyFile.write("\n")
            # save Player position
            MyFile.write(f"X:{Variables.PlayerPosition['X']}\n")
            MyFile.write(f"Y:{Variables.PlayerPosition['Y']}\n")
            MyFile.write(f"Name:{Variables.PlayerName}\n")
            # save game data
            MyFile.write(f"Santé:{Variables.Santé}\n")
            MyFile.write(f"Faim:{Variables.Faim}\n")
            MyFile.write(f"Soif:{Variables.Soif}\n")
            MyFile.write(f"Number of hours spent:{Variables.GameProgression}\n")
            MyFile.write(f"Inventory:{Inventory.BaseItems}\n")
            MyFile.write(f"Bag:{Inventory.LootableItems}\n")
            MyFile.write(f"KeyRing:{Inventory.Keys}\n")
            Variables.GameMessage = "\nLa partie en cours a été sauvegardée.\n"
    except:
        Variables.GameMessage = "\nSauvegarde de la partie impossible.\n"

def LoadingProgress():
    """
        Loading the player's progressions
    """
    try:
        # open game file in read mode
        with open(Variables.GameFileName, "r", encoding="utf-8") as MyFile:
            # reset map
            Variables.MapMap = []
            # load maze
            # read 1st line
            Line = MyFile.readline()
            # while line contains something
            while Line:
                # remove last Player (\n) at end of line
                Line = Line[:-1]
                if Line.startswith("Map:"):
                    # this data is part of map
                    MapLine = []
                    for Player in Line[len("Map:"):]:
                        MapLine.append(Player)
                    Variables.MapMap.append(MapLine)
                elif Line.startswith("X:"):
                    # this data is player position
                    Variables.NewPlayerPositionX = int(Line[len("X:"):])
                elif Line.startswith("Y:"):
                    # this data is player position
                    Variables.NewPlayerPositionY = int(Line[len("Y:"):])
                elif Line.startswith("Name:"):
                    # this data is the player name
                    Variables.PlayerName = str(Line[len("Name:"):])
                elif Line.startswith("Santé:"):
                    # this data is the player's energy
                    Variables.Santé = int(Line[len("Santé:"):])
                elif Line.startswith("Faim:"):
                    # this data is the player's hunger
                    Variables.Faim = int(Line[len("Faim:"):])
                elif Line.startswith("Soif:"):
                    # this data is the player's thirst
                    Variables.Soif = int(Line[len("Soif:"):])
                elif Line.startswith("Number of hours spent:"):
                    # this data is the player's progressions
                    Variables.GameProgression = int(Line[len("Number of hours spent:"):])
                elif Line.startswith("Inventory:"):
                    # this data is the player's Inventory
                    Inventory.BaseItems = eval(Line[len("Inventory:"):])
                elif Line.startswith("Bag:"):
                # this data is the player's bag
                    Inventory.LootableItems = eval(Line[len("Bag:"):])
                elif Line.startswith("KeyRing:"):
                # this data is the player's keyring
                    Inventory.Keys = eval(Line[len("KeyRing:"):])
                # read next line
                Line = MyFile.readline()

            Variables.GameMessage = "\nLa partie a été chargée.\n"
    except:
        Variables.GameMessage = "\nChargement de la partie impossible.\n"
        input("Chargement terminé")

def GetPlayerAction():
    """
        Ask for Player action
    """

# list of possible actions
    PossibleActions = ["Z", "Q", "S", "D","R","I","HELP","MAP","SAVE","LOAD","JIJICESAR","JIJISPHINX","JIJIBUZZ","JIJIDOOR","JIJIRAIDEBOULE","JIJIKEYKEYKEY"]

# wait for a valid action
    Action = ""
    while Action not in PossibleActions:
        Action = input("Que veux tu faire ? ").upper()

# execute action
    ExecutePlayerAction(Action)
    Clear.ClearConsole()
    GettingMap.DrawMap()
    print(Variables.GameMessage)
    GettingPlayer.GivingPlayersStats()
    GettingPlayer.PlayersDeath()

def ExecutePlayerAction(Action):
    """
        Executes choosen action
    """
    
    # store new Player position
    Variables.NewPlayerPositionX = Variables.PlayerPosition["X"]
    Variables.NewPlayerPositionY = Variables.PlayerPosition["Y"]

    # prepare action
    if Action == "Z": #UP
        Variables.NewPlayerPositionY -= 1
        Variables.GameMessage = f"\nTu te déplaces vers le Nord {GettingMap.MapElements[Variables.MapMap[Variables.NewPlayerPositionY][Variables.NewPlayerPositionX]]['Message']}\n"
        Movement()
        Variables.GameProgression += 1
    elif Action == "S": #DOWN
        Variables.NewPlayerPositionY += 1
        Variables.GameMessage = f"\nTu te déplaces vers le Sud {GettingMap.MapElements[Variables.MapMap[Variables.NewPlayerPositionY][Variables.NewPlayerPositionX]]['Message']}\n"
        Movement()
        Variables.GameProgression += 1
    elif Action == "Q": #LEFT
        Variables.NewPlayerPositionX -= 1
        Variables.GameMessage = f"\nTu te déplaces vers l'Ouest {GettingMap.MapElements[Variables.MapMap[Variables.NewPlayerPositionY][Variables.NewPlayerPositionX]]['Message']}\n"
        Movement()
        Variables.GameProgression += 1
    elif Action == "D": #RIGHT
        Variables.NewPlayerPositionX += 1
        Variables.GameMessage = f"\nTu te déplaces vers l'Est' {GettingMap.MapElements[Variables.MapMap[Variables.NewPlayerPositionY][Variables.NewPlayerPositionX]]['Message']}\n"
        Movement()
        Variables.GameProgression += 1
    elif Action == "R": #REST
        Variables.GameMessage = "\nTu te reposes pendant une heure\n"
        Resting()
        Variables.GameProgression += 1
    elif Action == "I": #INVENTORY
        print("\nDans ton sac il y a:\n")
        Inventory.GetObjectInBag()
        Inventory.ShowInventory()
        IdEntered = input("Pour intéragir avec un objet, tapes son ID (X.X) sinon appuie sur Enter ") 
        Inventory.UseObject(IdEntered)
    elif Action == "MAP": #MAP
        Variables.GameMessage = f"\nTu regardes la carte et sa légende\n {GettingMap.MapsLegend} \n"
        input("\n")
    elif Action == "HELP": #HELP
        Variables.GameMessage = f"\nZ pour aller vers le Nord, S pour le Sud, D pour l'Est et Q pour l'Ouest\nR pour vous reposer, I pour consulter votre Inventaire, MAP pour ouvrir la légende de la carte\n SAVE pour sauvegarder la partie et LOAD pour en charger une\n {input()} \n"
    elif Action == "SAVE": #SAVE
        SavingProgress()
        input("\n")
    elif Action == "LOAD": #LOAD
        LoadingProgress()
        input("\n")
    ##### CHEATING IS BAD !!! #####
    elif Action == "JIJICESAR": #GO TO CESAR (Y=3,X=35)
        Variables.NewPlayerPositionY = 3
        Variables.NewPlayerPositionX = 35
        input("\n")
    elif Action == "JIJISPHINX": #GO TO SPHINX (Y=5,X=74)
        Variables.NewPlayerPositionY = 5
        Variables.NewPlayerPositionX = 74
        input("\n")
    elif Action == "JIJIBUZZ": #GO TO FIZZBUZZ (Y=20,X=8)
        Variables.NewPlayerPositionY = 20
        Variables.NewPlayerPositionX = 8
        input("\n")
    elif Action == "JIJIDOOR": #GO TO THE BIG DOOR (Y=2,X=20)
        Variables.NewPlayerPositionY = 2
        Variables.NewPlayerPositionX = 20
        input("\n")
    elif Action == "JIJIRAIDEBOULE": #GET TO MAX STATS
        Variables.Santé = Variables.MaxStats
        Variables.Faim = Variables.MaxStats
        Variables.Soif = Variables.MaxStats
        input("\n")
    elif Action == "JIJIKEYKEYKEY": #GET ALL THE KEYS
        Inventory.Keys["2.1"][2] = True
        Inventory.Keys["2.2"][2] = True 
        Inventory.Keys["2.3"][2] = True
        input("\n")        
    print(Variables.GameMessage)
        

    # check if action is allowed
    if not GettingMap.MapElements[
        Variables.MapMap[Variables.NewPlayerPositionY][Variables.NewPlayerPositionX]]["CanWalk"]:
        # new position blocks movement, can't move
        Variables.GameMessage = f"\n{GettingMap.MapElements[Variables.MapMap[Variables.NewPlayerPositionY][Variables.NewPlayerPositionX]]['Message']} !\n"
        print(Variables.GameMessage)
        return

    # execute action
    Variables.PlayerPosition["X"] = Variables.NewPlayerPositionX
    Variables.PlayerPosition["Y"] = Variables.NewPlayerPositionY
    ActiveDoors(Variables.PlayerPosition["Y"],Variables.PlayerPosition["X"])
    ActiveBottle(Variables.PlayerPosition["Y"],Variables.PlayerPosition["X"])
    ActiveObject(Variables.PlayerPosition["Y"],Variables.PlayerPosition["X"])