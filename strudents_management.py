import sqlite3
# connect database
db = sqlite3.connect("data.db")
cr = db.cursor()
# make two tables
db.execute(
    "CREATE TABLE IF NOT EXISTS student(s_id INTEGER , s_name TEXT , s_age INTEGER)"
)
db.execute(
    "CREATE TABLE IF NOT EXISTS course(c_id INTEGER , c_name TEXT , degree INTEGER , s_id INTEGER)"
)

def save_changes():
    """function for saving changes and close database"""
    db.commit()
    db.close()
    print("Database Is Closed.")

def add():
    """adding student or courses"""
    user_choose = input("Student Or Course? ").strip().lower()
    if user_choose == "student":
        s_name = input("Write Student Name: ").strip().capitalize()
        s_id = input("Write Student Id: ").strip()
        s_age = input("Write Student Age: ").strip()
        cr.execute(
            "INSERT INTO student(s_id , s_name , s_age) VALUES(? , ? , ?)",(s_id , s_name , s_age)
        )
    elif user_choose == "course":
        c_name = input("Write Course Name: ").strip().capitalize()
        c_id = input("Write Course Id: ").strip() 
        degree = input("Write Degree: ").strip()
        s_id = input("Write Student Id: ").strip()
        cr.execute(
            "INSERT INTO course(c_id , c_name , degree , s_id) VALUES(? , ? , ? , ?)",(c_id , c_name , degree , s_id)
        ) 
    else:
        print("Only Choose Student Or Course")
    save_changes()        

def delete():
    """"delete data from database"""
    user_choose = input("Student Or Course: ").strip().lower()
    if user_choose == "student":
        s_id = input("Enter Student Id: ").strip()
        cr.execute(
            "DELETE FROM student WHERE s_id = ?" , (s_id)
        )
    elif user_choose == "course":
        c_id = input("Enter Course Id: ").strip()
        id = input("Enter Student Id: ").strip()
        cr.execute(
            "DELETE FROM course WHERE c_id = ? AND s_id = ?" , (c_id , id)
        )    
    else:
        print("Only Choose Student Or Course")
    save_changes()  

def update():
    """updating data"""
    user_choose = input("Student Or Course: ").strip().lower()
    if user_choose == "student":
        s_id = input("Enter Student Id: ").strip()
        s_age = input("Write The New Age: ").strip()
        cr.execute(
            "UPDATE student SET  s_age = ? WHERE s_id = ?" ,(s_age , s_id))
    elif user_choose == "course":
        id , c_id = input("Enter Student Id And Course Id: ").split()
        c_degree = input("Write The New Degree: ").strip()
        cr.execute(
            "UPDATE course SET degree = ? WHERE c_id = ? AND s_id = ?",(c_degree , c_id , id))
    else:
        print("Only Choose Student Or Course")
    save_changes()        

def show():
    """showing all data"""
    cr.execute(
        "SELECT * FROM student")
    students = cr.fetchall()
    cr.execute(
        "SELECT * FROM course")
    courses = cr.fetchall()
    for student in students:
        print(f"Student Id => {student[0]} , Student Name => {student[1]} , Student Age => {student[2]}")
        for course in courses:
            if course[3] == student[0]:
                print(f"Course Id => {course[0]} , Course Name => {course[1]} , Course Degree => {course[2]}")
        print("**********************************************************")        
    save_changes()

# input message
input_message = """There Are Many Actions You Can Do.
a >> Adding 
d >> Deleting
u >> Updating
s >> Showing All Data
q >> Closing The App
Choose The Needed Action: 
"""

# take the input from user
user_input = input(input_message).strip().lower()

actions_list = ["a" , "d" , "u" , "s" , "q"]

# check the action
if user_input in actions_list:
    if user_input == "a":
        add()
    elif user_input == "d":
        delete()
    elif user_input == "u":
        update()
    elif user_input == "s":
        show()
    else:
        print("The App Is Closed.")                
else:
    print("Sorry,This Action Not Exist.")