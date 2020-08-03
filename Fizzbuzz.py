import random
import Inventory
import Variables
import time

def Singe (message,Pos,TheListOfPlayers):
    """
        This function manage the Monkeys' answer
    """
    if "Singe" in TheListOfPlayers[Pos]:
        CheckIfCorrect = random.randint(1,100)
        if CheckIfCorrect <= 33:
            print(f"{TheListOfPlayers[Pos]} dit : {message} !!")
        else:
            print(f"{TheListOfPlayers[Pos]} ne dit pas {message} et se trompe, la hooonte")
            Delete = TheListOfPlayers.pop(Pos)

def Gorille (message,Pos,TheListOfPlayers):
    """
        This function manage the Gorillas' answer
    """
    if "Gorille" in TheListOfPlayers[Pos]:
        CheckIfCorrect = random.randint(1,100)
        if CheckIfCorrect <= 50:
            print(f"{TheListOfPlayers[Pos]} dit : {message} !!")
        else:
            print(f"{TheListOfPlayers[Pos]} ne dit pas {message} se trompe, la hooonte")
            Delete = TheListOfPlayers.pop(Pos)

def Joueur (message,Pos,TheListOfPlayers):
    """
        This function manage the Player's answer
    """
    if Variables.PlayerName in TheListOfPlayers[Pos]:
        CheckIfCorrect = random.randint(1,100)
        if CheckIfCorrect <= 75:
            print(f"{TheListOfPlayers[Pos]} dit : {message} !!")
        else:
            print(f"{TheListOfPlayers[Pos]} ne dit pas {message} se trompe, la hooonte")
            Delete = TheListOfPlayers.pop(Pos)
            

def FizzBuzzGame(TheListOfPlayers):
    """
        This function starts the game
    """
    TheListOfPlayers.append(Variables.PlayerName)
    Stats = "Ongoing"
    PosInList = 0
    Turn = 1
    Variables.GameProgression += 1
    while Variables.PlayerName in TheListOfPlayers:
        time.sleep(1)

        if PosInList > len(TheListOfPlayers)-1:
            PosInList = 0
        
        if Turn %3 == 0 and Turn %5 == 0 : #If we can divide by 3 and 5
            
            Singe("Fizz Buzz",PosInList,TheListOfPlayers)
            Gorille("Fizz Buzz",PosInList,TheListOfPlayers)
            Joueur("Fizz Buzz",PosInList,TheListOfPlayers)    
        
        elif Turn %3 == 0: #If we can divide by 3
            
            Singe("Fizz",PosInList,TheListOfPlayers)
            Gorille("Fizz",PosInList,TheListOfPlayers)
            Joueur("Fizz",PosInList,TheListOfPlayers)    
        
        elif Turn %5 == 0: #If we can divide by 5
            
            Singe("Buzz",PosInList,TheListOfPlayers)
            Gorille("Buzz",PosInList,TheListOfPlayers)
            Joueur("Buzz",PosInList,TheListOfPlayers)    
        
        else: #Other but not by 3 or 5
            
            Singe(Turn,PosInList,TheListOfPlayers)
            Gorille(Turn,PosInList,TheListOfPlayers)
            Joueur(Turn,PosInList,TheListOfPlayers)    
        
        PosInList = PosInList + 1 #Next player please
        
        Turn = Turn + 1 #keep counting

        if len(TheListOfPlayers) == 1 and TheListOfPlayers[0] == Variables.PlayerName: #If the last player is the Player
            print("C'est gagné")
            Stats = "Won"
            break  
    
        Stats = "Lost"
    
    if Stats == "Won":
        print("Félicitations, vous obtenez la clé en \u001b[38;5;220mOr\u001b[0m !")  #Golden key in your pocket !
        Inventory.Keys["2.3"][2] = True
        print("La tribu te félicite et t'invite à un banquet, il te laisse même utiliser leur hamac pour te reposer")
        Variables.Santé = Variables.MaxStats
        Variables.Faim = Variables.MaxStats
        Variables.Soif = Variables.MaxStats
    if Stats == "Lost" :    #If Player lost the game
        replay = input("Tu as perdu, veux tu rejouer ? Oui ou non ? ").upper()   #Try again ?
        if replay == "OUI":
            print("C'est reparti, tout le monde reprend sa place") #Shit, here we go again
            ListOfPlayersReplay = []
            del ListOfPlayersReplay[:]   #We refresh the list
            ListOfPlayersReplay = ["Singe Agile", "Singe Marrant", "Singe Sage", "Singe Grand", "Singe Mince", "Chef Gorille", "Singe Farceur", "Singe énieur", "Singe Comunimaj", "Garo Gorille"]
            FizzBuzzGame(ListOfPlayersReplay)
    print()

ListOfPlayers = ["Singe Agile", "Singe Marrant", "Singe Sage", "Singe Grand", "Singe Mince", "Chef Gorille", "Singe Farceur", "Singe énieur", "Singe Comunimaj", "Garo Gorille"]



