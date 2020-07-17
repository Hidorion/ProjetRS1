import random
import Inventory
import Variables

def Singe (message,Pos):
    """
        Cette fonction permet de gérer le score du Singe
    """
    if "Singe" in ListOfPlayers[Pos]:
        CheckIfCorrect = random.randint(1,100)
        if CheckIfCorrect < 31:
            print(f"{ListOfPlayers[Pos]} dit : {message} !!")
        else:
            print(f"{ListOfPlayers[Pos]} ne dit pas {message} et se trompe, la hooonte")
            Delete = ListOfPlayers.pop(Pos)

def Gorille (message,Pos):
    """
        Cette fonction permet de gérer le score du Chef
    """
    if "Gorille" in ListOfPlayers[Pos]:
        CheckIfCorrect = random.randint(1,100)
        if CheckIfCorrect < 51:
            print(f"{ListOfPlayers[Pos]} dit : {message} !!")
        else:
            print(f"{ListOfPlayers[Pos]} ne dit pas {message} se trompe, la hooonte")
            Delete = ListOfPlayers.pop(Pos)

def Joueur (message,Pos):
    """
        Cette fonction permet de gérer le score du joueur
    """
    if Player in ListOfPlayers[Pos]:
        CheckIfCorrect = random.randint(1,100)
        if CheckIfCorrect < 71:
            print(f"{ListOfPlayers[Pos]} dit : {message} !!")
        else:
            print(f"{ListOfPlayers[Pos]} ne dit pas {message} se trompe, la hooonte")
            Delete = ListOfPlayers.pop(Pos)
            

def FizzBuzzGame():
    Stats = False
    for j in range(21):
        PosInList = 0
        if Player not in ListOfPlayers:
            print("C'est perdu")
            break
            
        if len(ListOfPlayers) == 1 and ListOfPlayers[0] == Player:
            print("C'est gagné")
            Stats = True
            break
        
        Turn = j + 1
        
        if PosInList > len(ListOfPlayers)-1:
            PosInList = 0
        
        if Turn %3 == 0 and Turn %5 == 0 :
            
            Singe("Fizz Buzz",PosInList)
            Gorille("Fizz Buzz",PosInList)
            Joueur("Fizz Buzz",PosInList)    
        
        elif Turn %3 == 0:
            
            Singe("Fizz",PosInList)
            Gorille("Fizz",PosInList)
            Joueur("Fizz",PosInList)    
        
        elif Turn %5 == 0:
            
            Singe("Buzz",PosInList)
            Gorille("Buzz",PosInList)
            Joueur("Buzz",PosInList)    
        
        else:
            
            Singe(Turn,PosInList)
            Gorille(Turn,PosInList)
            Joueur(Turn,PosInList)    
        
        PosInList = PosInList + 1
    return Stats




Player = Variables.PlayerName
ListOfPlayers = ["Singe Agile", "Singe Marrant", "Singe Sage", "Singe Grand", "Singe Mince", "Chef Gorille", Player]

if FizzBuzzGame():
    print("Félicitations, vous obtenez la clé en Or !")
    Inventory.Keys["3.3"][2] = True
else :
    print("Retente ta chance plus tard")

FizzBuzzGame()