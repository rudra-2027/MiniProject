import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
import os 
 
def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['Teacher id'])
    e2.insert(0,select['Teacher name'])
    e3.insert(0,select['Teacher subject'])
    e4.insert(0,select['Teacher mobile'])
    e5.insert(0,select['Teacher salary'])
 
 
def Add():
    T_id = e1.get()
    T_name = e2.get()
    T_subject =  e3.get()
    T_mobile = e4.get()
    T_salary = e5.get()
 
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="lenovo@#021",database="payroll1")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "INSERT INTO  registation (id,empname,subject,mobile,salary) VALUES (%s, %s, %s, %s, %s)"
       val = (T_id,T_name,T_subject,T_mobile,T_salary)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Teacher inserted successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e1.focus_set()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
 
def update():
    T_id = e1.get()
    T_name = e2.get()
    T_subject = e3.get()
    T_mobile = e4.get()
    T_salary = e5.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="lenovo@#021",database="payroll1")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "Update  registation set empname= %s, subject= %s,mobile= %s,salary= %s where id= %s"
       val = (T_name,T_subject,T_mobile,T_salary,T_id)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Updated successfully...")
 
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e1.focus_set()
 
    except Exception as e:
 
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
def delete():
    T_id = e1.get()
 
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="lenovo@#021",database="payroll1")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "delete from registation where id = %s"
       val = (T_id,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Delete successfully...")
 
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e1.focus_set()

 
    except Exception as e:
 
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="lenovo@#021", database="payroll1")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT id,empname,subject,mobile,salary FROM registation")
        records = mycursor.fetchall()
        print(records)
 
        for i, (id,name,subject, mobile,salary) in enumerate(records, start=1):
            listBox.insert("", "end", values=(id, name,subject, mobile, salary))
            mysqldb.close()
 
root = Tk()
root.geometry("1050x500")
root.title('T_Registation')
global e1
global e2
global e3
global e4
global e5
 
tk.Label(root, text="Teacher Registation", fg="red", font=(None, 30)).place(x=300, y=5)
 
tk.Label(root, text="Teacher ID").place(x=10, y=10)
Label(root, text="Teacher Name").place(x=10, y=40)
Label(root, text="Subject").place(x=10, y=70)
Label(root, text="Mobile").place(x=10, y=100)
Label(root, text="Salary").place(x=10, y=130)
 
e1 = Entry(root)
e1.place(x=140, y=10)
 
e2 = Entry(root)
e2.place(x=140, y=40)
 
e3 = Entry(root)
e3.place(x=140, y=70)
 
e4 = Entry(root)
e4.place(x=140, y=100)

e5 = Entry(root)
e5.place(x=140, y=130)


def run(): os.system('py windows\\TEACHER_TIMETABLE.py')


Button(root, text="Add",command = Add,height=3, width= 13).place(x=30, y=160)
Button(root, text="update",command = update,height=3, width= 13).place(x=140, y=160)
Button(root, text="Delete",command = delete,height=3, width= 13).place(x=250, y=160)
Button(root, text="Add Teacher TimeTable",command = run,height=3, width= 18).place(x=380, y=160)
 
cols = ('Teacher id', 'Teacher name','Teacher subject', 'Teacher mobile','Teacher salary')
listBox = ttk.Treeview(root, columns=cols, show='headings' )
 
for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=1)
    listBox.place(x=10, y=220)
 
show()
listBox.bind('<Double-Button-1>',GetValue)
 
root.mainloop()
