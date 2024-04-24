from tkinter import *
win = Tk()
win.size()
win.title("Display Record")
def display():
    try:
        with open("C:\\Users\\rudra\\OneDrive\\Desktop\\Python\\Python\\Mini Project\\STUDENT MANAGEMENT SYSTEM\\New.txt", 'r') as f:
    # Your file handling code here

            record_text.delete('1.0',(END))  # Clear previous content
            record_text.insert(END, f.read())
    except Exception as e:
        record_text.insert(END, f"An error occurred: {e}")
    
record_text = Text(win, height=20, width=50)
record_text.pack(padx=10, pady=10)  

display_button = Button(win, text="Display Records", command=display)
display_button.pack(pady=5)
win.mainloop()