from tkinter import *
import mysql.connector
win=Tk()

my_connect = mysql.connector.connect(
  host="localhost",
  user="root", 
  passwd="lenovo@#021",
  database="payroll1"
)
my_conn = my_connect.cursor()
####### end of connection ####
my_conn.execute("SELECT * FROM registation ")
e=Label(win,width=10,text='Teacher Id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=1,column=0)
e=Label(win,width=15,text='Teacher name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=1,column=1)
e=Label(win,width=10,text='Subject',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=1,column=2)


i=1
for registation in my_conn:
    for j in range(len(registation)+1):
        if j<3:
            e = Label(win,width=20,text=registation[j], borderwidth=2,relief='ridge',anchor='w')
            e.grid(row=i+1, column=j)
            
    i=i+1

win.mainloop()
