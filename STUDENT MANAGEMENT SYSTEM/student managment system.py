#WAP to enter the 5 student details such as name roll number section and percentage from the user and save it into the file name as record 
def add():
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
        
    f.close()
    re()


def re():
    f=open("Record.txt",'r')
    a=f.read()
    print()
    print(a)
    f.close()


def modify():
    
    f=open("Record.txt","r")
    s=f.readlines()
    
    found = False
    ch=input("Enter the name of student to modify ")
    
    for i in range(len(s)):
        if "Name of the student:- "+ ch in s[i]:
            
            roll = input("Enter the roll number of the student ")
            section = input("Enter the section of the student ")
            percentage = input("Enter the percentage of the student ")
            
            
            s[i+1] = "Roll Number:- " + roll + '\n'
            s[i+2] = "Section:- " + section + '\n'
            s[i+3] = "Percentage:- " + percentage + '\n' 
            
            found = True
            break
        
    if found:
        with open("Record.txt","w") as f:
            f.writelines(s)
            print("Record Is modified!")
    else:
        print("Student not found!")
        
        
    
def main():
    while True:
        print("\nMenu:")
        print("1. Add a record")
        print("2. Read all records")
        print("3. Modify a record")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add()
        elif choice == '2':
            re()
        elif choice == '3':
            modify()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()