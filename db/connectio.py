import sqlite3
from sqlite3 import Error

def create_connection():

    try:
        
        conn = sqlite3.connect('db/customer1.db')
        
        return conn
    except Error as e:
        print("Error connecting to db: " + str(e))


# import sqlite3
# conn=sqlite3.connect('customer1.db')
# c=conn.cursor()
# c.execute("""CREATE TABLE Users(
#     first_name VARCHAR(50),
#     last_name VARCHAR(50),
#     email VARCHAR(50),
#     id VARCHAR(50)
# )"""
#           )
# # c.execute(" INSERT INTO customers VALUES ('sena','mehta','sm@123','1')")
# # print("command executed successfully")
# #null INTEGER real text blob(img)

# # conn.commit()
# # conn.close()