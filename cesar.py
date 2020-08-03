##### DATA #####
import Variables
import Clear
import Inventory

##### MODULES #####
import random



def RandomCredo():
    """
        Cette fonction permet d'afficher la porte au départ avec une clé générée aléatoirement
    """
    CredoARandom = "ZEN DE PYTHON"
    CredoRandom = []
    CodageCR = Alphabet.index(Alphabet[random.randint(0,24)])
    CodageCR = int(CodageCR)
    for i in range(len(CredoARandom)): 
        
        if CredoARandom[i] == " ":                 #If there is a blank, we keep it
            CredoRandom.append(" ")
        
        else:
            CredoRandom.append(Alphabet.index(CredoARandom[i])) #We put a letter
    
    for j in range(len(CredoRandom)):
        
        if CredoRandom[j] == " ":             #If there is a blank, we keep it
            CredoRandom[j] = " "
        
        else:
            Clef = CredoRandom[j] + CodageCR    #From the letter from the credo, we take the value from the list index and we had the one we get
        
            if Clef >= len(Alphabet):           #We reduce if too big
                Clef = Clef - len(Alphabet)
            
            elif Clef <= 0:                     #We grow it if too small
                Clef = len(Alphabet) - Clef
            
            CredoRandom[j] = Alphabet[Clef] #We got the new credo
    
    CredoARandom = CredoRandom
    CredoARandom = "".join(CredoARandom) #Changing the list to a string
    
    ##### Rules #####
    Rules = "\n┌─────────────────────────────────────────────────┐\n│Bonjour explorateur !                            │\n│Trouve la clé qui rendrait le message clair.     │\n│Utilise la pour me dire comment on t'appelle.    │\n│Je rendrais à César ce qui appartient à César.   │\n│Et à toi, la clé d'Argent.                       │\n│Ecris une lettre et observe.                     │\n│Quand tu te sens prêt, entre le code.            │\n│Si tu écris plus d'une lettre,                   │\n│je considère que tu tentes d'entrer le code.     │\n│Bon courage ! Observe et la clé est à Toi !      │\n└─────────────────────────────────────────────────┘\n" 

    ##### Now that we nail it, we add some colours #####
    ColourStart = "\u001b[31m"
    ColourEnd = "\u001b[0m"

    ##### Door #####
    Door = f"\n░░░░░░░░░░░░░░░░░░░░░░░\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n▒KZA-{ColourStart}{CredoARandom}{ColourEnd}-NGF▒\n░LSO╔══════╤══════╗BBQ░\n▒OXC║      │░     ║PBA▒\n░ZAQ║      │░     ║DYT░\n▒VQE║      │░     ║RHR▒\n░GWS║      │░     ║FND░\n▒YEG║      │░     ║TUX▒\n░BDU║      │░     ║HJE░\n▒HCI║      │░     ║VIS▒\n░URW║      │░     ║JKW░\n▒PFK║      │░     ║XLI▒\n░MVY║      │░     ║LPJ░\n▒CTM║______│░_____║ZMN▒\n"

    ##### Giving the Rules #####
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
    CodagePN = Alphabet.index(Key)+ 1  #We compare the alphabet and the code
    CodagePN = int(CodagePN)
    for i in range(len(PlayerName)): 
        CodagePN = Alphabet.index(Key)+ 1  #We compare the alphabet and the code
        CodagePN = int(CodagePN)
        if PlayerName[i] == " ":                 #If there is a blank, we keep it
            PlayerNameEnco.append(" ")
        
        else:
            PlayerNameEnco.append(Alphabet.index(PlayerName[i])) #We put a letter
    
    for j in range(len(PlayerNameEnco)):
        
        if PlayerNameEnco[j] == " " or PlayerNameEnco[j] == "-":             #If there is a blank, we keep it
            PlayerNameEnco[j] = " "
        
        else:
            Clef = PlayerNameEnco[j] + CodagePN    #From the letter from the credo, we take the value from the list index and we had the one we get
        
            if Clef >= len(Alphabet):           #We reduce if too big
                Clef = Clef - len(Alphabet)
            
            elif Clef <= 0:                     #We grow it if too small
                Clef = len(Alphabet) - Clef
            
            PlayerNameEnco[j] = Alphabet[Clef] #We got the new credo
    
    PlayerName = PlayerNameEnco
    PlayerName = "".join(PlayerName) #Changing the list to a string
    return PlayerName

