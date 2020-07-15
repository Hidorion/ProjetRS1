import random



Player = "Alex"
ListOfPlayers = ["Singe Agile", "Singe Marrant", "Singe Sage", "Singe Grand", "Singe Mince", "Chef Gorille", Player]
PosInList = 0

while ListOfPlayers[0] == Player and Player in ListOfPlayers:
    
    for j in range(50):
        
        Turn = j + 1
        
        if PosInList > len(ListOfPlayers)-1:
            PosInList = 0
        
        if Turn %3 == 0 and Turn %5 == 0 :
            
            if "Singe" in ListOfPlayers[PosInList]:
                CheckIfCorrect = random.randint(1,100)
                print(CheckIfCorrect)
                
                if CheckIfCorrect < 31:
                    print(f"{ListOfPlayers[PosInList]} dit : Fizz Buzz !!")
                
                else:
                    print(f"{ListOfPlayers[PosInList]} se trompe, la hooonte")
                    Delete = ListOfPlayers.pop(PosInList)
            else:
                CheckIfCorrect = random.randint(1,100)
                print(CheckIfCorrect)
                
                if CheckIfCorrect < 71:
                    print(f"{ListOfPlayers[PosInList]} dit : Fizz Buzz !!")
                
                else:
                    print(f"{ListOfPlayers[PosInList]} se trompe, la hooonte")
                    Delete = ListOfPlayers.pop(PosInList)
                
        elif Turn %3 == 0:
            
            if "Singe" in ListOfPlayers[PosInList]:
                CheckIfCorrect = random.randint(1,100)
                print(CheckIfCorrect)
                
                if CheckIfCorrect < 31:
                    print(f"{ListOfPlayers[PosInList]} dit : Fizz !!")
                
                else:
                    print(f"{ListOfPlayers[PosInList]} se trompe, la hooonte")
                    Delete = ListOfPlayers.pop(PosInList)
            else:
                CheckIfCorrect = random.randint(1,100)
                print(CheckIfCorrect)
                
                if CheckIfCorrect < 71:
                    print(f"{ListOfPlayers[PosInList]} dit : Fizz !!")
                
                else:
                    print(f"{ListOfPlayers[PosInList]} se trompe, la hooonte")
                    Delete = ListOfPlayers.pop(PosInList)
        
        elif Turn %5 == 0:
            
            if "Singe" in ListOfPlayers[PosInList]:
                CheckIfCorrect = random.randint(1,100)
                print(CheckIfCorrect)
                
                if CheckIfCorrect < 31:
                    print(f"{ListOfPlayers[PosInList]} dit : Buzz !!")
                
                else:
                    print(f"{ListOfPlayers[PosInList]} se trompe, la hooonte")
                    Delete = ListOfPlayers.pop(PosInList)
            
            else:
                CheckIfCorrect = random.randint(1,100)
                print(CheckIfCorrect)
                
                if CheckIfCorrect < 71:
                    print(f"{ListOfPlayers[PosInList]} dit : Buzz !!")
                
                else:
                    print(f"{ListOfPlayers[PosInList]} se trompe, la hooonte")
                    Delete = ListOfPlayers.pop(PosInList)
        else:
            
            if "Singe" in ListOfPlayers[PosInList]:
                CheckIfCorrect = random.randint(1,100)
                print(CheckIfCorrect)
                
                if CheckIfCorrect < 31:
                    print(f"{ListOfPlayers[PosInList]} dit : {Turn} !!")
                
                else:
                    print(f"{ListOfPlayers[PosInList]} se trompe, la hooonte")
                    Delete = ListOfPlayers.pop(PosInList)
            else:
                CheckIfCorrect = random.randint(1,100)
                print(CheckIfCorrect)
                
                if CheckIfCorrect < 71:
                    print(f"{ListOfPlayers[PosInList]} dit : {Turn} !!")
                
                else:
                    print(f"{ListOfPlayers[PosInList]} se trompe, la hooonte")
                    Delete = ListOfPlayers.pop(PosInList)
        
        PosInList = PosInList + 1
        
        print(ListOfPlayers)
    
    print("agrandir range")  

print("C'est gagné")
print("Blablabla")