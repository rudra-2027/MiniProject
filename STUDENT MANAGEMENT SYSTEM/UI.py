from tkinter import *
import subprocess
# import w
import os
import sys
win = Tk()  
win.geometry("400x100")
win.resizable(False,False)

def change():
    # sys.path.append()
    gui_script_path = os.path.abspath("C:\\Users\\rudra\\OneDrive\\Desktop\\Python\\Python\\Mini Project\\STUDENT MANAGEMENT SYSTEM\\windows\\main.py")
    # os.system("py windows\\main.py")
    subprocess.call(['python', gui_script_path])
    win.destroy()
    
Label(win,text="Welcome, \n Student Mangement System",font = 'Console').pack()

Button(win,text='Enter',font = 'Console',bd=4,height=1,width='4',command=change).pack()
win.mainloop()