import csv

students = []

def add_student():
    try:
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        marks1 = float(input("Enter marks for Subject 1: "))
        marks2 = float(input("Enter marks for Subject 2: "))
        marks3 = float(input("Enter marks for Subject 3: "))
        student = {
            "name": name,
            "roll": roll,
            "marks": [marks1, marks2, marks3]
        }
        students.append(student)
        print("Student added successfully.\n")
    except ValueError:
        print("Please enter valid numbers for marks.\n")

def display_students():
    if not students:
        print("No student records found.\n")
        return
    print("Student Records:")
    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}")
    print()

def calculate_averages():
    if not students:
        print("No student records to calculate average.\n")
        return
    print("Average Marks:")
    for s in students:
        avg = sum(s["marks"]) / 3
        print(f"{s['name']} (Roll {s['roll']}): Average = {avg:.2f}")
    print()

def save_to_csv():
    try:
        with open("students.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Roll", "Subject1", "Subject2", "Subject3"])
            for s in students:
                writer.writerow([s["name"], s["roll"], *s["marks"]])
        print("Records saved to students.csv\n")
    except Exception as e:
        print(f"Error saving file: {e}\n")

def main():
    while True:
        print("Student Data Tracker")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Calculate Average Marks")
        print("4. Save to CSV")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            calculate_averages()
        elif choice == "4":
            save_to_csv()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.\n")

if __name__ == "__main__":
    main()
