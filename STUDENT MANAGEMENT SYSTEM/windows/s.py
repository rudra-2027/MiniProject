from tkinter import * 
from tkinter import messagebox
win = Tk()
win.size()
win.title("Search Record")
def srch():
    roll_number=roll_entry.get()
    try:
        with open("C:\\Users\\rudra\\OneDrive\\Desktop\\Python\\Python\\Mini Project\\STUDENT MANAGEMENT SYSTEM\\New.txt", 'r') as f:
            found = False
            student_details = ""
            for line in f:
                if line.strip().startswith("Roll Number:-") and line.strip().split(" ")[-1] == roll_number:
                # if "Roll Number:- "+ roll_number in f:
                    found = True
                    # c=0
                    # f.seek(c)
                    student_details += "Student found with Roll Number: " + str(roll_number) + "\n"
                    student_details += "Student Details:\n"
                    print(f"Roll Number:-{roll_number}")
                    #student_details += line + "\n"
                    for _ in range(3):  # Get the next 3 lines (Name, Section, Percentage)
                        student_details += next(f).strip() + "\n"
                        print(student_details)
                        # c+=1
                        
                    break
            if found:
                messagebox.showinfo("Record Found", student_details)
            else:
                messagebox.showinfo("Record Not Found", "Student with Roll Number " + str(roll_number) + " not found in the record.")

    except FileNotFoundError:
        messagebox.showerror("Error", "Record file not found.")
            
Label(win,text="Roll number of the student").grid(row=0,column=0)
roll_entry = Entry(win)
roll_entry.grid(row=0,column=1)
Button(win,text="Submit",bd=2,command=srch).grid(row=1,column=1)
win.mainloop()