import random
import Inventory
import Variables
import time

def Singe (message,Pos,TheListOfPlayers):
    """
        Cette fonction permet de gérer si les Singe répondent correctement
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
        Cette fonction permet de gérer si les Gorilles répondent correctement
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
        Cette fonction permet de gérer si le joueur répond correctement
    """
    if Variables.PlayerName in TheListOfPlayers[Pos]:
        CheckIfCorrect = random.randint(1,100)
        if CheckIfCorrect <= 75:
            print(f"{TheListOfPlayers[Pos]} dit : {message} !!")
        else:
            print(f"{TheListOfPlayers[Pos]} ne dit pas {message} se trompe, la hooonte")
            Delete = TheListOfPlayers.pop(Pos)
            

def FizzBuzzGame(TheListOfPlayers):
    print("Fonctione appelée \n")
    """
        C'est la fonction pour commencer le jeu
    """
    TheListOfPlayers.append(Variables.PlayerName)
    Stats = "Ongoing"
    PosInList = 0
    Turn = 1
    while Variables.PlayerName in TheListOfPlayers:
        print("Fonctione en marche \n")
        time.sleep(1)

        if PosInList > len(TheListOfPlayers)-1:
            PosInList = 0
        
        if Turn %3 == 0 and Turn %5 == 0 : #Si c'est un multipe de 3 et 5
            
            Singe("Fizz Buzz",PosInList,TheListOfPlayers)
            Gorille("Fizz Buzz",PosInList,TheListOfPlayers)
            Joueur("Fizz Buzz",PosInList,TheListOfPlayers)    
        
        elif Turn %3 == 0: #Si c'est un multipe de 3
            
            Singe("Fizz",PosInList,TheListOfPlayers)
            Gorille("Fizz",PosInList,TheListOfPlayers)
            Joueur("Fizz",PosInList,TheListOfPlayers)    
        
        elif Turn %5 == 0: #Si c'est un multipe de 5
            
            Singe("Buzz",PosInList,TheListOfPlayers)
            Gorille("Buzz",PosInList,TheListOfPlayers)
            Joueur("Buzz",PosInList,TheListOfPlayers)    
        
        else: #Si ce n'est pas un multipe de 3 ou de 5
            
            Singe(Turn,PosInList,TheListOfPlayers)
            Gorille(Turn,PosInList,TheListOfPlayers)
            Joueur(Turn,PosInList,TheListOfPlayers)    
        
        PosInList = PosInList + 1 #On passe au joueur suivant
        
        Turn = Turn + 1 #On continue de compter

        if len(TheListOfPlayers) == 1 and TheListOfPlayers[0] == Variables.PlayerName: #Si il ne reste qu'une personne et que c'est le joueur :
            print("C'est gagné")
            Stats = "Won"
            break  
    
        Stats = "Lost"
    
    if Stats == "Won":
        print("Félicitations, vous obtenez la clé en Or !")  #La clé en or en poche
        Inventory.Keys["3.3"][2] = True
    
    if Stats == "Lost" :    #Si c'est perdu
        replay = input("Tu as perdu, veux tu rejouer ? Oui ou non ? ").upper()   #On retente ?
        if replay == "OUI":
            print("C'est reparti, tout le monde reprend sa place") #Ca repart
            ListOfPlayersReplay = []
            del ListOfPlayersReplay[:]   #On réinitialise la liste
            ListOfPlayersReplay = ["Singe Agile", "Singe Marrant", "Singe Sage", "Singe Grand", "Singe Mince", "Chef Gorille", "Singe Farceur", "Singe énieur", "Singe Comunimaj", "Garo Gorille"]
            FizzBuzzGame(ListOfPlayersReplay)
    print()

ListOfPlayers = ["Singe Agile", "Singe Marrant", "Singe Sage", "Singe Grand", "Singe Mince", "Chef Gorille", "Singe Farceur", "Singe énieur", "Singe Comunimaj", "Garo Gorille"]

#FizzBuzzGame(ListOfPlayers)

