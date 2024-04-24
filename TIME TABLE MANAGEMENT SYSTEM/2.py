from tkinter import *
from tkinter import messagebox
import os, sys
sys.path.insert(0, 'windows/')

win=Tk()
win.title('Welcome')
win.geometry('400x500')
win.resizable(False,False)

Label(win,text="Time Table").pack()
