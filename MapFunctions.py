def entrypoints(d):
    pointchanger(5,0," ",d)
    pointchanger(10,10," ",d)
    pointchanger(0,10," ",d)
    pointchanger(5,20," ",d)
#a quel y / b quel x / c par quel caractère / d doit être la map à changer
def pointchanger (a,b,c,d):
    d[a][b] = " "


#a depuis quelle colone / b jusqu'à la case en colonne / c sur quelle colonne / d par quel caractère / e doit être la map à changer
def columnchanger (cca,ccb,ccc,ccd,cce): 
    for i in range(cca,ccb):
        cce[i][ccc] = ccd

#a depuis quelle ligne / b jusqu'à la case en ligne / c sur quelle ligne / d par quel caractère / e doit être la map à changer
def linechanger (lca,lcb,lcc,lcd,lce): 
    for j in range(lca,lcb):
        lce[lcc][j] = lcd
        