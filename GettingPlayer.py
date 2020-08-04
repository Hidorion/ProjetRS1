##### DATA #####
import Variables
import Clear

##### MODULES #####
import tkinter as tk
from PIL import ImageTk, Image

def DeathPrep(path):
    """
        Player is dead.
    """
    image_window = tk.Tk()
    img = ImageTk.PhotoImage(Image.open(path))
    panel = tk.Label(image_window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    image_window.mainloop()
def Death():   
    DeathPrep("Pictures\death.jpg")
    print()
    

def GettingPlayersName():    
    """
        We ask the player to give its - correct - name.
    """
    PlayerName = input("Mais tout d'abord, quel est ton nom ? ")
    PlayerName = PlayerName.upper()
    while not GettingPlayersInfo(PlayerName):
        PlayerName = input("Attends, reprends ton souffle, je t'écoute... : ").strip() #We want to delete extra blanks
    return PlayerName

def GettingRules ():
    """
        Giving the player some basic infos.
    """    
    WelcomeText = f"Bienvenue {Variables.PlayerName} sur cette île mystérieuse.\nTu es ici avec un seul et unique but. Réussir à franchir la Grande Porte ! (۩)\nPour cela tu devras réussir à obtenir 3 clés que tu obtiendras en réussisant les 3 défis de l'île.\n"
    SurvivalText = "Cette île n'est pas si paradisiaque.\nSes conditions climatiques risquent de te fatiguer et de t'affamer pendant ton périple\nSans compter sur cette chaleur, tu devras penser à boire pour t'hydrater.\nPour faire court, la mort te guette.\nSi ta Soif, ta Faim ou ta Santé tombe à 0, tu mourras et devras tout recommencer.\n"
    print(WelcomeText)
    print()
    print(SurvivalText)

def GettingInfo ():
    """
        Giving the player some useful tips.
    """ 
    CheckTheMap = "Tu as une carte dans ton inventaire. -> I\n"
    CheckYou="Tu es marqué par ce symbole -> ☻\n"
    CheckObjects="Sur la carte, il y a les 3 portes (en rouge) derrière lesquelles se trouvent les défis.\n"
    print(CheckTheMap)
    print(CheckYou)
    print(CheckObjects)

def GivingPlayerGlobalStatue():    
    """
        Giving the player the last crucial infos.
    """
    print(f"Hoo {Variables.PlayerName} est un jolie nom.\n")
    GettingRules ()
    GettingInfo ()
    print("Tu as eu de la chance, tu as pu être parfaitement reposé, nourri et hydraté avant de t'échouer ici\n")
    print("Tu as actuellement:\n")
    print(" - 100/100 d'énergie.\n")
    print(" - 100/100 de satiété.\n")
    print(" - 100/100 d'hydratation.\n")
    print("Pour te déplacer :\nZ pour aller vers le Nord, S pour le Sud, D pour l'Est et Q pour l'Ouest. Si tu as besoin d'autres informations écrits : Help\n")
    passer = input("Une fois que tu as bien tout compris, appuies sur Entrée ")
    Clear.ClearConsole()

def GettingPlayersInfo (Name):
    """
        We check that the name is correct.
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
    """
        Giving the player its current stats.
    """
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

def PlayersDeath():
    """
        We check if the player is going to die.
    """
    if (Variables.Santé or Variables.Faim or Variables.Soif) < 1:
        Variables.GameInProgress = False
        print("Partie terminée")
        Death()
