if __name__ == "__main__":
    pass

##### IMPORT LOCAL #####

import Variables
import Clear
import GettingPlayer
import GettingMap
import Actions
import Menu

##### IMPORT MODULE #####

##### MENU #####

Menu.MenuPrint()
Choice = input("\nChoisir une option : ")
Clear.ClearConsole()
if Choice == "2": #Load Game
    Actions.LoadingProgress()
    Variables.PlayerPosition["X"] = Variables.NewPlayerPositionX
    Variables.PlayerPosition["Y"] = Variables.NewPlayerPositionY
    GettingMap.DoorSpawn()
    GettingMap.ObjectsSpawn()
    Clear.ClearConsole()
    GettingMap.DrawMap()
    GettingPlayer.GivingPlayersStats()          
else : #Newgame
    
    ##### INITIALIZING #####

    Variables.PlayerName = GettingPlayer.GettingPlayersName()
    GettingPlayer.GivingPlayerGlobalStatue()

    ##### MAP & ACTIONS #####
    GettingMap.LoadMapFromFile("Text\map.txt")
    GettingMap.DoorSpawn()
    GettingMap.ObjectsSpawn()
    Clear.ClearConsole()
    GettingMap.DrawMap()
while Variables.GameInProgress:
    Actions.GetPlayerAction()
