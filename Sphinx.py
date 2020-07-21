import random
import Inventory
import Variables

##############################On imprime le beau sphinx####################################
def SphinxPrep(Filename):   
    LoadSphinx(Filename)
    print()
    DrawSphinx()
    
def LoadSphinx(FileName):
    """
        Loads the beautiful Sphinx
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
                Variables.Sphinx.append(Columns) # add line to map
                Y += 1

def DrawSphinx():
    """
        Draw the beautiful Sphinx
    """
    for Y in range(len(Variables.Sphinx)):
        for X in range(len(Variables.Sphinx[Y])):        
            print(f'{Variables.Sphinx[Y][X]}', end="" )
        print()
    
    MagicNumber()
    
#######################################################################################


def MagicNumber(): #Le jeu du numéro mystérieux
    input("Pour continuer, appuie sur ""Entrée"" ")
    SphinxRules = "J'ai choisi un nombre entre 1 et 100 (inclus).\nSi tu le trouves en moins de 20 coups, tu remportes la Clé de \u001b[38;5;136mBronze\u001b[0m !"
    NotInt = "Vous devriez essayer avec des nombres entiers positifs"
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
    print ("Félicitations ! La Clé de \u001b[38;5;136mBronze\u001b[0m est à Toi !")
    Inventory.Keys["3.1"][2] = True
        #les variables et des blablas, tout tient sur cette page pour éviter d'avoir 15 000 page.py"

#les règles expliquées rapidement

#Message explicite

#Sphinx = [] #Pour passer le sphinx en liste à 2D
#SphinxPrep("Sphinx.txt") #On va chercher le beau sphinx

#input("Pour continuer, appuie sur ""Entrée"" ") #On fait en sorte que le joueur puisse bien comprendre le système de clés
#print(SphinxRules) #On affiche les règles


