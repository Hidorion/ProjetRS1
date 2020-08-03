##### MODULES #####
import random

##### DATA #####



def DiceGame(Player):
    """
        Mini Game to entertain the player
    """
    PlayerOne = Player
    PlayerTwo = "Wilson"    
    DiceOne = random.randint(1,6)
    DiceTwo = random.randint(1,6)
    DiceThree = random.randint(1,6)
    DiceFour = random.randint(1,6)
    TryOne = DiceOne + DiceTwo
    TryTwo = DiceThree + DiceFour
    print(f"{PlayerOne} lance les 2 dés.\nIl obtient :\n{DiceAssign(DiceOne,DiceOne)}{DiceAssign(DiceTwo,DiceTwo)}\nSoit un score total de {TryOne}\n")
    print(f"{PlayerTwo} lance les 2 dés.\nIl obtient :\n{DiceAssign(DiceThree,DiceThree)}{DiceAssign(DiceFour,DiceFour)}\nSoit un score total de {TryTwo}\n")
    if TryOne < TryTwo:
        print(f"{PlayerTwo} gagne la partie")
    elif TryOne > TryTwo:
        print(f"{PlayerOne} gagne la partie")
    else :
        print("Match nul")
    print("Bon... On s'y remet, j'ai des clés à récupérer")
    input("Appuies sur Entrée pour continuer")

def DiceAssign(Dice,Value):
    """
        This function allows the player to see the dice he has just thrown.
    """
    One = "┌───────┐\n│       │\n│   ●   │\n│       │\n└───────┘\n"
    Two = "┌───────┐\n│ ●     │\n│       │\n│     ● │\n└───────┘\n"
    Three = "┌───────┐\n│ ●     │\n│   ●   │\n│     ● │\n└───────┘\n"
    Four = "┌───────┐\n│ ●   ● │\n│       │\n│ ●   ● │\n└───────┘\n"
    Five = "┌───────┐\n│ ●   ● │\n│   ●   │\n│ ●   ● │\n└───────┘\n"
    Six = "\u001b[31m┌───────┐\n│ ●   ● │\n│ ●   ● │\n│ ●   ● │\n└───────┘\u001b[0m\n"
    Dice = Value
    if Value == 1:
        DiceValue = One
    elif Value == 2:
        DiceValue = Two
    elif Value == 3:
        DiceValue = Three
    elif Value == 4:
        DiceValue = Four
    elif Value == 5:
        DiceValue = Five
    elif Value == 6:
        DiceValue = Six
    return DiceValue

