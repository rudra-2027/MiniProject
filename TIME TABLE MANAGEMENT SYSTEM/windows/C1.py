import mysql.connector
from tkinter import *
from tkinter import messagebox
win=Tk()
win.title('Update Class 1 Time Table')
win.geometry('400x400')

def Update():
    
    P1=e1.get()
    P2=e2.get()
    P3=e3.get()
    P4=e4.get()
    P5=e5.get()
    P6=e6.get()
    P7=e7.get()
    P8=e8.get()
    P9=D1.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="lenovo@#021",database="school")
    mycursor=mysqldb.cursor()
    try:
       sql = "Update class1 set Period1 = %s,Period2 = %s,Period3 =%s ,Period4 =%s, \
Period5=%s, Period6=%s, Period7=%s, Period8=%s  where DAY=%s"
       val=(P1,P2,P3,P4,P5,P6,P7,P8,P9)
       print(sql,val)
       mycursor.execute(sql,val)
       
       mysqldb.commit()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()


e1 = Entry(win)
e1.place(x=140, y=30)

e2 = Entry(win)
e2.place(x=140, y=50)

e3 = Entry(win)
e3.place(x=140, y=70)

e4 = Entry(win)
e4.place(x=140, y=90)

e5 = Entry(win)
e5.place(x=140, y=110)

e6 = Entry(win)
e6.place(x=140, y=130)

e7 = Entry(win)
e7.place(x=140, y=150)

e8 = Entry(win)
e8.place(x=140, y=170)


#For DAYS #######
D1 = Entry(win)
D1.place(x=140, y=10)


Label(win,text='Days',font='Arial 10 bold').place(x=50,y=10)
Label(win,text='Period 1',font='Arial 10 bold').place(x=50,y=30)
Label(win,text='Period 2',font='Arial 10 bold').place(x=50,y=50)
Label(win,text='Period 3',font='Arial 10 bold').place(x=50,y=70)
Label(win,text='Period 4',font='Arial 10 bold').place(x=50,y=90)
Label(win,text='Period 5',font='Arial 10 bold').place(x=50,y=110)
Label(win,text='Period 6',font='Arial 10 bold').place(x=50,y=130)
Label(win,text='Period 7',font='Arial 10 bold').place(x=50,y=150)
Label(win,text='Period 8',font='Arial 10 bold').place(x=50,y=170)




Button(win, text="Update",command = Update,height=3, width= 13).place(x=130, y=200)
win.mainloop()
