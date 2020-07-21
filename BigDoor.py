########## MODULES ##########
import tkinter as tk
from PIL import ImageTk, Image

########## DATA ##########
import Variables

########## Fonction pour afficher l'image ##########
def show_imge(path):
    """
        On affiche une belle photo d'une belle porte. C'est vraiment pour faire beau.
    """
    image_window = tk.Tk()
    img = ImageTk.PhotoImage(Image.open(path))
    panel = tk.Label(image_window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    image_window.mainloop()

########## Fonction de la Grande Porte ##########
def BigDoorPrep(Filename):   
    show_imge("door.jpg")
    LoadBigDoor(Filename)
    print()
    DrawBigDoor()
    
def LoadBigDoor(FileName): ########## On charge le texte associé à la porte
    """
        Loads the beautiful BigDoor
    """
    with open(FileName, "r", encoding="utf-8") as MyFile:
            Y = 0
            for Line in MyFile:
                Columns = []
                X = 0
                for Character in Line:
                    if Character == "\n": # ignore line ends
                        continue
                    Columns.append(Character) # add character to map
                    X += 1
                Variables.BigDoor.append(Columns) # add line to map
                Y += 1
def DrawBigDoor(): ########## On le dessine
    """
        Draw the beautiful BigDoor
    """
    for Y in range(len(Variables.BigDoor)):
        for X in range(len(Variables.BigDoor[Y])):        
            print(f'{Variables.BigDoor[Y][X]}', end="" )
        print()
    input()
    print(Variables.Credits)

#BigDoorPrep("TheBigDoor.txt")
