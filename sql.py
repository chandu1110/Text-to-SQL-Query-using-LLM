import sqlite3
import random

## Connect to SQLite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert records and create the table
cursor = connection.cursor()

## Create the table if it doesn't already exist to prevent errors on re-running
table_info = """
Create table if not exists STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);
"""
cursor.execute(table_info)

# --- Data Generation for 100 Records ---

# Lists to generate random data from
first_names = ['Rohan', 'Priya', 'Amit', 'Sneha', 'Arjun', 'Anjali', 'Vikram', 'Pooja', 'Rahul', 'Kavita']
last_names = ['Sharma', 'Gupta', 'Verma', 'Singh', 'Patel', 'Kumar', 'Jain', 'Reddy', 'Naidu', 'Rao']
classes = ['Data Science', 'DEVOPS', 'Web Development', 'Machine Learning', 'Cloud Computing']
sections = ['A', 'B', 'C']

students_data = []
for _ in range(100):
    #
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    full_name = f"{first_name} {last_name}"
    
    # Select a random class, section, and marks
    class_name = random.choice(classes)
    section = random.choice(sections)
    marks = random.randint(35, 100) # Generate a random mark between 35 and 100
    
    # Add the generated record as a tuple to the list
    students_data.append((full_name, class_name, section, marks))

# --- Database Insertion ---

## Insert all 100 records into the STUDENT table using executemany for better performance
cursor.executemany('''Insert Into STUDENT (NAME, CLASS, SECTION, MARKS) values(?,?,?,?)''', students_data)

## Display all the records from the table to verify insertion
print("--- Displaying all 100 inserted records ---")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes to the database
connection.commit()

## Close the connection to the database
connection.close()

print("\nSuccessfully inserted 100 records and closed the database connection.")
