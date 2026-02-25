# Task 1: Create a Dictionary of Student Marks

# Dictionary
students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

# Ask user input
name = input("Enter the student's name: ")

# Check and display result
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")