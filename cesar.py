#import
from random import random
import Variables
import Clear
import random
from Variables import PlayerName
import string
def RandomCredo():
    CredoARandom = "ZEN DE PYTHON"
    CredoRandom = []
    CodageCR = Alphabet.index(Alphabet[random.randint(4,9)], 1)
    CodageCR = int(CodageCR)
    for i in range(len(CredoARandom)): 
        
        if CredoARandom[i] == " ":                 #Si il y a un espace, on garde l'espace
            CredoRandom.append(" ")
        
        else:
            CredoRandom.append(Alphabet.index(CredoARandom[i],1)) #Sinon on met la lettre
    
    for j in range(len(CredoRandom)):
        
        if CredoRandom[j] == " ":             #Si il y a un espace, on garde l'espace
            CredoRandom[j] = " "
        
        else:
            Clef = CredoRandom[j] + CodageCR    #La Clef à la valeur dans l'index de la lettre du credo + celle ajoutée
        
            if Clef >= len(Alphabet):           #Si la clef est trop grande on la réduit
                Clef = Clef - len(Alphabet)
            
            elif Clef <= 0:                     #Si elle est trop petite on l'agrandit
                Clef = len(Alphabet) - Clef
            
            CredoRandom[j] = Alphabet[Clef] #On effectue le changement du nouveau Crédo en fonction de l'Alphabet
    
    CredoARandom = CredoRandom
    CredoARandom = "".join(CredoARandom) #On remet la liste en string
    return CredoARandom

def PlayersNameCesar(PlayerName,ClefCodage,CodagePN):
    PlayerName = list(PlayerName)
    PlayerNameEnco = []
    CodagePN = Alphabet.index(ClefCodage, 1)  #On compare l'Alphabet et le Codage
    CodagePN = int(CodagePN)
    for i in range(len(PlayerName)): 
        
        if PlayerName[i] == " ":                 #Si il y a un espace, on garde l'espace
            PlayerNameEnco.append(" ")
        
        else:
            PlayerNameEnco.append(Alphabet.index(PlayerName[i],1)) #Sinon on met la lettre
    
    for j in range(len(PlayerNameEnco)):
        
        if PlayerNameEnco[j] == " " or "-":             #Si il y a un espace, on garde l'espace
            PlayerNameEnco[j] = " "
        
        else:
            Clef = PlayerNameEnco[j] + CodagePN    #La Clef à la valeur dans l'index de la lettre du credo + celle ajoutée
        
            if Clef >= len(Alphabet):           #Si la clef est trop grande on la réduit
                Clef = Clef - len(Alphabet)
            
            elif Clef <= 0:                     #Si elle est trop petite on l'agrandit
                Clef = len(Alphabet) - Clef
            
            PlayerNameEnco[j] = Alphabet[Clef] #On effectue le changement du nouveau Crédo en fonction de l'Alphabet
    
    PlayerName = PlayerNameEnco
    PlayerName = "".join(PlayerName) #On remet la liste en string
    return PlayerName

