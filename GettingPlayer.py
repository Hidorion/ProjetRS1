def GettingPlayersName():    
    """
        On vient demander le prénom du joueur et on vérifie qu'il s'agit bien d'un prénom.
    """
    PlayerName = input("Mais tout d'abord, quel est ton nom ? ")
    PlayerName = PlayerName.upper()
    while not GettingPlayersInfo(PlayerName):
        PlayerName = input("Attends, reprends ton souffle, je t'écoute... : ").strip() #On veut retirer de possibles espaces accidentels ou non.
    
def GivingPlayerStatue():    
    """
        On fait part au joueur de sa condition.
    """
    print(f"Hoo {PlayerName} est un jolie nom.\n")
    print("Tu as eu de la chance, tu as pu être parfaitement reposé, nourri et hydraté avant de t'échouer ici\n")
    print("Tu as actuellement:\n")
    print(" - 100/100 de Santé.\n")
    print(" - 100/100 de Faim.\n")
    print(" - 100/100 de Soif.\n")

def GettingPlayersInfo (Name):
    """
        C'est ici que la vérification du prénom se fait.
    """
    if Name == "":
        return False
    for Character in Name:
        if (not Character.isalpha() #On ne veut que des lettres.
            and Character != "-"    #On accepte les tirets.
            and Character != " "):  #Ainsi que les espaces, Prénom et Nom par exemple.
            return False
    return True

