import mysql.connector
import tkinter  as tk 
from tkinter import *
import os
my_w = tk.Tk()
my_w.title('Class 4 Time Table')
my_w.geometry("849x170")
my_w.resizable(False,False)
my_connect = mysql.connector.connect(
  host="localhost",
  user="root", 
  passwd="lenovo@#021",
  database="school"
)

my_conn = my_connect.cursor()
####### end of connection ####
my_conn.execute("SELECT * FROM class4 limit 0,10")
e=Label(my_w,width=10,text='Day',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=0)
e=Label(my_w,width=10,text='Period1',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=1)
e=Label(my_w,width=10,text='Period2',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=2)
e=Label(my_w,width=10,text='Period3',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=3)
e=Label(my_w,width=10,text='Period4',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=4)
e=Label(my_w,width=10,text='',borderwidth=2, relief='ridge')
e.grid(row=0,column=5)
e=Label(my_w,width=10,text='Period5',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=6)
e=Label(my_w,width=10,text='Period6',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=7)
e=Label(my_w,width=10,text='Period7',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=8)
e=Label(my_w,width=10,text='Period8',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=9)

i=1
recess = "RECESS"
for class12 in my_conn: 
    for j in range(len(class12)+1):
        if j < 5:
            e = Label(my_w,width=10,text=class12[j], borderwidth=2,relief='ridge',anchor='w')
            e.grid(row=i, column=j)
        elif j == 5:
            e = Label(my_w,width=10,text=recess[i-1], borderwidth=2,relief='ridge')
            e.grid(row=i, column=j)
        else:
            e = Label(my_w,width=10,text=class12[j-1], borderwidth=2,relief='ridge',anchor='w')
            e.grid(row=i, column=j)
        #e.insert(END, class12[j])
    i=i+1
def c(): os.system('py windows\\C4.py')


Button(my_w,width=10,text='Update',bd=3 , command=c).grid(row=10,column=10)
my_w.mainloop()
