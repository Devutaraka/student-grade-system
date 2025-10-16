import json

FILENAME = "students.json"

def load_data():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(students):
    with open(FILENAME, "w") as f:
        json.dump(students, f, indent=4)

def add_student(students):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students.append({"name": name, "marks": marks})
    save_data(students)
    print(f"Student {name} added successfully!")

def view_students(students):
    if not students:
        print("No student records found.")
    else:
        for s in students:
            print(f"Name: {s['name']}, Marks: {s['marks']}")

def average_marks(students):
    if not students:
        print("No student data to calculate average.")
        return
    avg = sum(s['marks'] for s in students) / len(students)
    print(f"Average marks: {avg:.2f}")

def main():
    students = load_data()
    while True:
        print("\n=== Student Grade Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Calculate Average Marks")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            average_marks(students)
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