def CesarGame():
    Credo = RandomCredo()
    Credo = list(Credo)  #On l'a modifie en liste
    Game = "Lost"
    while Game == "Lost": #Condition de victoire rempli ou non 
        CredoEncode = [] #Crédo codé avec la clé entrée par le joueur
        while True:
            try:                    #On met le système d'exception fraichement appris
                ClefCodage = str(input("Entrez une lettre, ou la réponse à l'énigme "))
                ClefCodage = ClefCodage.upper()  #On demande une lettre, on l'upper pour matcher avec la liste
                Codage = Alphabet.index(ClefCodage, 1)  #On compare l'Alphabet et le Codage
                Codage = int(Codage)
                PlayersNameCode = PlayersNameCesar(Variables.PlayerName,ClefCodage,Codage)
                if len(ClefCodage) > 1:                 #Si le joueur entre plus d'une lettre c'est qu'on considère qu'il tente de rentrer la solution
                    
                    if ClefCodage == PlayersNameCode :
                        Game = "Won"                    #Si il a réussi, c'est gagné !
                        break
                    
                    else:
                        continue
                break
            except ValueError:
                print("Je n'ai pas pu reconnaitre votre lettre, applique toi s'il te plait")
        for i in range(len(Credo)): 
            
            if Credo[i] == " ":                 #Si il y a un espace, on garde l'espace
                CredoEncode.append(" ")
            
            else:
                CredoEncode.append(Alphabet.index(Credo[i],1)) #Sinon on met la lettre
        
        for j in range(len(CredoEncode)):
            
            if CredoEncode[j] == " ":             #Si il y a un espace, on garde l'espace
                CredoEncode[j] = " "
            
            else:
                Clef = CredoEncode[j] + Codage    #La Clef à la valeur dans l'index de la lettre du credo + celle ajoutée
            
                if Clef >= len(Alphabet):           #Si la clef est trop grande on la réduit
                    Clef = Clef - len(Alphabet)
                
                elif Clef <= 0:                     #Si elle est trop petite on l'agrandit
                    Clef = len(Alphabet) - Clef
                
                CredoEncode[j] = Alphabet[Clef] #On effectue le changement du nouveau Crédo en fonction de l'Alphabet
        
        Credo = CredoEncode
        Credo = "".join(Credo) #On remet la liste en string

    #On print la porte avec le crédo modifié
        Clear.ClearConsole()
        print(f"\n░░░░░░░░░░░░░░░░░░░░░░░\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n▒KZA-{ColourStart}{Credo}{ColourEnd}-NGF▒\n░LSO╔══════╤══════╗BBQ░\n▒OXC║      │░     ║PBA▒\n░ZAQ║      │░     ║DYT░\n▒VQE║      │░     ║RHR▒\n░GWS║      │░     ║FND░\n▒YEG║      │░     ║TUX▒\n░BDU║      │░     ║HJE░\n▒HCI║      │░     ║VIS▒\n░URW║      │░     ║JKW░\n▒PFK║      │░     ║XLI▒\n░MVY║      │░     ║LPJ░\n▒CTM║______│░_____║ZMN▒\n")

    print("You did it mutafukaz") #Bien joué
#Rules
Rules = "\n┌─────────────────────────────────────────────────┐\n│Bonjour explorateur !                            │\n│Trouve la clé qui rendrait le message clair.     │\n│Utilise là pour me dire comment on t'appelle.    │\n│Je rendrais à César ce qui appartient à César.   │\n│Et à toi, la clé d'Argent.                       │\n│Ecris une lettre et observe.                     │\n│Quand tu te sens prêt, entre le code.            │\n│Si tu écris plus d'une lettre,                   │\n│Je considère que tu tentes d'entre le code.      │\n│Bon courage ! Observe et la clé est à Toi !      │\n└─────────────────────────────────────────────────┘\n" 

#Base#Trouve la clé qui rendrait le message clair. Utilise là pour me dire comment on t'appelle. \nAinsi, je rendrais à César ce qui appartient à César. Et à toi, la clé d'Argent.
Alphabet = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#Un peu de couleur maintenant qu'on gère#
ColourStart = "\u001b[31m"
ColourEnd = "\u001b[0m"

#Zen de Python Cesarié ;)#

#On lance les fonctions pour le jeu en amont#
StartCredo = RandomCredo()

#Door#
Door = f"\n░░░░░░░░░░░░░░░░░░░░░░░\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n▒KZA-{ColourStart}{StartCredo}{ColourEnd}-NGF▒\n░LSO╔══════╤══════╗BBQ░\n▒OXC║      │░     ║PBA▒\n░ZAQ║      │░     ║DYT░\n▒VQE║      │░     ║RHR▒\n░GWS║      │░     ║FND░\n▒YEG║      │░     ║TUX▒\n░BDU║      │░     ║HJE░\n▒HCI║      │░     ║VIS▒\n░URW║      │░     ║JKW░\n▒PFK║      │░     ║XLI▒\n░MVY║      │░     ║LPJ░\n▒CTM║______│░_____║ZMN▒\n"

#On balance les règles, la porte et le jeu
print(Rules)
Passe = input("Appuyez sur Enter pour continuer ")
print(Door)


CesarGame()








