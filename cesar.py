#import

import Variables
import Clear
import random

import Inventory

def RandomCredo():
    """
        Cette fonction permet d'afficher la porte au départ avec une clé générée aléatoirement
    """
    CredoARandom = "ZEN DE PYTHON"
    CredoRandom = []
    CodageCR = Alphabet.index(Alphabet[random.randint(0,24)])
    CodageCR = int(CodageCR)
    for i in range(len(CredoARandom)): 
        
        if CredoARandom[i] == " ":                 #Si il y a un espace, on garde l'espace
            CredoRandom.append(" ")
        
        else:
            CredoRandom.append(Alphabet.index(CredoARandom[i])) #Sinon on met la lettre
    
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
    
        #Rules
    Rules = "\n┌─────────────────────────────────────────────────┐\n│Bonjour explorateur !                            │\n│Trouve la clé qui rendrait le message clair.     │\n│Utilise la pour me dire comment on t'appelle.    │\n│Je rendrais à César ce qui appartient à César.   │\n│Et à toi, la clé d'Argent.                       │\n│Ecris une lettre et observe.                     │\n│Quand tu te sens prêt, entre le code.            │\n│Si tu écris plus d'une lettre,                   │\n│je considère que tu tentes d'entrer le code.     │\n│Bon courage ! Observe et la clé est à Toi !      │\n└─────────────────────────────────────────────────┘\n" 

    #Un peu de couleur maintenant qu'on gère#
    ColourStart = "\u001b[31m"
    ColourEnd = "\u001b[0m"

    #On lance les fonctions pour le jeu en amont#

    #Door#
    Door = f"\n░░░░░░░░░░░░░░░░░░░░░░░\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n▒KZA-{ColourStart}{CredoARandom}{ColourEnd}-NGF▒\n░LSO╔══════╤══════╗BBQ░\n▒OXC║      │░     ║PBA▒\n░ZAQ║      │░     ║DYT░\n▒VQE║      │░     ║RHR▒\n░GWS║      │░     ║FND░\n▒YEG║      │░     ║TUX▒\n░BDU║      │░     ║HJE░\n▒HCI║      │░     ║VIS▒\n░URW║      │░     ║JKW░\n▒PFK║      │░     ║XLI▒\n░MVY║      │░     ║LPJ░\n▒CTM║______│░_____║ZMN▒\n"

    #On balance les règles, la porte et le jeu
    print(Rules)
    Passe = input("Appuyez sur Enter pour continuer ")
    print(Door)
    return CredoARandom

def PlayersNameCesar(PlayerName,Key,CodagePN):
    """
        Cette fonction permet de changer votre nom en fonction de la clé entré
    """
    PlayerName = list(PlayerName)
    PlayerNameEnco = []
    CodagePN = Alphabet.index(Key)+ 1  #On compare l'Alphabet et le Codage
    CodagePN = int(CodagePN)
    for i in range(len(PlayerName)): 
        CodagePN = Alphabet.index(Key)+ 1  #On compare l'Alphabet et le Codage
        CodagePN = int(CodagePN)
        if PlayerName[i] == " ":                 #Si il y a un espace, on garde l'espace
            PlayerNameEnco.append(" ")
        
        else:
            PlayerNameEnco.append(Alphabet.index(PlayerName[i])) #Sinon on met la lettre
    
    for j in range(len(PlayerNameEnco)):
        
        if PlayerNameEnco[j] == " " or PlayerNameEnco[j] == "-":             #Si il y a un espace, on garde l'espace
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
    """
        Cette fonction permet d'afficher le jeu.
    """
    Credo = RandomCredo()
    Credo = list(Credo)  #On l'a modifie en liste
    LastKey = Alphabet.index(Alphabet[random.randint(0,24)]) # empêche de rentrer la solution dès le premier coup sans essayer
    Codage = random.randint(0,24)                            # idem
    Game = "Lost"
    while Game == "Lost": #Condition de victoire rempli ou non 
        CredoEncode = [] #Crédo codé avec la clé entrée par le joueur
        while True:
            try:                    #On met le système d'exception fraichement appris
                ClefCodage = str(input("Entrez une lettre, ou la réponse à l'énigme "))
                ClefCodage = ClefCodage.upper()  #On demande une lettre, on l'upper pour matcher avec la liste
                if len(ClefCodage) == 1:
                    Codage = Alphabet.index(ClefCodage) + 1  #On compare l'Alphabet et le Codage
                    Codage = int(Codage)
                    LastKey = ClefCodage
                if len(ClefCodage) > 1 :
                    PlayersNameCode = PlayersNameCesar(Variables.PlayerName,LastKey,Codage)
                    PlayersNameCodeFinal = PlayersNameCode.upper()
                    if ClefCodage == PlayersNameCodeFinal:                 #Si le joueur entre plus d'une lettre c'est qu'on considère qu'il tente de rentrer la solution
                        
                        Game = "Won"                    #Si il a réussi, c'est gagné !
                        break
                break
            except ValueError:
                print("Je n'ai pas pu reconnaitre votre lettre, applique toi s'il te plait")
        for i in range(len(Credo)): 
            
            if Credo[i] == " ":                 #Si il y a un espace, on garde l'espace
                CredoEncode.append(" ")
            
            else:
                CredoEncode.append(Alphabet.index(Credo[i])) #Sinon on met la lettre
        
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
        ColourStart = "\u001b[31m"
        ColourEnd = "\u001b[0m"
        print(f"\n░░░░░░░░░░░░░░░░░░░░░░░\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n▒KZA-{ColourStart}{Credo}{ColourEnd}-NGF▒\n░LSO╔══════╤══════╗BBQ░\n▒OXC║      │░     ║PBA▒\n░ZAQ║      │░     ║DYT░\n▒VQE║      │░     ║RHR▒\n░GWS║      │░     ║FND░\n▒YEG║      │░     ║TUX▒\n░BDU║      │░     ║HJE░\n▒HCI║      │░     ║VIS▒\n░URW║      │░     ║JKW░\n▒PFK║      │░     ║XLI▒\n░MVY║      │░     ║LPJ░\n▒CTM║______│░_____║ZMN▒\n")

    print("La porte s'ouvre et devant, sur une pierre taillée, une clé argentée y est posée. Tu la récupères.\n") #Bien joué
    Inventory.Keys["3.2"][2] = True
#Base#Trouve la clé qui rendrait le message clair. Utilise là pour me dire comment on t'appelle. \nAinsi, je rendrais à César ce qui appartient à César. Et à toi, la clé d'Argent.
Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]











