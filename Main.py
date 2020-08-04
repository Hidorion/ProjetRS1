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
Choice = input("\nChoisir une option :")
if Choice != 2:
    pass #Newgame
else :
    Actions.LoadingProgress() #LoadGame



##### INITIALIZING #####

Variables.PlayerName = GettingPlayer.GettingPlayersName()
GettingPlayer.GivingPlayerGlobalStatue()

##### MAP & ACTIONS #####

GettingMap.LoadMapFromFile("Text\map.txt")
GettingMap.DoorSpawn()
Clear.ClearConsole()
GettingMap.DrawMap()
while Variables.GameInProgress:
    Actions.GetPlayerAction()