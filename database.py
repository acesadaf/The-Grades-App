import sqlite3 
from sqlite3 import Error
def create_connection():
    """ create a database connection to a SQLite database """
    # conn = sqlite3.connect(db_file)
    # return conn
    db_file = r"D:\Python_OOP\project\pythonsqlite.db"
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
    make_courses = "create table if not exists Courses(username char(100), Course_ID char(100), Course_Name char (100), Component char(100), Weight number, primary key (Course_ID, Component), foreign key (username) references Users (username))"
    make_entries = "create table if not exists Entries(username char(100), Course_ID char(100), Component char(100), value number, outof number, primary key(username, Course_ID, Component), foreign key (Component) references Courses (Component))" 
    conn.execute(make_users)
    conn.execute(make_courses)
    conn.execute(make_entries)
    conn.commit()




def insert_user(username, name, password, conn):
    user_inserter = "insert into Users values('{}', '{}', '{}')".format(username, name, password)
    conn.execute(user_inserter)



    #checker2 = "SELECT name FROM sqlite_master WHERE type='table' AND name='courses"
    
 
# conn = create_connection(r"D:\Python_OOP\project\pythonsqlite.db")
# create_if_not_exists(conn)
# conn.execute("select * from Users")
# conn.execute("insert into Users values('acesadaf', 'sadaf md halim', 'mypass')")
# cursor = conn.execute("select * from Users")
# for row in cursor:
#     print (row[0])
# conn.commit()
# close_connection(conn)





