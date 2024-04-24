from tkinter import *
import os

win=Tk()
win.title('Clases')

Label(win,text='CLASSES TIMETABLE',font='Arial 10 bold').pack()


def class12(): os.system('py windows\\Class12.py ')
def class11(): os.system('py windows\\Class11.py ')
def class10(): os.system('py windows\\Class10.py ')
def class9(): os.system('py windows\\Class9.py ')
def class8(): os.system('py windows\\Class8.py ')
def class7(): os.system('py windows\\Class7.py ')
def class6(): os.system('py windows\\Class6.py ')
def class5(): os.system('py windows\\Class5.py ')
def class4(): os.system('py windows\\Class4.py ')
def class3(): os.system('py windows\\Class3.py ')
def class2(): os.system('py windows\\Class2.py ')
def class1(): os.system('py windows\\Class1.py ')



Button(win,text='Class I',bd=4,command=class1).pack(pady=5)

Button(win,text='Class II',bd=4,command=class2).pack(pady=5)

Button(win,text='Class III',bd=4,command=class3).pack(pady=5)

Button(win,text='Class IV',bd=4,command=class4).pack(pady=5)

Button(win,text='Class V',bd=4,command=class5).pack(pady=5)

Button(win,text='Class VI',bd=4,command=class6).pack(pady=5)

Button(win,text='Class VII',bd=4,command=class7).pack(pady=5)

Button(win,text='Class VIII',bd=4,command=class8).pack(pady=5)

Button(win,text='Class IX',bd=4,command=class9).pack(pady=5)

Button(win,text='Class X',bd=4,command=class10).pack(pady=5)

Button(win,text='Class XI',bd=4,command=class11).pack(pady=5)

Button(win,text='Class XII',bd=4,command=class12).pack(pady=5)
win.mainloop()
