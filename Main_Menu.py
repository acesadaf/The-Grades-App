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
    Course_ID.strip()
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
        Course_Name.strip()
        active = True 
        component = []
        weight = []
        while(active):
            print("To Add a new course component, press 1, and if done, press 2")
            key = input()
            if key == '2':
                active = False
                continue
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
                continue
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
    print('For what course would you like to add a value?. Please enter the Course ID.')
    print('Here are all your course IDs: ')
    
    conn = db.create_connection()
    CheckString = "Select distinct(Course_ID) from Courses where username = '{}'".format(username)
    MyCursor = conn.cursor()
    MyCursor.execute(CheckString)
    rows = MyCursor.fetchall()
    for row in rows:
        print(row[0])
    active = True
    while(active):
        Course_ID = input()
        CheckString = "Select Course_ID from Courses where username = '{}' AND Course_ID = '{}'".format(username, Course_ID)
        MyCursor.execute(CheckString)
        rows = MyCursor.fetchall()
        if(len(rows)>0):
            active = False
        else:
            print("This course does not exist!")
            print("Press 1 to try again, and 2 to exit")
            while(1):
                key2 = input()
                if key2 == '1':
                    break
                if key2 == '2':
                    return 
                else:
                    print("Please press either 1 or 2!")

        while(1):
            CheckString = "Select component from Courses where username = '{}' and Course_ID = '{}'".format(username, Course_ID)
            MyCursor = conn.cursor()
            MyCursor.execute(CheckString)
            rows = MyCursor.fetchall()
            complist = []
            for row in rows:
                complist.append(row[0])

            
            newlist = complist.copy()
            for idx, row in enumerate(rows):
                print(idx)
                Check_If_Already_Added = "Select * from Entries where username = '{}' and Course_ID = '{}' and Component = '{}'".format(username, Course_ID, complist[idx])
                MyCursor.execute(Check_If_Already_Added)
                ent = MyCursor.fetchall()
                if(len(ent) > 0):
                    newlist.remove(complist[idx]) 

            if(len(newlist) == 0):
                print("All information for this course is already added! Returning to Main Menu")
                return        
            print("Here's a list of all the components of this course.")        
            print(newlist)

            print("For what component would you like to make an entry?")
            print (newlist)
            comp = input()
            flag = False 
            while comp not in newlist:
                if flag == False:
                    print("This component does not exist! Press 1 to try again, and 2 to exit")
                    flag = True
                key4 = input()
                if key4 == '1':
                    print("Lets try again. Which component?")
                    comp = input()
                    if comp not in newlist:
                        print("This component does not exist! Press 1 to try again, and 2 to exit")
                    continue
                if key4 == '2':
                    return 
                else:
                    print("please press either 1 or 2.")
            print("Great! Lets make an entry for {}".format(comp))
            
            print("How many points was this worth?")
            total = "placeholder"
            while(total.isnumeric()!=True):
                print("Please enter a numeric value.")
                total = input()
            total = int(total)
            print("How many points did you score?")
            scored = "placeholder"
            while(scored.isnumeric()!=True):
                print("Please enter a numeric value.")
                scored = input()
            scored = int(scored)
            InsertString = "insert into Entries values('{}', '{}', '{}', '{}', '{}')".format(username, Course_ID, comp, scored, total)
            conn.execute(InsertString)
            conn.commit()
            print("Would you like to add results for another component? If so press 1, otherwise press 2 to exit.")
            while(1):
                key5 = input()
                if key5 == '1':
                    break
                if key5 == '2':
                    db.close_connection(conn)
                    return
                else:
                    print("Please enter either 1 or 2!")







                



            





    

