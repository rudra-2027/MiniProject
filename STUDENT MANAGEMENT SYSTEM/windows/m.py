from tkinter import *
from tkinter import messagebox
def modify_record():
    name = name_entry.get()
    new_section = section_entry.get()
    new_roll = roll_entry.get()
    new_percentage = percentage_entry.get()
    try:
        with open("C:\\Users\\rudra\\OneDrive\\Desktop\\Python\\Python\\Mini Project\\STUDENT MANAGEMENT SYSTEM\\New.txt",'r') as f:
            lines = f.readlines()
        found = False
        for i in range(len(lines)):
            if "Name of the student:- "+ name in lines[i]:
                lines[i + 1] = "Roll Number:- " + new_roll + "\n"
                lines[i + 2] = "Section:- " + new_section + "\n"
                lines[i + 3] = "Percentage:- " + new_percentage + "\n"
                found = True
        if found:
            with open("C:\\Users\\rudra\\OneDrive\\Desktop\\Python\\Python\\Mini Project\\STUDENT MANAGEMENT SYSTEM\\New.txt", "w") as f:
                f.writelines(lines)
            messagebox.showinfo("Success", "Record modified successfully!")
        else:
            messagebox.showerror("Error", "Student not found in the record.")
                
    except FileNotFoundError:
        messagebox.showerror("Error","File not Found Please Make Sure First add the file")
        
win = Tk()
win.size()
win.resizable(False,False)

win.title("Modify Record Entry")
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

Button(win,text='Submit',bd=2,command=modify_record).grid(row=4,column=1)
win.mainloop()