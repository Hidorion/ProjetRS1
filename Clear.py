import os
import sys
#######################################################################################
def ClearConsole():
    """
        This function clears the console depending on OS except Mac, because reason.
    """
    if "win" in sys.platform.lower():
        os.system("cls")
    elif "linux" in sys.platform.lower():
        os.system("clear")
        # mac users, you can't pay for that sorry.
#######################################################################################