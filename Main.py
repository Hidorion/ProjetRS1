if __name__ == "__main__":
    pass

#ImportLocal
import Readme
import Variables
import Doors
import GettingPlayer
import TheMap
import GettingMap
#ImportModules


#Showing Rules
#Readme.GettingRules()

#Getting Name
#GettingPlayer.GettingPlayersName()
#Giving infos
#Readme.GettingInfo()

#TheMap.printmap()

GettingMap.LoadMapFromFile("map.txt")
GettingMap.DrawMaze()