import sqlite3


connection = sqlite3.connect("database.db")
cursor = connection.cursor()


def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS Students (full_name TEXT, first_exam INT, second_exam INT, third_exam INT)")


def insert(full_name, first_exam, second_exam, third_exam):
    cursor.execute("INSERT INTO Students (full_name, first_exam, second_exam, third_exam) VALUES (?, ?, ?, ?)", 
                   (full_name, first_exam, second_exam, third_exam))
    connection.commit()


def select():
    cursor.execute("SELECT * FROM Students")
    for row in cursor.fetchall():
        print(row)


def delete(full_name):
    cursor.execute("DELETE FROM Students WHERE full_name=?", (full_name,))
    connection.commit()


create_table()


name = input("Enter the student's full name: ")
first_exam = int(input("Enter the score for the first exam: "))
second_exam = int(input("Enter the score for the second exam: "))
third_exam = int(input("Enter the score for the third exam: "))
insert(name, first_exam, second_exam, third_exam)

print("\nData in the database after insertion:")
select()

name_to_delete = input("\nEnter the name of the student you want to delete: ")
delete(name_to_delete)

print("\nData in the database after deletion:")
select()


cursor.close()
connection.close()
