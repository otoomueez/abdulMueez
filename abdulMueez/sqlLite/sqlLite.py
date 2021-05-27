import sqlite3
try:
    conn = sqlite3.connect("Students.db")
    getit = conn.cursor()
    # query = """CREATE TABLE Students(
    #             student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #             f_name TEXT,
    #             l_name TEXT,
    #             age INTEGER,
    #             program TEXT
    # )"""
    # getit.execute("DROP TABLE IF EXISTS Students")
    # getit.execute(query)
    # print("Database created")
    # query = """INSERT INTO Students (f_name, l_name, age, program)
                            # VALUES ( "Samuelina", "Oppong", 28, "Sonography")"""
    query = """UPDATE Students SET l_name = " " WHERE student_id = 7 """
    # query = """DELETE l_name FROM Students WHERE student_id = 7 """
    getit.execute(query)
    conn.commit()
    print("Successfully Updated")
except conn.Error as error:
    print("Error", error)
finally:
    if conn:
        conn.close()

# students_data = [
#     ( "Stephen", "Okoh", 21, "Physics"),
#     ( "Sheriff", "Yasin", 20, "Comp. Eng"),
#     ( "Melinda", "Ako", 21, "Mathematics"),
#     ( "Sandra", "Okoh", 21, "Physics")
# ]

# def insert_students (list):
#     try:
#         conn = sqlite3.connect("Students.db")
#         getit = conn.cursor()
#         query = """INSERT INTO Students (f_name, l_name, age, program )
#                                 VALUES (?,?,?,?)"""
#         print("Insert Successful ", list)
#         getit.executemany(query, list)
#         conn.commit()
#         print("Insert successful")
#     except conn.Error as error:
#         print("Error inserting into table ", error)
#     finally:
#         if conn:
#             conn.close()

# insert_students(students_data)