def CesarGame():
    """
        Cette fonction permet d'afficher le jeu.
    """
    Variables.GameProgression += 1
    Credo = RandomCredo()
    Credo = list(Credo)  #We change in to a list
    LastKey = Alphabet.index(Alphabet[random.randint(0,24)]) # We don't want the player to enter the solution directly
    Codage = random.randint(0,24)                            # idem
    Game = "Lost"
    while Game == "Lost": #Victory condition
        CredoEncode = [] #Coded Credo
        while True:
            try:                    #Exceptions
                ClefCodage = str(input("Entrez une lettre, ou la réponse à l'énigme "))
                ClefCodage = ClefCodage.upper()  #Get the letter and upper it
                if len(ClefCodage) == 1:
                    Codage = Alphabet.index(ClefCodage) + 1  #We compare the alphabet and the code
                    Codage = int(Codage)
                    LastKey = ClefCodage
                if len(ClefCodage) > 1 :
                    PlayersNameCode = PlayersNameCesar(Variables.PlayerName,LastKey,Codage)
                    PlayersNameCodeFinal = PlayersNameCode.upper()
                    if ClefCodage == PlayersNameCodeFinal:                 #If more than a letter is entred we compare to the solution
                        
                        Game = "Won"                    #If it succeeds, it's won
                        break
                break
            except ValueError:
                print("Je n'ai pas pu reconnaitre votre lettre, applique toi s'il te plait")
        for i in range(len(Credo)): 
            
            if Credo[i] == " ":                 #If there is a blank, we keep it
                CredoEncode.append(" ")
            
            else:
                CredoEncode.append(Alphabet.index(Credo[i])) #We put a letter
        
        for j in range(len(CredoEncode)):
            
            if CredoEncode[j] == " ":             #If there is a blank, we keep it
                CredoEncode[j] = " "
            
            else:
                Clef = CredoEncode[j] + Codage    #From the letter from the credo, we take the value from the list index and we had the one we get
            
                if Clef >= len(Alphabet):           #We reduce if too big
                    Clef = Clef - len(Alphabet)
                
                elif Clef <= 0:                     #We grow it if too small
                    Clef = len(Alphabet) - Clef
                
                CredoEncode[j] = Alphabet[Clef] #We got the new credo
        
        Credo = CredoEncode
        Credo = "".join(Credo) #Changing the list to a string

    ##### We print the door we the new credo #####
        Clear.ClearConsole()
        ColourStart = "\u001b[31m"
        ColourEnd = "\u001b[0m"
        print(f"\n░░░░░░░░░░░░░░░░░░░░░░░\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n▒KZA-{ColourStart}{Credo}{ColourEnd}-NGF▒\n░LSO╔══════╤══════╗BBQ░\n▒OXC║      │░     ║PBA▒\n░ZAQ║      │░     ║DYT░\n▒VQE║      │░     ║RHR▒\n░GWS║      │░     ║FND░\n▒YEG║      │░     ║TUX▒\n░BDU║      │░     ║HJE░\n▒HCI║      │░     ║VIS▒\n░URW║      │░     ║JKW░\n▒PFK║      │░     ║XLI▒\n░MVY║      │░     ║LPJ░\n▒CTM║______│░_____║ZMN▒\n")

    print("La porte s'ouvre et devant, sur une pierre taillée, la clé \u001b[38;5;249mArgent\u001b[0m y est posée. Tu la récupères.\n") #Well done
    Inventory.Keys["2.2"][2] = True
#Base#Trouve la clé qui rendrait le message clair. Utilise là pour me dire comment on t'appelle. \nAinsi, je rendrais à César ce qui appartient à César. Et à toi, la clé d'Argent.
Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]











