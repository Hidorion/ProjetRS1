if __name__ == "__main__":
    pass

##### IMPORT LOCAL #####

import Variables
import Clear
import GettingPlayer
import GettingMap
import Actions

##### IMPORT MODULE #####


##### INITIALIZING #####

Variables.PlayerName = GettingPlayer.GettingPlayersName()
GettingPlayer.GivingPlayerGlobalStatue()

##### MAP & ACTIONS #####

GettingMap.LoadMapFromFile("map.txt")
GettingMap.DoorSpawn()
Clear.ClearConsole()
GettingMap.DrawMap()
while Variables.GameInProgress:
    Actions.GetPlayerAction()