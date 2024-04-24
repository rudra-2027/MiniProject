'''
f=open("Record.txt",'a')
for i in range(1):
    name = input("Enter the name of student ")
    roll = input("Enter the roll number of the student ")
    section = input("Enter the section of the student ")
    percentage = input("Enter the percentage of the student ")
    f.write("\nName of the student:- "+name)
    f.write("\nRoll Number:- "+roll)
    f.write("\nSection:- "+section)
    f.write("\nPercentage:- "+percentage)
    f.write("\n----------------------------------")
    
f.close()'''
from tkinter import *
from tkinter import messagebox
def save_record():
    name = name_entry.get()
    roll = roll_entry.get()
    section = section_entry.get()
    percentage = percentage_entry.get()
    record = f"\nRoll Number:- {roll}\nName of the student:- {name}\nSection:- {section}\nPercentage:- {percentage}\n----------------------------------"
    try:
        with open("C:\\Users\\rudra\\OneDrive\\Desktop\\Python\\Python\\Mini Project\\STUDENT MANAGEMENT SYSTEM\\New.txt",'a') as f:
            f.write(record)
        messagebox.showinfo("Saved","Record Saved Successfully")
    except Exception as e:
        messagebox.showerror("Error",f'An error is {e}')       

win = Tk()
win.size()
win.title("Stundent Record Entry")
Label(win,text="Name: ").grid(row=0,column=0)
name_entry=Entry(win)
name_entry.grid(row=0,column=1)
Label(win,text="Section: ").grid(row=1,column=0)
section_entry=Entry(win)
section_entry.grid(row=1,column=1)
Label(win,text="Roll Number: ").grid(row=2,column=0)
roll_entry=Entry(win)
roll_entry.grid(row=2,column=1)
Label(win,text="Percentage: ").grid(row=3,column=0)
percentage_entry=Entry(win)
percentage_entry.grid(row=3,column=1)

Button(win,text="Save Record",bd=2,command=save_record).grid(row=5,column=1)
win.mainloop()