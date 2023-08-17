import sqlite3
from sqlite3 import Error
from .connectio import create_connection


def insert_User(data):
    conn = create_connection()
    sql = """ INSERT INTO Users (first_name, last_name, email, id) 
                VALUES(?, ?, ?, ?)
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Inserted")
        return True, cur.lastrowid
    except Error as e:
        print("Errro Inserting new Users:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()
def select_all_Users():
    conn = create_connection()
    sql = "SELECT * FROM Users"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all Users: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()
            
def delete_User(Email):
    conn = create_connection()
    sql = f"DELETE FROM Users WHERE email = {Email}"


    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("deleted")
        return True
    except Error as e:
        print("Error Deleting User:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def update_User(_id, data):
    conn = create_connection()

    sql = f""" UPDATE Users SET  
                            firstName = ?,
                            lastName = ?,
                            Email = ?,
                            id = ?,
                            
            WHERE id = {_id}

    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Updated")
        return True
    except Error as e:
        print("Error updating book: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()