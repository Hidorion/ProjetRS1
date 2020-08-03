##### MODULES #####
import random

##### DATA #####



def DiceGame(Player):
    """
        Mini Game to entertain the player
    """
    PlayerOne = Player
    PlayerTwo = f"{Player}'s imaginary friend"    
    TryOne = random.randint(1,6) + random.randint(1,6)
    TryTwo = random.randint(1,6) + random.randint(1,6)
    print(f"{PlayerOne} lance les 2 dés. Il obtient {TryOne}")
    print(f"{PlayerTwo} lance les 2 dés. Il obtient {TryTwo}")
    if TryOne < TryTwo:
        print(f"{PlayerTwo} gagne la partie")
    elif TryOne > TryTwo:
        print(f"{PlayerOne} gagne la partie")
    else :
        print("Match nul")
    print("Bon... On s'y remet, j'ai des clés à récupérer")