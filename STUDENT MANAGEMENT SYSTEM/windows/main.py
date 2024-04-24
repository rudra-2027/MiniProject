from tkinter import*
import subprocess
# from w import *
# import w as write
import os
win = Tk()  
win.geometry()
win.resizable(False,False)
def wrt():
    gui_script_path = os.path.abspath("C:\\Users\\rudra\\OneDrive\\Desktop\\Python\\Python\\Mini Project\\STUDENT MANAGEMENT SYSTEM\\windows\\w.py")
    # os.system("py windows\\main.py")
    subprocess.call(['python', gui_script_path])
    # subprocess.run(['python', 'windows\\w.py'])

def rd():
    gui_script_path = os.path.abspath("C:\\Users\\rudra\\OneDrive\\Desktop\\Python\\Python\\Mini Project\\STUDENT MANAGEMENT SYSTEM\\windows\\r.py")
    # os.system("py windows\\main.py")
    subprocess.call(['python', gui_script_path])

def mdfy():
    gui_script_path = os.path.abspath("C:\\Users\\rudra\\OneDrive\\Desktop\\Python\\Python\\Mini Project\\STUDENT MANAGEMENT SYSTEM\\windows\\m.py")
    # os.system("py windows\\main.py")
    subprocess.call(['python', gui_script_path])
    
def serch():
    gui_script_path = os.path.abspath("C:\\Users\\rudra\\OneDrive\\Desktop\\Python\\Python\\Mini Project\\STUDENT MANAGEMENT SYSTEM\\windows\\s.py")
    
    subprocess.call(['python', gui_script_path])

def delte():
    gui_script_path = os.path.abspath("C:\\Users\\rudra\\OneDrive\\Desktop\\Python\\Python\\Mini Project\\STUDENT MANAGEMENT SYSTEM\\windows\\d.py")
    
    subprocess.call(['python', gui_script_path])
    
Button(win,text='Add Record',font='Console 10 bold',bd='2',width='10',command=wrt).pack(pady=5)
Button(win,text='See Record',font='Console 10 bold',bd='2',command=rd).pack(pady=5)
Button(win,text='Modify Record',font='Console 10 bold',bd='2',command=mdfy).pack(pady=5)
Button(win,text='Search Record',font='Console 10 bold',bd='2',command=serch).pack(pady=5)
Button(win,text='Delete Record',font='Console 10 bold',bd='2',command=delte).pack(pady=5)

win.mainloop()