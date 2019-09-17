import sqlite3 
from sqlite3 import Error
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    # conn = sqlite3.connect(db_file)
    # return conn

    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn
    # finally:
    #     if conn:
    #         conn.close()
def close_connection(conn):
    if conn!= None:
        conn.close()

def create_if_not_exists(conn): 
    make_users = "create table if not exists Users(username char(100) primary key, name char(100), password char(100))"
    #make_courses = 
    conn.execute(make_users)


def insert_user(username, name, password, conn):
    user_inserter = "insert into Users values('{}', '{}', '{}')".format(username, name, password)
    conn.execute(user_inserter)



    #checker2 = "SELECT name FROM sqlite_master WHERE type='table' AND name='courses"
    
 
conn = create_connection(r"D:\Python_OOP\project\pythonsqlite.db")
create_if_not_exists(conn)
conn.execute("select * from Users")
conn.execute("insert into Users values('acesadaf', 'sadaf md halim', 'mypass')")
cursor = conn.execute("select * from Users")
for row in cursor:
    print (row[0])
conn.commit()
close_connection(conn)





