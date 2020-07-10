#import
import GettingPlayer
import Clear


#Rules
Rules = "Trouve la clé qui rendrait le message clair. Utilise là pour me dire comment on t'appelle. \nAinsi, je rendrais à César ce qui appartient à César. Et à toi, la clé d'Argent." 

#Base#
Alphabet = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#Un peu de couleur maintenant qu'on gère#
ColourStart = "\u001b[31m"
ColourEnd = "\u001b[0m"

#Zen de Python Cesarié ;)#
Credo = "BGP FG RAVJQP"


#Crédo codé avec la clé entrée par le joueur
CredoCode = []

#On balance les règles, la porte et le jeu
print(Rules)
Passe = input("Appuyez sur Enter pour continuer ")
print(f"\n░░░░░░░░░░░░░░░░░░░░░░░\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n▒KZA-{ColourStart}{Credo}{ColourEnd}-NGF▒\n░LSO╔══════╤══════╗BBQ░\n▒OXC║      │░     ║PBA▒\n░ZAQ║      │░     ║DYT░\n▒VQE║      │░     ║RHR▒\n░GWS║      │░     ║FND░\n▒YEG║      │░     ║TUX▒\n░BDU║      │░     ║HJE░\n▒HCI║      │░     ║VIS▒\n░URW║      │░     ║JKW░\n▒PFK║      │░     ║XLI▒\n░MVY║      │░     ║LPJ░\n▒CTM║______│░_____║ZMN▒\n")
Credo = list(Credo)  #On l'a modifie en liste

#Condition de Victoire ou défaite
PlayersName = "ALEX" #Modifié en fonctio nde ce qu'a rentré le joueur en début de partie.
Game = "Lost"


while Game == "Lost":
    
    ClefCodage = str(input("Entrez une lettre, ou la réponse à l'énigme "))
    ClefCodage = ClefCodage.upper()
        
    if len(ClefCodage) > 1:   
        if ClefCodage == PlayersName :
            Game = "Won"
            break
        else:
            continue

    Codage = Alphabet.index(ClefCodage, 1)
    Codage = int(Codage)
    
    for i in range(len(Credo)):
        
        if Credo[i] == " ":
            CredoCode.append(" ")
        
        else:
            CredoCode.append(Alphabet.index(Credo[i],1))
    
    for j in range(len(CredoCode)):
        
        if CredoCode[j] == " ":
            CredoCode[j] = " "
        
        else:
            Clef = CredoCode[j] + Codage
        
        if Clef >= len(Alphabet):
            Clef = Clef - len(Alphabet)
        
        CredoCode[j] = Alphabet[Clef] #On effectue le changement du nouveau Crédo en fonction de l'Alphabet
    Credo = CredoCode
    Credo = "".join(Credo) #On remet la liste en string

#On print la porte avec le crédo modifié
    Clear.ClearConsole()
    print(f"\n░░░░░░░░░░░░░░░░░░░░░░░\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n▒KZA-{ColourStart}{Credo}{ColourEnd}-NGF▒\n░LSO╔══════╤══════╗BBQ░\n▒OXC║      │░     ║PBA▒\n░ZAQ║      │░     ║DYT░\n▒VQE║      │░     ║RHR▒\n░GWS║      │░     ║FND░\n▒YEG║      │░     ║TUX▒\n░BDU║      │░     ║HJE░\n▒HCI║      │░     ║VIS▒\n░URW║      │░     ║JKW░\n▒PFK║      │░     ║XLI▒\n░MVY║      │░     ║LPJ░\n▒CTM║______│░_____║ZMN▒\n")

print("You did it mutafukaz") #Bien joué


