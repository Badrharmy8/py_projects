from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# create the gui
root = Tk()
root.title("Employees Managment")
root.geometry("620x500+0+0")
root.resizable(False , False)
root.configure(bg = "#C5C6D0")

# title
title = Label(text = "Employee Data" , font = ("Calibri" , 23) , bg = "#C5C6D0" , fg = "black")
title.place(x = 200 , y = 5)

# entries
name = StringVar()
lbl_name = Label(text = "Name: " , font = ("Calibri" , 15) , bg = "#C5C6D0" , fg = "black")
lbl_name.place(x = 20 , y = 70) 
name_entry = Entry(root,textvariable = name, width = 25 , font = ("Calibri" , 13))
name_entry.place(x = 20 , y = 100)

age = DoubleVar()
lbl_age = Label(text = "Age: " , font = ("Calibri" , 15) , bg = "#C5C6D0" , fg = "black")
lbl_age.place(x = 20 , y = 140) 
age_entry = Entry(root, textvariable = age , width = 25 , font = ("Calibri" , 13))
age_entry.place(x = 20 , y = 170)

job = StringVar()
lbl_job = Label(text = "Job: " , font = ("Calibri" , 15) , bg = "#C5C6D0" , fg = "black")
lbl_job.place(x = 20 , y = 210) 
job_entry = Entry(root ,textvariable = job, width = 25 , font = ("Calibri" , 13))
job_entry.place(x = 20 , y = 240)

gender = StringVar()
lbl_gender = Label(text = "Gender: " , font = ("Calibri" , 15) , bg = "#C5C6D0" , fg = "black")
lbl_gender.place(x = 20 , y = 280) 
gender_entry = ttk.Combobox(root,textvariable = gender , width = 23 , font = ("Calibri" , 13))
gender_entry["values"] = ["Male" , "Female"]
gender_entry.place(x = 20 , y = 310)

phone = StringVar()
lbl_phone = Label(text = "Phone: " , font = ("Calibri" , 15) , bg = "#C5C6D0" , fg = "black")
lbl_phone.place(x = 350 , y = 70) 
phone_entry = Entry(root,textvariable = phone , width = 25 , font = ("Calibri" , 13))
phone_entry.place(x = 350 , y = 100)

email = StringVar()
lbl_email = Label(text = "Email: " , font = ("Calibri" , 15) , bg = "#C5C6D0" , fg = "black")
lbl_email.place(x = 350 , y = 140) 
email_entry = Entry(root,textvariable = email , width = 25 , font = ("Calibri" , 13))
email_entry.place(x = 350 , y = 170)

salary = DoubleVar()
lbl_salary = Label(text = "Salary: " , font = ("Calibri" , 15) , bg = "#C5C6D0" , fg = "black")
lbl_salary.place(x = 350 , y = 210) 
salary_entry = Entry(root, textvariable = salary , width = 25 , font = ("Calibri" , 13))
salary_entry.place(x = 350 , y = 240)

address = StringVar()
lbl_address = Label(text = "Address: " , font = ("Calibri" , 15) , bg = "#C5C6D0" , fg = "black")
lbl_address.place(x = 350 , y = 280) 
address_entry = ttk.Combobox(root, textvariable = address , width = 23 , font = ("Calibri" , 13))
address_entry["values"] = ["Mansoura" , "Alexandria" , "Cairo" , "Aswan" , "Luxor" , "Other"]
address_entry.place(x = 350 , y = 310)

def delete_entries():
    """function for deleting data from entries"""
    name_entry.delete(first = 0 , last = END)
    age_entry.delete(first = 0 , last = END)
    job_entry.delete(first = 0 , last = END)
    gender_entry.delete(first = 0 , last = END)
    phone_entry.delete(first = 0 , last = END)
    email_entry.delete(first = 0 , last = END)
    salary_entry.delete(first = 0 , last = END)
    address_entry.delete(first = 0 , last = END)

