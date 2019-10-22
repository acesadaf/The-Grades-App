import database as db
class Main_Menu:
    def __init__(self, username):
        self.username = username
        print("Howdy!")
        done = False 
        while (done!=True):
            print("Press 1 to add a new course.")
            print("Press 2 to add an entry for an existing course.")
            print("Press 3 to quit!")
            key="placeholder"
            while (1):
                key = input()
                if(key =='1' or key =='2' or key == '3'):
                    break 
                else:
                    print('Enter either 1 or 2')
            if key == '1':
                AddCourse(username)
            elif key == '2':
                AddEntry(username)
            else:
                quit()


def AddCourse(username):
    print("Hi! Before we can add this course, we need some information.")
    print("Please provide your Course_ID")
    Course_ID = input()
    Course_Name = "placeholder"
    conn = db.create_connection()
    CheckString = "Select * from Courses where username = '{}' and Course_ID = '{}'".format(username, Course_ID)
    MyCursor = conn.cursor()
    MyCursor.execute(CheckString)
    rows = MyCursor.fetchall()
    db.close_connection(conn)
    if(len(rows)==0):
        print("And your course name?")
        Course_Name = input()
        active = True 
        component = []
        weight = []
        while(active):
            print("To Add a new course component, press 1, and if done, press 2")
            key = input()
            if key == '2':
                active = False
            if key == '1':
                print("component name? (such as exam, quiz) ")
                name = input()
                print("weight?")
                w = "placeholder"
                flag = False
                while(flag!=True):
                    print("Please input a numeric value between 1 to 100.")
                    w = input()
                    if(w.isnumeric()):
                        if (int(w) >= 0 and int(w)<=100):
                            flag = True
                        else:
                            flag = False
                
                component.append(name)
                weight.append(int(w))
                print(component)
                print(weight)
                
            else:
                print("please enter either 1 or 2")
        conn = db.create_connection()
        for idx, value in enumerate(component):
            InsertString = "insert into Courses values('{}', '{}', '{}', '{}', '{}')".format(username, Course_ID, Course_Name, component[idx], weight[idx])
            conn.execute(InsertString)
        conn.commit()

    

def AddEntry(username):
    pass
