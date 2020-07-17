import random
import Inventory
##############################On imprime le beau sphinx####################################
def LoadMapFromFile(FileName):
    """
        Loads a generic map from specified file name
    """
    with open(FileName, "r", encoding="utf-8") as MyFile:
            Y = 0
            for Line in MyFile:
                Columns = []
                X = 0
                for Character in Line:
                    if Character == "\n": # ignore line ends
                        continue
                    Columns.append(Character) # add character to map
                    X += 1
                Sphinx.append(Columns) # add line to map
                Y += 1

def DrawMap():
    """
        Draw Map on console from 2 dimensional list
    """
    for Y in range(len(Sphinx)):
        for X in range(len(Sphinx[Y])):        
            print(f'{Sphinx[Y][X]}', end="" )
        print()
#######################################################################################


def MagicNumber (): #Le jeu du numéro mystérieux
    ToGuess = random.randint(1,100) #Le "sphinx" choisit un nombre
    NbEssai = 1  #Pour savoir ou on en est
    Guess = False
    Try = input(f"Votre essai numéro {NbEssai} est ")
    if Try.isdigit :     #On fait en sorte que le joueur donne des nombres
        Try = int(Try)
    else :    
        Try = 0      #Sinon il perd un tour bêtement
        print(NotInt)
    while Try != ToGuess or NbEssai == 20:
        if NbEssai < 21 and Guess == False:
            if Try < ToGuess:
                print("Il faut chercher plus haut")  #C'est plus !
                NbEssai += 1
                Try = input(f"Votre essai numéro {NbEssai} est ")
                if Try.isdigit :
                    Try = int(Try)
                else :    
                    Try = 0
                    print(NotInt)
            elif Try > ToGuess:
                print("Il faut chercher plus bas") #C'est moins !
                NbEssai += 1
                Try = input(f"Votre essai numéro {NbEssai} est ")
                if Try.isdigit :
                    Try = int(Try)
                else :    
                    Try = 0
                    print(NotInt)
            else:
                Guess = True
        elif NbEssai >= 20 and Guess == False:    #Si on est nul, on peut retenter
            print("C'est perdu, il faut recommencer")   
            YorN = input("Voulez vous recommencer ? Y/N ")
            if YorN == "Y" or YorN == "y":
                print(SphinxRules)
                MagicNumber()
            else:
                print("Très bien, au revoir !") #Mauvais joueur !
    print ("Bien joué")
    return True
        #les variables et des blablas, tout tient sur cette page pour éviter d'avoir 15 000 page.py"

#les règles expliquées rapidement
SphinxRules = "J'ai choisi un nombre entre 1 et 100 (inclus).\nSi tu le trouves en moins de 20 coups, la Clé de \u001b[38;5;136mBronze\u001b[0m est à Toi !"
#Message explicite
NotInt = "Vous devriez essayer avec des nombres entiers positifs"
Sphinx = [] #Pour passer le sphinx en liste à 2D
LoadMapFromFile("Sphinx.txt") #On va chercher le beau sphinx
DrawMap() #on le dessine
input("Pour continuer, appuie sur ""Enter"" ") #On fait en sorte que le joueur puisse bien comprendre le système de clés
print(SphinxRules) #On affiche les règles
Alors = MagicNumber() #On lance la partie !

if Alors:
    Inventory.Keys["3.1"][2] = True



print(Inventory.Keys["3.1"])

