if __name__ == "__main__":
    pass

#ImportLocal
import Readme
import Variables
import Clear
import GettingPlayer
import GettingMap
#ImportModules


#Showing Rules
#Readme.GettingRules()

#Getting Name
#GettingPlayer.GettingPlayersName()
#Giving infos
#Readme.GettingInfo()



GettingMap.LoadMapFromFile("map.txt")
GettingMap.DoorSpawn()
Clear.ClearConsole()
GettingMap.DrawMap()
