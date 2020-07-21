import random
import Inventory
import Variables

##### We print the beautiful Sphinx #####
def SphinxPrep(Filename):   
    LoadSphinx(Filename)
    print()
    DrawSphinx()

##### Getting the sphinx #####    
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

##### Drawing the Sphinx #####
def DrawSphinx():
    """
        Draw the beautiful Sphinx
    """
    for Y in range(len(Variables.Sphinx)):
        for X in range(len(Variables.Sphinx[Y])):        
            print(f'{Variables.Sphinx[Y][X]}', end="" )
        print()
    
    MagicNumber()
    


##### Mysterious Number's Game #####
def MagicNumber(): 
    input("Pour continuer, appuie sur ""Entrée"" ")
    SphinxRules = "J'ai choisi un nombre entre 1 et 100 (inclus).\nSi tu le trouves en moins de 20 coups, tu remportes la Clé de \u001b[38;5;136mBronze\u001b[0m !"
    NotInt = "Vous devriez essayer avec des nombres entiers positifs"
    ToGuess = random.randint(1,100) #The "sphinx" picks a number
    NbEssai = 1  #Number of try
    Guess = False
    Try = input(f"Votre essai numéro {NbEssai} est ")
    if Try.isdigit :     #Making player to only give digit
        Try = int(Try)
    else :    
        Try = 0      #Or he just lost a try
        print(NotInt)
    while Try != ToGuess or NbEssai == 20:
        if NbEssai < 21 and Guess == False:
            if Try < ToGuess:
                print("Il faut chercher plus haut")  # More
                NbEssai += 1
                Try = input(f"Votre essai numéro {NbEssai} est ")
                if Try.isdigit :
                    Try = int(Try)
                else :    
                    Try = 0
                    print(NotInt)
            elif Try > ToGuess:
                print("Il faut chercher plus bas") # Less
                NbEssai += 1
                Try = input(f"Votre essai numéro {NbEssai} est ")
                if Try.isdigit :
                    Try = int(Try)
                else :    
                    Try = 0
                    print(NotInt)
            else:
                Guess = True
        elif NbEssai >= 20 and Guess == False:    # If you sucked, you can try again
            print("C'est perdu, il faut recommencer")   
            YorN = input("Voulez vous recommencer ? Y/N ")
            if YorN == "Y" or YorN == "y":
                print(SphinxRules)
                MagicNumber()
            else:
                print("Très bien, au revoir !") # Bye
    print ("Félicitations ! La Clé de \u001b[38;5;136mBronze\u001b[0m est à Toi !")
    Inventory.Keys["3.1"][2] = True



