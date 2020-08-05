##### MODULES #####
import tkinter as tk
from PIL import ImageTk, Image

##### DATA #####
import Variables
import Inventory
import Clear

##### Function to show the picture #####
def show_imge(path):
    """
        We show a beautiful picture of a door.
    """
    image_window = tk.Tk()
    img = ImageTk.PhotoImage(Image.open(path))
    panel = tk.Label(image_window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    image_window.mainloop()

##### Function to print the Big Door #####
def BigDoorPrep(Filename):   
    show_imge("Pictures\door.jpg")
    LoadBigDoor(Filename)
    print()
    DrawBigDoor()
    
##### Loading the data #####
def LoadBigDoor(FileName): 
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

##### Printing #####
def DrawBigDoor(): 
    """
        Draw the beautiful BigDoor
    """
    for Y in range(len(Variables.BigDoor)):
        for X in range(len(Variables.BigDoor[Y])):        
            print(f'{Variables.BigDoor[Y][X]}', end="" )
        print()
    input()
    

def CheckKeys():
    """
        Just checking that the players got the keys to finish the game
    """
    if Inventory.Keys["2.1"][2] and Inventory.Keys["2.2"][2] and Inventory.Keys["2.3"][2]:
        Inventory.Keys["2.4"][2] = True
        BigDoorPrep("Text\TheBigDoor.txt")
        Clear.ClearConsole()
        print(Variables.Credits)
        input()
        Variables.GameInProgress = False
    else :
        BigDoorPrep("Text\TheBigDoorWrong.txt")