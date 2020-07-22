from tkinter import Variable
import Variables


def GettingPlayersName():    
    """
        On vient demander le prénom du joueur et on vérifie qu'il s'agit bien d'un prénom.
    """
    PlayerName = input("Mais tout d'abord, quel est ton nom ? ")
    PlayerName = PlayerName.upper()
    while not GettingPlayersInfo(PlayerName):
        PlayerName = input("Attends, reprends ton souffle, je t'écoute... : ").strip() #We want to delete extra blanks
    return PlayerName

def GettingRules ():    
    WelcomeText = f"Bienvenue {Variables.PlayerName} sur cette île mystérieuse.\nTu es ici avec un seul et unique but. Réussir à franchir la Grande Porte ! (۩)\nPour cela tu devras réussir à obtenir et assembler 3 clés. Tu les obtiendras en réussisant les 3 challenges de l'île.\nIls sont derrière 3 portes éparpillées sur l'île.\n"
    SurvivalText = "Tu te trouves sur une île pas si paradisiaque.\nAvec les conditions climatiques de l'île, tu risques de te fatiguer et d'avoir faim tout au long de ton parcours\nSans compter sur cette chaleur, tu devras penser à boire et t'hydrater.\nPour faire court, la mort te guette.\nSi ta Soif, ta Faim ou ta Santé tombe à 0, tu mourras et devras tout recommencer.\n"
    print(WelcomeText)
    print()
    print(SurvivalText)

def GettingInfo ():
    CheckTheMap = "Tu as une carte dans ton inventaire. -> I\n"
    CheckYou="Tu es marqué par ce symbole -> ☻\n"
    CheckObjects="Sur la carte, il y a la grande porte -> ۩ puis des objets intéractifs ●\n"
    print(CheckTheMap)
    print(CheckYou)
    print(CheckObjects)

def GivingPlayerGlobalStatue():    
    """
        On fait part au joueur de sa condition.
    """
    print(f"Hoo {Variables.PlayerName} est un jolie nom.\n")
    GettingRules ()
    GettingInfo ()
    print("Tu as eu de la chance, tu as pu être parfaitement reposé, nourri et hydraté avant de t'échouer ici\n")
    print("Tu as actuellement:\n")
    print(" - 100/100 d'énergie.\n")
    print(" - 100/100 de satiété.\n")
    print(" - 100/100 d'hydratation'.\n")
    print("Pour te déplacer :\nZ pour aller vers le Nord, S pour le Sud, D pour l'Est et Q pour l'Ouest. Si tu as besoin d'autres informations écrits : Help\n")
    passer = input("Une fois que tu as bien tout compris, appuies sur Entrée ")

def GettingPlayersInfo (Name):
    """
        C'est ici que la vérification du prénom se fait.
    """
    if Name == "":
        return False
    for Character in Name:
        if (not Character.isalpha() #We only want letters
            and Character != "-"    #Ok we can accept the -
            and Character != " "):  #Why not space if you want to put your full name.
            return False
    return True

def GivingPlayersStats():
    
    if Variables.Santé > Variables.MaxStats:
        Variables.Santé = Variables.MaxStats
    
    if Variables.Faim > Variables.MaxStats:
        Variables.Faim = Variables.MaxStats
    
    if Variables.Soif > Variables.MaxStats:
        Variables.Soif = Variables.MaxStats
    
    print(f"\nVous êtes à : {Variables.Santé}/{Variables.MaxStats} d'énergie")
    print(f"Vous êtes à : {Variables.Faim}/{Variables.MaxStats} de satieté")
    print(f"Vous êtes à : {Variables.Soif}/{Variables.MaxStats} d'hydratation\n")
    print(f"Tu es sur l'île depuis {Variables.GameProgression} heures\n")