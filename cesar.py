#import
import GettingPlayer
import Clear


def CesarGame ():
    #Rules
    Rules = "\n┌─────────────────────────────────────────────────┐\n│Bonjour explorateur !                            │\n│Trouve la clé qui rendrait le message clair.     │\n│Utilise là pour me dire comment on t'appelle.    │\n│Je rendrais à César ce qui appartient à César.   │\n│Et à toi, la clé d'Argent.                       │\n│Ecris une lettre et observe.                     │\n│Quand tu te sens prêt, entre le code.            │\n│Si tu écris plus d'une lettre,                   │\n│Je considère que tu tentes d'entre le code.      │\n│Bon courage ! Observe et la clé est à Toi !      │\n└─────────────────────────────────────────────────┘\n" 

    #Base#Trouve la clé qui rendrait le message clair. Utilise là pour me dire comment on t'appelle. \nAinsi, je rendrais à César ce qui appartient à César. Et à toi, la clé d'Argent.
    Alphabet = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    #Un peu de couleur maintenant qu'on gère#
    ColourStart = "\u001b[31m"
    ColourEnd = "\u001b[0m"

    #Zen de Python Cesarié ;)#
    Credo = "BGP FG RAVJQP"

    #Door#
    Door = f"\n░░░░░░░░░░░░░░░░░░░░░░░\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n▒KZA-{ColourStart}{Credo}{ColourEnd}-NGF▒\n░LSO╔══════╤══════╗BBQ░\n▒OXC║      │░     ║PBA▒\n░ZAQ║      │░     ║DYT░\n▒VQE║      │░     ║RHR▒\n░GWS║      │░     ║FND░\n▒YEG║      │░     ║TUX▒\n░BDU║      │░     ║HJE░\n▒HCI║      │░     ║VIS▒\n░URW║      │░     ║JKW░\n▒PFK║      │░     ║XLI▒\n░MVY║      │░     ║LPJ░\n▒CTM║______│░_____║ZMN▒\n"

    #On balance les règles, la porte et le jeu
    print(Rules)
    Passe = input("Appuyez sur Enter pour continuer ")
    print(Door)
    Credo = list(Credo)  #On l'a modifie en liste

    #Condition de Victoire ou défaite
    PlayersName = "ALEX" #Modifié en fonctio nde ce qu'a rentré le joueur en début de partie.
    Game = "Lost"
    while Game == "Lost": #Condition de victoire rempli ou non 
        CredoEncode = [] #Crédo codé avec la clé entrée par le joueur
        while True:
            try:                    #On met le système d'exception fraichement appris

                ClefCodage = str(input("Entrez une lettre, ou la réponse à l'énigme "))
                ClefCodage = ClefCodage.upper()  #On demande une lettre, on l'upper pour matcher avec la liste
                    
                if len(ClefCodage) > 1:                 #Si le joueur entre plus d'une lettre c'est qu'on considère qu'il tente de rentrer la solution
                    
                    if ClefCodage == PlayersName :
                        Game = "Won"                    #Si il a réussi, c'est gagné !
                        break
                    
                    else:
                        continue

                Codage = Alphabet.index(ClefCodage, 1)  #On compare l'Alphabet et le Codage
                Codage = int(Codage)
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









