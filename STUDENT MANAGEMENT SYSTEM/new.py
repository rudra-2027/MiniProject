import json

def add_record():
    records = []
    with open("Record.json", "a+") as file:
        # Read existing records if any
        file.seek(0)
        try:
            records = json.load(file)
        except json.decoder.JSONDecodeError:
            pass  # If file is empty or not properly formatted JSON
        
        # Get details from user
        name = input("Enter the name of the student: ")
        roll = input("Enter the roll number of the student: ")
        section = input("Enter the section of the student: ")
        percentage = input("Enter the percentage of the student: ")
        
        # Add record to list of records
        records.append({
            "Name": name,
            "Roll": roll,
            "Section": section,
            "Percentage": percentage
        })
        
        # Write the updated records list back to the file
        file.seek(0)
        json.dump(records, file, indent=4)

def main():
    while True:
        print("\nMenu:")
        print("1. Add a record")
        print("2. Read all records")
        print("3. Modify a record")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_record()
        # Add options for reading, modifying, and exiting here
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
