# # import python database module
import sqlite3
# try_except
try:
    # Create database with name internship_demo
    conn = sqlite3.connect('internship_demo.db')
    # cursor is a messenger btn the db and your application
    cursor = conn.cursor()
    # Query or assign command
    # query = """SELECT sqlite_version()"""
    # The triple quotes """ """ allows us to write on multiple lines without having to put it on every line
    # query = """CREATE TABLE IF NOT EXISTS Interns (
    query = """INSERT INTO Interns ( intern_id ,first_name, last_name,email,phone_number, school)
                            VALUES (001, "Chantelle","Osafo", "cosafo@gmail.com", "0123456789", "Ashesi" )"""
    # Execute messenger
    cursor.execute(query)
    conn.commit()
    print("Insert successful")
    # Assign data collected to variable "result"
    # result = cursor.fetchall()
    # Output result
    # print("Database successfully Opened. Version is ", result)
    # print("Table successfully created.")
except conn.Error as error:
    print("Error creating Table ", error)
finally:
    if conn:
        conn.close()

#  query = """CREATE TABLE IF NOT EXISTS Interns (
#                         intern_id INTEGER,
#                         first_name TEXT NOT NULL,
#                         last_name TEXT NOT NULL,
#                         email TEXT,
#                         phone_number TEXT,
#                         school TEXT

# Data Types : Real; Float/Decimal, Blob, Integer; Int, Text; String/VarChar, Null; Null/None/Does not exist

interns_list = [(2, "Enoch", "Sem", "enochsem@gmail.com", "0554444433", "UCC"),
                (3, "Vanessa", "Bedzra", "vanessabezra@gmail.com", "0552244433", "Ashesi"),
                (4, "George", "Arthur", "georgearthur@gmail.com", "0554884433", "Ashesi"),
                (5, "Hilda", "Ajara", "hilda@gmail.com", "0554994433", "UCC")]

def insert_interns (list):
    try:
        conn = sqlite3.connect('internship_demo.db')
        cursor = conn.cursor()
        query = """INSERT INTO Interns ( intern_id ,first_name, last_name,email,phone_number, school)
                                VALUES (?, ?, ?, ?, ?, ? )"""
        print("Insert successful", list)
        # Execute messenger
        cursor.executemany(query, list)
        conn.commit()
        print("Insert successful")
    except conn.Error as error:
        print("Error inserting into Table ", error)
    finally:
        if conn:
            conn.close()

insert_interns(interns_list)



















# import python database module
import sqlite3
# try_except
try:
    # Create database with name internship_demo
    conn = sqlite3.connect('internship_demo.db')
    # cursor is a messenger btn the db and your application
    cursor = conn.cursor()
    # Query or assign command
    # query = """SELECT sqlite_version()"""
    # The triple quotes """ """ allows us to write on multiple lines without having to put it on every line
    # query = """CREATE TABLE IF NOT EXISTS Interns (
    query = """INSERT INTO Interns ( intern_id ,first_name, last_name,email,phone_number, school)
                            VALUES (001, "Chantelle","Osafo", "cosafo@gmail.com", "0123456789", "Ashesi" )"""
    # Execute messenger
    cursor.execute(query)
    conn.commit()
    print("Insert successful")
    # Assign data collected to variable "result"
    # result = cursor.fetchall()
    # Output result
    # print("Database successfully Opened. Version is ", result)
    # print("Table successfully created.")
except conn.Error as error:
    print("Error creating Table ", error)
finally:
    if conn:
        conn.close()

#  query = """CREATE TABLE IF NOT EXISTS Interns (
#                         intern_id INTEGER,
#                         first_name TEXT NOT NULL,
#                         last_name TEXT NOT NULL,
#                         email TEXT,
#                         phone_number TEXT,
#                         school TEXT

# Data Types : Real; Float/Decimal, Blob, Integer; Int, Text; String/VarChar, Null; Null/None/Does not exist

interns_list = [(2, "Enoch", "Sem", "enochsem@gmail.com", "0554444433", "UCC"),
                (3, "Vanessa", "Bedzra", "vanessabezra@gmail.com", "0552244433", "Ashesi"),
                (4, "George", "Arthur", "georgearthur@gmail.com", "0554884433", "Ashesi"),
                (5, "Hilda", "Ajara", "hilda@gmail.com", "0554994433", "UCC")]

def insert_interns (list):
    try:
        conn = sqlite3.connect('internship_demo.db')
        # cursor = conn.cursor()
        # intern_id = list[0]
        # first_name = list[1]
        # last_name = list[2]
        # email = list[3]
        # phone_number = list[4]
        # school = list[5]
        query = """INSERT INTO Interns ( intern_id ,first_name, last_name,email,phone_number, school)
                                VALUES (?, ?, ?, ?, ?, ? )"""
        print("Insert successful", list)
        # Execute messenger
        cursor.executemany(query, list)
        conn.commit()
        print("Insert successful")
    except conn.Error as error:
        print("Error inserting into Table ", error)
    finally:
        if conn:
            conn.close()

insert_interns(interns_list)














import sqlite3

def update_phone_number(id, new_phonenumber):
    try:
            conn = sqlite3.connect("internship_demo.db")
            cursor = conn.cursor()
            # query = """SELECT first_name, last_name FROM interns WHERE intern_id >= 3 """
            # query = """SELECT first_name, last_name FROM interns WHERE school = "Ashesi" """
            # wildcard % used to return specific data/ data that has a specific type of data
            # query below return people from school that starts from A
            # query = """SELECT first_name, last_name FROM interns WHERE school LIKE "A%" """
            query = """UPDATE interns SET phone_number = "2342456536" WHERE intern_id = 4 """
            data_tuple = (new_phonenumber, id)
            cursor.execute(query)
            # result = cursor.fetchall()
            # print("Data returned successfully")
            print("Data updated successfully")
            # for intern in result:
            #     print("firstname:", intern[0])
            #     print("lastname:", intern[1])
            #     print("\n")
    except conn.Error as error:
        print("Error returninig daata from Table", error)
    finally:
        if conn:
            conn.close()

update_phone_number(3, 123456789)













    # SELECT
    # UPDATE
    # AND
    # WHERE
    # FROM
    # WHERE
    # fetchall, fetchmany, fetchone
    # * means all; SELECT * = select all