# connect database
import sqlite3
db = sqlite3.connect("mydata.db")
cr = db.cursor()
# create table for employess
cr.execute(
    "CREATE TABLE IF NOT EXISTS employee(id INTEGER ,name TEXT , age INTEGER , job TEXT , gender TEXT , phone TEXT , email TEXT , salary INTEGER , address TEXT)")

id = 1
def add():
    global id
    """function to insert employee data in database"""
    cr.execute(
        "INSERT INTO employee VALUES(?,?,?,?,?,?,?,?,?)",(id , name.get() , age.get() , job.get() , gender.get() , phone.get() , email.get(), salary.get(), address.get()))
    messagebox.showinfo("Success" , f"{name.get()} is added successfuly.")
    id += 1
    db.commit()
    delete_entries()

def show():
    """dislay data from database"""
    # fetching data from database
    cr.execute(
        "SELECT * FROM employee")
    data = cr.fetchall()
    # gui for display data from database
    new = Tk()
    new.title("Employees")
    new.geometry("800x700+150+50")
    new.configure(bg = "#C5C6D0")
    num = 1
    j = 10
    for row in data:
        text = Label(new ,text = (f"Employee {num}\nID : {row[0]},  Name: {row[1]},  Age: {row[2]},  Job: {row[3]},  Gender: {row[4]},\nPhone: {row[5]},  Email: {row[6]},  Salary: {row[7]},  Address: {row[8]}\n\n")   
                    , font = ("Calibri" , 15) , bg = "#C5C6D0" , fg = "black")
        text.place(x = 10 , y = j)
        num += 1
        j += 100    
    db.commit()

def delete():
    """"function for deleting employee""" 
    dl_gui = Tk()
    dl_gui.geometry("400x320+650+100")
    dl_gui.title("Delete Employee")
    dl_gui.configure(bg = "#C5C6D0")

    # make the entries
    text = Label(dl_gui , text = "Deleting Employee" , font = ("Calibri" , 18) , bg = "#C5C6D0" , fg = "black")
    text.place(x = 90 , y = 10)

    d_id = StringVar()
    dl_id = Label(dl_gui , text = "Employee Id: " , font = ("Calibri" , 15) , bg = "#C5C6D0" , fg = "black")
    dl_id.place(x = 40 , y = 70)
    dl_entry = Entry(dl_gui, textvariable = d_id , width = 20 , font = ("Calibri" , 13))
    dl_entry.place(x = 40 , y = 110)

    d_name = StringVar()
    dl_name = Label(dl_gui , text = "Employee Name: " , font = ("Calibri" , 15) , bg = "#C5C6D0" , fg = "black")
    dl_name.place(x = 40 , y = 160)
    dln_entry = Entry(dl_gui ,textvariable = d_name, width = 20 , font = ("Calibri" , 13))
    dln_entry.place(x = 40 , y = 200)

    def deleting_btn():
        cr.execute(
        "DELETE FROM employee WHERE id = ? AND name = ?" , (dl_entry.get() , dln_entry.get()))
        messagebox.showinfo("Success" , f"{dln_entry.get()} is deleting")
        db.commit()
        dl_entry.delete(first = 0 , last = END)
        dln_entry.delete(first = 0 , last = END)


    # deleting button
    del_btn = Button(dl_gui ,command = deleting_btn,
                     text = "Delete" , width = 10 , bd = 0 , bg = "white" , font = ("Calibri" , 12))
    del_btn.place(x = 150 , y = 250)


add_btn = Button(root ,command = add ,text = "Add Employee" , width = 15 , bd = 0 , bg = "white" , font = ("Calibri" , 12))
add_btn.place(x = 150 , y = 375)

delete_btn = Button(root ,command = delete ,text = "Delete Employee" , width = 15 , bd = 0 , bg = "white" , font = ("Calibri" , 12))
delete_btn.place(x = 300 , y = 375)

show_btn = Button(root ,command = show ,text = "Show Employees" , width = 15 , bd = 0 , bg = "white" , font = ("Calibri" , 12))
show_btn.place(x = 230 , y = 420) 


root.mainloop()