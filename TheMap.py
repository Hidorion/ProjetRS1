#a quel y / b quel x / c par quel caractère / d doit être la map à changer
def pointchanger (y,x,sample,map):
    map[y][x] = sample

def CantMoveSpots(d): #Squelette immuable de la map
    for i in range(5):
        linechanger(0,30,i,"M",d)
        linechanger(35,82,i,"M",d)
        linechanger(30,35,i,"S",d)
        linechanger(7,32,i+24,"░",d)
    for j in range(5, 16):
        linechanger(0,7,j,"M",d)
        linechanger(30,35,j,"S",d)
        linechanger(75,82,j,"M",d)
        linechanger(32,37,(j +13),"S",d)
        linechanger(29,30,j,"░",d)
        linechanger(35,36,j,"░",d)
    for k in range(15, 32):    
        linechanger(0,7,k,"M",d)
        linechanger(75,82,k,"M",d)
        linechanger(37,75,k,"░",d)
    for l in range(29,32):
        linechanger(7,82,l,"~",d)
    pointchanger(15,36,"░",MyListY)


MyListY = [] 
for y in range(32): 
    MySubList = [] 
    for x in range(82): 
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
        

CantMoveSpots(MyListY)
pointchanger(28,65,"☻",MyListY)
def printmap():
    for Base_x in MyListY:
        print("".join(Base_x))


""" 
Eau potable = S
Eau de mer = ~
Montagne = M
Portes = ●
Objets = ○
Sable = ░
Plaine = " "
"""