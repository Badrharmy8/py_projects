# create the database
import sqlite3
db = sqlite3.connect("Tasks.db")
cr = db.cursor()

# create the table for tasks
cr.execute(
    "CREATE TABLE IF NOT EXISTS work_task(id INTEGER, name TEXT , priority TEXT , limited time TEXT)")
cr.execute(
    "CREATE TABLE IF NOT EXISTS shopping_task(id INTEGER, name TEXT , priority TEXT , limited time TEXT)")
cr.execute(
    "CREATE TABLE IF NOT EXISTS personal_task(id INTEGER, name TEXT , priority TEXT , limited time TEXT)")
cr.execute(
    "CREATE TABLE IF NOT EXISTS completed_task(name TEXT , priority TEXT , limited time TEXT , category TEXT)")

# class for the task
class Task:
    def task(self):
        """function for adding tasks"""
        name = input("Write Your Task: ").capitalize()
        priority = input("Its Priority Between Other Taskes: ").capitalize()
        limited_time = input("Limited Time To Finish It: ")
        category = input("Your Task Is 'Work , Shopping , Personal'? ").capitalize()    
        if category == "Work":
                cr.execute(
                    "INSERT INTO work_task VALUES(?, ? , ? , ?)",(1 , name , priority , limited_time))
                db.commit()
        elif category == "Shopping":
                cr.execute(
                    "INSERT INTO shopping_task VALUES(?, ? , ? , ?)",(2 , name , priority , limited_time))
                db.commit()
        elif category == "Personal":
                cr.execute(
                    "INSERT INTO personal_task VALUES(?, ? , ? , ?)",(3 , name , priority , limited_time))           
                db.commit()

    def show(self):
        """function for displaying tasks"""
        task_type = input("Display Completed Tasks Or Not Completed? ")
        if task_type.capitalize() == "Completed tasks" or task_type.capitalize() == "Completed":
            tasks =  cr.execute(
                "SELECT * FROM completed_task")
            print("Completed Tasks: ")  
            for row in tasks:  
                print(row[0])
        elif task_type.capitalize() == "Not completed tasks" or task_type.capitalize() == "Not completed":        
            user_choose = input("Display 'Work Tasks' Or 'Personal Tasks' Or 'Shopping Tasks' Or 'All'? ").capitalize()
            if user_choose == "Work tasks" or user_choose == "Work":
                tasks1 =  cr.execute(
                    "SELECT * FROM work_task")
                print("Work Tasks: ")  
                for row in tasks1:  
                    print(row[1])
            elif user_choose == "Personal tasks" or user_choose == "Personal":
                tasks2 =  cr.execute(
                    "SELECT * FROM personal_task")
                print("Personal Tasks: ") 
                for row in tasks2:   
                    print(row[1])    
            elif user_choose == "Shopping tasks" or user_choose == "Shopping":
                tasks3 =  cr.execute(
                    "SELECT * FROM shopping_task")
                print("Shopping Tasks: ")
                for row in tasks3:    
                    print(row[1])    
            elif user_choose == "All tasks" or user_choose == "All":
                w_tasks =  cr.execute(
                    "SELECT * FROM work_task")
                print("Work Tasks: ")
                for row in w_tasks:
                    print(row[1])    
                p_tasks =  cr.execute(
                    "SELECT * FROM personal_task")
                print("Personal Tasks: ")
                for row in p_tasks:
                    print(row[1])    
                s_tasks =  cr.execute(
                    "SELECT * FROM shopping_task")
                print("Shopping Tasks: ")
                for row in s_tasks:
                    print(row[1])            
            else:
                print("Your Choose Is Not Exist.")    

    def delete(self):
        """function for deleting task"""
        task_name = input("Enter The Task Name: ").capitalize()
        task_type = input("Work Task Or Personal Task Or Shopping Task: ").capitalize()
        if task_type == "Work" or task_type == "Work task":
            cr.execute(
                "DELETE FROM work_task WHERE name = ?",(task_name,))
            db.commit()
        elif task_type == "Personal" or task_type == "Personal task":
            cr.execute(
                "DELETE FROM personal_task WHERE name = ?",(task_name,))        
            db.commit()
        elif task_type == "Shopping" or task_type == "Shopping task":
            cr.execute(
                "DELETE FROM shopping_task WHERE name = ?",(task_name,))
            db.commit()    

    def complete(self):
        """function for completed tasks"""
        task_name = input("Enter The Task Name: ").capitalize()
        task_type = input("Work Task Or Personal Task Or Shopping Task: ").capitalize()
        if task_type == "Work" or task_type == "Work task":
            w_task = cr.execute(
                "SELECT * FROM work_task WHERE name = ?" ,(task_name,)).fetchall()
            cr.execute(
                "INSERT INTO completed_task VALUES(?,?,?,?)",(w_task[0][1] , w_task[0][2] , w_task[0][3] , "Work"))
            cr.execute(
                "DELETE FROM work_task WHERE name = ?",(task_name,))
            db.commit()     
        elif task_type == "Personal" or task_type == "Personal task":
            p_task = cr.execute(
                "SELECT * FROM personal_task WHERE name = ?" ,(task_name,)).fetchall()
            cr.execute(
                "INSERT INTO completed_task VALUES(?,?,?,?)",(p_task[0][1] , p_task[0][2] , p_task[0][3] , "Personal")) 
            cr.execute(
                "DELETE FROM personal_task WHERE name = ?",(task_name,))
            db.commit()     
        elif task_type == "Shopping" or task_type == "Shopping task":
            s_task = cr.execute(
                "SELECT * FROM shopping_task WHERE name = ?" ,(task_name,)).fetchall()   
            cr.execute(
                "INSERT INTO completed_task VALUES(?,?,?,?)",(s_task[0][1] , s_task[0][2] , s_task[0][3] , "Shopping")) 
            cr.execute(
                "DELETE FROM shopping_task WHERE name = ?",(task_name,))
            db.commit()                    


# object to the class
task = Task()
# input message
operation = """There Are Many Operations To Do
"Add Task" , "Finish Task" , "Delete Task" , "Display Tasks" 
Write One Of This Operations: """
user_input = input(operation)
# detremine the operation
if user_input.capitalize() == "Add task" or user_input.capitalize() == "Add":
    task.task()        
elif user_input.capitalize() == "Display task" or user_input.capitalize() == "Display":
    task.show()
elif user_input.capitalize() == "Delete task" or user_input.capitalize() == "Delete":
    task.delete()      
elif user_input.capitalize() == "Finish task" or user_input.capitalize() == "Finish":
    task.complete()  