#import
import GettingPlayer
import Clear
Rules = "Trouve la clé qui rendrait le message clair. Utilise là pour me dire comment on t'appelle. \nAinsi, je rendrais à César ce qui appartient à César. Et à toi, la clé d'Argent." 
Alphabet = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ColourStart = "\u001b[31m"
ColourEnd = "\u001b[0m"
Credo = "bgp fg ravjqp"
CredoCode = []
#print(Rules)
#Passe = input("Appuyez sur Enter pour continuer ")
print(f"\n░░░░░░░░░░░░░░░░░░░░░░░\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n▒KZA-{ColourStart}{Credo}{ColourEnd}-NGF▒\n░LSO╔══════╤══════╗BBQ░\n▒OXC║      │░     ║PBA▒\n░ZAQ║      │░     ║DYT░\n▒VQE║      │░     ║RHR▒\n░GWS║      │░     ║FND░\n▒YEG║      │░     ║TUX▒\n░BDU║      │░     ║HJE░\n▒HCI║      │░     ║VIS▒\n░URW║      │░     ║JKW░\n▒PFK║      │░     ║XLI▒\n░MVY║      │░     ║LPJ░\n▒CTM║______│░_____║ZMN▒\n")
GettingPlayer.PlayersName = "Alex"
Credo = list(Credo)
ClefCodage = str(input("Entrez une lettre, ou la réponse à l'énigme "))
Clear.ClearConsole()
while ClefCodage != GettingPlayer.PlayersName:
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
            if Clef > len(Alphabet):
                Clef = Clef - len(Alphabet)
            else:
                CredoCode[j] = Alphabet[Clef]
    CredoCode = "".join(CredoCode)
    print(f"\n░░░░░░░░░░░░░░░░░░░░░░░\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n▒KZA-{ColourStart}{CredoCode}{ColourEnd}-NGF▒\n░LSO╔══════╤══════╗BBQ░\n▒OXC║      │░     ║PBA▒\n░ZAQ║      │░     ║DYT░\n▒VQE║      │░     ║RHR▒\n░GWS║      │░     ║FND░\n▒YEG║      │░     ║TUX▒\n░BDU║      │░     ║HJE░\n▒HCI║      │░     ║VIS▒\n░URW║      │░     ║JKW░\n▒PFK║      │░     ║XLI▒\n░MVY║      │░     ║LPJ░\n▒CTM║______│░_____║ZMN▒\n")
    ClefCodage = str(input("Entrez une lettre, ou la réponse à l'énigme "))


