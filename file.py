import os
import sys
from tkinter import *
import tkinter.filedialog

filename=tkinter.filedialog.askdirectory()
listfile = os.listdir(filename)
print(listfile)