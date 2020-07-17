if __name__ == "__main__":
    pass

#ImportLocal

import Variables
import Clear
import GettingPlayer
import GettingMap
import Actions
#ImportModules




#Showing Rules
#Getting Name
Variables.PlayerName = GettingPlayer.GettingPlayersName()
#Giving infos
GettingPlayer.GivingPlayerGlobalStatue()





GettingMap.LoadMapFromFile("map.txt")
GettingMap.DoorSpawn()
Clear.ClearConsole()
GettingMap.DrawMap()
while Variables.GameInProgress:
    Actions.GetCharacterAction()