from tkinter import *
from tkinter import messagebox
import os, sys
sys.path.insert(0, 'windows/')

win=Tk()
win.title('Welcome')
win.geometry('400x500')
win.resizable(False,False)


#HEADING
Label(win,text='TIME TABLE MANAGEMENT SYSTEM',font='Consolas 20 bold',wrap=400).pack(pady=20)


#Welcome!
Label(win,text='Welcome! \n Please Enter Your \nLogin Username And Password',font='Consolas 12').pack(pady=20)


#LABEL USER AND PASSWORD
id_user=Label(win,text='Username!',font='Consolas 14 italic bold')
id_user.pack()
id_pass=Label(win,text='Password!',font='Consolas 14 italic bold')
id_pass.pack(pady=20)

#NEW WINDOW
def challenge():
    u_ent=n_entry.get()
    pass_ent=p_entry.get()
    if u_ent== 'User' and pass_ent == 'Kvpbt':
        win.destroy()
        os.system('py windows\\main.py')
    else:
        messagebox.showerror('WRONG ENTRY', 'USERNAME AND PASSWORD')


#ENTRY USER AND PASSWORD

n_entry=StringVar()
p_entry=StringVar()
u_ent=Entry(win,text='',font='Consolas 10',textvariable=n_entry)
u_ent.place(x=120,y=240)
pass_ent=Entry(win,show='●',font='Consolas 10',textvariable=p_entry)
pass_ent.place(x=120,y=290)

#PASSWORD SHOW BUTTON
def show_passw():
    if pass_ent['show']=='●':
        pass_ent['show'] = ''
        B_show['text'] ='●'
        B_show.update()
    elif pass_ent['show']=='':
        pass_ent['show'] ='○'
        B_show['text'] ='○'
        B_show.update()
    pass_ent.update()

#BUTTON'
B_show=Button(win,text='○',font='Consolas 12',bd=4,height=1 ,width=2,command=show_passw)
B_show.place(x=270,y=283)





#BUTTON LOGIN
Button(win,text='Login',font='Consolas 12',command=challenge).pack(pady=10)


win.mainloop()
