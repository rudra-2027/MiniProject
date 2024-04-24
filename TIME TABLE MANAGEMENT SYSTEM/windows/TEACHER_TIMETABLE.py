import mysql.connector
from tkinter import *
from tkinter import messagebox
win=Tk()
win.title('ADD T_TIMETABLE')
win.geometry('400x400')

def Add():
    T_id=e9.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="lenovo@#021",database="payroll1")
    mycursor=mysqldb.cursor()
    try:
       sql = "CREATE TABLE {}(Day Varchar(30),P1 varchar(30),P2 varchar(30),P3 varchar(30),P4 varchar(30),\
       P5 varchar(30),P6 varchar(30),P7 varchar(30),P8 varchar(30))"
       Table = (T_id)
       mycursor.execute(sql.format(T_id))
       mysqldb.commit()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()

def Insert():
    e=e9.get()
    P1=e1.get()
    P2=e2.get()
    P3=e3.get()
    P4=e4.get()
    P5=e5.get()
    P6=e6.get()
    P7=e7.get()
    P8=e8.get()
    P10=D1.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="lenovo@#021",database="payroll1")
    mycursor=mysqldb.cursor()
    try:
       sql = "INSERT INTO {0}(Day,P1,P2,P3,P4,P5,P6,P7,P8) VALUES ('{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}',\
       '{9}')"
       Table = (P10,P1,P2,P3,P4,P5,P6,P7,P8)
       print(sql.format(e,P10,P1,P2,P3,P4,P5,P6,P7,P8))
       mycursor.execute(sql.format(e,P10,P1,P2,P3,P4,P5,P6,P7,P8))
       
       mysqldb.commit()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()


e1 = Entry(win)
e1.place(x=140, y=70)

e2 = Entry(win)
e2.place(x=140, y=90)

e3 = Entry(win)
e3.place(x=140, y=110)

e4 = Entry(win)
e4.place(x=140, y=130)

e5 = Entry(win)
e5.place(x=140, y=150)

e6 = Entry(win)
e6.place(x=140, y=170)

e7 = Entry(win)
e7.place(x=140, y=190)

e8 = Entry(win)
e8.place(x=140, y=210)

#For Table Name
e9 = Entry(win)
e9.place(x=140, y=10)

#For DAYS #######
D1 = Entry(win)
D1.place(x=140, y=50)


Label(win,text='Days',font='Arial 10 bold').place(x=50,y=50)
Label(win,text='Period 1',font='Arial 10 bold').place(x=50,y=70)
Label(win,text='Period 2',font='Arial 10 bold').place(x=50,y=90)
Label(win,text='Period 3',font='Arial 10 bold').place(x=50,y=110)
Label(win,text='Period 4',font='Arial 10 bold').place(x=50,y=130)
Label(win,text='Period 5',font='Arial 10 bold').place(x=50,y=150)
Label(win,text='Period 6',font='Arial 10 bold').place(x=50,y=170)
Label(win,text='Period 7',font='Arial 10 bold').place(x=50,y=190)
Label(win,text='Period 8',font='Arial 10 bold').place(x=50,y=210)

Label(win,text='ENTER T_ID ',font='Arial 10 bold').place(x=50,y=10)
Label(win,text='(Example:- T_101) ',font='Arial 10 bold',fg='red').place(x=250,y=10)


Button(win, text="Add",command = Add,height=1, width= 7).place(x=400, y=10)
Button(win, text="Insert",command = Insert,height=3, width= 13).place(x=130, y=250)
win.mainloop()
