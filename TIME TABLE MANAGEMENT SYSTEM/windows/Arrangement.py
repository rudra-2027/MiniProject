from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import os 


win=Tk()
win.title('Arrangement')
win.geometry('700x600')
win.configure(bg='white')

Label(win,text='ARRANGEMENT MAKER',font='Arial 18 bold',bg='white').pack()

#window label
Label(win,text='Teacher Id',font='ARIAL 12 bold ',bg='white',fg='red').place(x=20,y=50)
Label(win,text='Class',font='ARIAL 12 bold ',bg='white',fg='red').place(x=20,y=80)
Label(win,text='Period',font='ARIAL 12 bold ',bg='white',fg='red').place(x=20,y=110)
Label(win,text='Day',font='ARIAL 12 bold ',bg='white',fg='red').place(x=20,y=140)





##Drop Box

#For Class
var=StringVar(win)
var.set('I')
OptionMenu(win,var,'I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII').place(x=120,y=80)

#For Period
v=StringVar(win)
v.set('P1')
OptionMenu(win,v,'P1','P2','P3','P4','P5','P6','P7','P8').place(x=120,y=110)

#For Day
a=StringVar(win)
a.set('')
OptionMenu(win,a,'Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday').place(x=120,y=140)

#Submit Button

def Submit():
    P1=b.get()     
    P4=a.get()
    
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="lenovo@#021",database="payroll1")
    mycursor=mysqldb.cursor()
    try:
       sql = "Select * from {0} where day ='{1}' "
       print(sql.format(P1,P4))
       mycursor.execute(sql.format(P1,P4))
       
       e=Label(win,width=10,text='Day',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
       e.place(x=20,y=300)
       e=Label(win,width=10,text='Period1',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
       e.place(x=90,y=300)
       e=Label(win,width=10,text='Period2',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
       e.place(x=160,y=300)
       e=Label(win,width=10,text='Period3',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
       e.place(x=230,y=300)
       e=Label(win,width=10,text='Period4',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
       e.place(x=300,y=300)
       e=Label(win,width=10,text='Period5',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
       e.place(x=370,y=300)
       e=Label(win,width=10,text='Period6',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
       e.place(x=440,y=300)
       e=Label(win,width=10,text='Period7',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
       e.place(x=510,y=300)
       e=Label(win,width=10,text='Period8',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
       e.place(x=580,y=300)

       i=1
       for classa in mycursor:
           for j in range(len(classa)+1):
               if j < 9:
                   e = Label(win,width=10,text=classa[j], borderwidth=2,relief='ridge',anchor='w')
                   e.place(x=20+(j*70),y=320)
               
           i=i+2
       
           

       mysqldb.commit()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()

#Entry Box
b=Entry(win,bd=2)
b.place(x=120,y=50)
Button(win,text='Submit',font='arial 12 ',bd=4,command=Submit).place(x=150,y=180)

def run(): os.system('py windows\\T_id.py')

Button(win,text='Teacher ID',font='arial 12 ',bd=4,command=run).pack()



win.mainloop()
