import random
import Inventory
import Variables


Player = Variables.PlayerName
ListOfPlayers = ["Singe Agile", "Singe Marrant", "Singe Sage", "Singe Grand", "Singe Mince", "Chef Gorille", Player]
PosInList = 0

def Singe (message):
    if "Singe" in ListOfPlayers[PosInList]:
        CheckIfCorrect = random.randint(1,100)
        if CheckIfCorrect < 31:
            print(f"{ListOfPlayers[PosInList]} dit : {message} !!")
        else:
                    print(f"{ListOfPlayers[PosInList]} se trompe, la hooonte")
                    Delete = ListOfPlayers.pop(PosInList)


def Gorille (message):
    if "Gorille" in ListOfPlayers[PosInList]:
        CheckIfCorrect = random.randint(1,100)
        if CheckIfCorrect < 51:
            print(f"{ListOfPlayers[PosInList]} dit : {message} !!")
        else:
                    print(f"{ListOfPlayers[PosInList]} se trompe, la hooonte")
                    Delete = ListOfPlayers.pop(PosInList)



def Joueur (message):
    if Player in ListOfPlayers[PosInList]:
        CheckIfCorrect = random.randint(1,100)
        if CheckIfCorrect < 71:
            print(f"{ListOfPlayers[PosInList]} dit : {message} !!")
        else:
                    print(f"{ListOfPlayers[PosInList]} se trompe, la hooonte")
                    Delete = ListOfPlayers.pop(PosInList)
            
for j in range(50):
    
    if Player not in ListOfPlayers:
        print("Perdu")
        break
        
    if len(ListOfPlayers) == 1 and ListOfPlayers[0] == Player:
        print("C'est gagné")
        break
    
    Turn = j + 1
    
    if PosInList > len(ListOfPlayers)-1:
        PosInList = 0
    
    if Turn %3 == 0 and Turn %5 == 0 :
        
        Singe("Fizz Buzz")
        Gorille("Fizz Buzz")
        Joueur("Fizz Buzz")    
    
    elif Turn %3 == 0:
        
        Singe("Fizz")
        Gorille("Fizz")
        Joueur("Fizz")    
    
    elif Turn %5 == 0:
        
        Singe("Buzz")
        Gorille("Buzz")
        Joueur("Buzz")    
    
    else:
        
        Singe(Turn)
        Gorille(Turn)
        Joueur(Turn)    
    
    PosInList = PosInList + 1

print("Félicitations, vous obtenez la clé en Or !")
Inventory.Keys["3.3"][2] = True