import random

#a quel y / b quel x / c par quel caractère / d doit être la map à changer
def pointchanger (y,x,sample,map):
    map[y][x] = sample

def CantMoveSpots(d): #Squelette immuable de la map
    for i in range(3):
        linechanger(0,30,i,"M",d)
        linechanger(35,100,i,"M",d)
        linechanger(30,35,i,"S",d)
    for j in range(3,25):
        linechanger(0,7,j,"M",d)
        linechanger(93,100,j,"M",d)
        linechanger(92,93,j,"T",d)
    for k in range (25,30):
        linechanger(0,100,k,"~",d)
    for sand in range (20,25):
        linechanger(8,92,sand,"░",d)
        linechanger(35,50,sand,"S",d)


MyListY = [] 
for y in range(30): 
    MySubList = [] 
    for x in range(100): 
        MySubList.append(" ") 
    MyListY.append(MySubList)


#a Depuis ce point /b jusqu'à x en colonne /c la colonne /d par quel caractère /e la map    
def columnchanger (depart,arrive,Colonne,sample,map): 
    """
        Permet de changer rapidement des éléments sur une colonne
    """
    for i in range(depart,arrive):
        map[i][Colonne] = sample

#a Depuis ce point / b jusqu'à x en ligne /c La ligne /d par quel caractère /e la map
def linechanger (depart,arrive,Ligne,sample,map): 
    """
        Permet de changer rapidement des éléments sur une ligne
    """
    for j in range(depart,arrive):
        map[Ligne][j] = sample
        

CantMoveSpots(MyListY) #Entrées des points visitables
pointchanger(24,85,"☻",MyListY)
#pointchanger(random.randint(20,26),74,"۩",MyListY)
pointchanger(2,random.randint(50,90),"○",MyListY) #Position César Code
pointchanger(random.randint(10,16),92,"◌",MyListY) #Position Sphinx Nombre Mystérieux
#pointchanger(random.randint(20,25),random.randint(8,14),"●",MyListY) #Position Fizz Buzz

def printmap():
    for Base_x in MyListY:
        print("".join(Base_x))


""" 
Eau potable = S
Eau de mer = ~
Montagne = M
Sable = ░
Plaine = " "
Porte 1 César = ○
Porte 2 ????  = ◌
Porte 3 FB-ZZ = ●
Objet consommable = ©
Objet récupérable = ʘ
Grande Porte = ۩
Arbre = T
Pont = "="
"""

