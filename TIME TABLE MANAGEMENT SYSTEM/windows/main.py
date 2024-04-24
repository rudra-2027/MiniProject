import tkinter as tk
from tkinter import *
import os
win  =Tk()
win.geometry('300x400')
win.resizable(False,False)
win.title('TIME TABLE ARRANGEMENT')
#LABEL
Label(win,text='SCHOOL MANAGEMNET',font='airtel 18 bold').place(x=10,y=0)

#FUNCTION
def new_time(): os.system('py windows\\New_Teacher.py')
def run_time(): os.system('py windows\\classes_t.py')
def a_time(): os.system('py windows\\Arrangement.py')
def u_time(): os.system('py windows\\update.py')
def Quit_time(): win.destroy()
#BUTTON
Button(win,text='New Teacher',font='bold',bd=4, command=new_time).place(x=95,y=39)
Button(win,text='Show Time Table',font='bold',bd=4 , command=run_time).place(x=80,y=82)
Button(win,text='Arrangement',font='bold',bd=4, command=a_time).place(x=95,y=125)
Button(win,text='Update Teacher Time Table',font='bold',bd=4, command=u_time).place(x=30,y=170)
Button(win,text='Quit',font='bold',bd=4,command=Quit_time).place(x=125,y=215)


win.mainloop()
