import sqlite3

def update_phone_number(id, new_phonenumber):
    try:
            conn = sqlite3.connect("internship_demo.db")
            cursor = conn.cursor()
            query = """DELETE FROM interns WHERE intern_id = 4 """
            cursor.execute(query)
            conn.commit()
            print("Data deleted successfully")
    except conn.Error as error:
        print("Error deleting data from Table", error)
    finally:
        if conn:
            conn.close()













    # SELECT
    # UPDATE
    # AND
    # WHERE
    # FROM
    # WHERE