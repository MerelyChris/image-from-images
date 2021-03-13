from tkinter import Tk
from tkinter.filedialog import askdirectory, askopenfile, askopenfilename
import ctypes

#Stops tkinter's GUI
Tk().withdraw()

#Handles DPI scaling
ctypes.windll.shcore.SetProcessDpiAwareness(1)

#Opens and stores the multiple image folder and the final image file
img_fold_dir_loc = askdirectory()
final_img_file = askopenfile()

