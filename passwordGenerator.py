from tkinter import * 
from tkinter import messagebox

# make the GUI
main = Tk()
main.title("Password Generator")
main.geometry("350x500")
main.resizable(FALSE , FALSE)

length = StringVar()
upper_char = StringVar()
lower_char = StringVar()
special_char = StringVar()
digit = StringVar()

# frame for inputs
input = Frame(main , width = 350 , height = 500 , bg = "#59788E")
input.place(x = 0 , y = 0)

# title for the frame

title = Label(input , text = "Generate Your Password" , font = ("Calibri" , 17, "bold") , bg = "#59788E" , fg = "black")
title.place(x = 45 , y = 3)

# make the entries

txt_length = Label(input ,  text = "Length Of The Password : " , font = ("Calibri" , 14) , bg = "#59788E" , fg = "black")
txt_length.place( x = 10 , y = 50)
length_entry = Entry(input , textvariable = length,width = 20)
length_entry.place(x = 20 , y = 85)

precentage = Label(input , text = "Precentages" , font = ("Calibri" , 16 , "bold") , bg = "#59788E" , fg = "black")
precentage.place(x = 80, y = 120)

txt_upper = Label(input ,text = "Upper Characters : " , font = ("Calibri" , 14) , bg = "#59788E" , fg = "black")
txt_upper.place( x = 10 , y = 165)
upper_entry = Entry(input ,textvariable = upper_char , width = 20)
upper_entry.place(x = 20 , y = 200)

txt_lower = Label(input ,text = "Lower Characters : " , font = ("Calibri" , 14) , bg = "#59788E" , fg = "black")
txt_lower.place( x = 10 , y = 235)
lower_entry = Entry(input ,textvariable = lower_char , width = 20)
lower_entry.place(x = 20 , y = 270)

txt_special = Label(input ,text = "Special Characters : " , font = ("Calibri" , 14) , bg = "#59788E" , fg = "black")
txt_special.place( x = 10 , y = 305)
special_entry = Entry(input ,textvariable = special_char , width = 20)
special_entry.place(x = 20 , y = 345)

txt_digit = Label(input ,text = "Digits : " , font = ("Calibri" , 14) , bg = "#59788E" , fg = "black")
txt_digit.place( x = 10 , y = 375)
digit_entry = Entry(input ,textvariable = digit , width = 20)
digit_entry.place(x = 20 , y = 410)

# clear function
def clear():
    length_entry.delete(first = 0 ,last = END)
    upper_entry.delete(first = 0 , last = END)
    lower_entry.delete(first = 0 , last = END)
    special_entry.delete(first = 0 , last = END)
    digit_entry.delete(first = 0 , last = END)

# generate function
def generate():
    import string
    import random
    upper_chars = list(string.ascii_uppercase)
    lower_chars = list(string.ascii_lowercase)
    digits = list(string.digits)
    special_chars = list(string.punctuation)
    random.shuffle(upper_chars)
    random.shuffle(lower_chars)
    random.shuffle(digits)
    random.shuffle(special_chars)
    pass_len = length_entry.get()
    
    pass_len = int(pass_len)
    if int(pass_len) < 5:
        messagebox.showerror("Error" , "The length must be > 5.")
        clear()
        pass_len = length_entry.get() 
    len1 = upper_entry.get() 
    len2 = lower_entry.get() 
    len3 = digit_entry.get()
    len4 = special_entry.get()           
        
    if int(len1) + int(len2) + int(len3) + int(len4) != 100:
        messagebox.showerror("Error","The Total Precentage Must Be 100.")
        clear()
        len1 = upper_entry.get() 
        len2 = lower_entry.get() 
        len3 = digit_entry.get()
        len4 = special_entry.get()                  
    part1 = round(int(pass_len) * (int(len1) / 100))
    part2 = round(int(pass_len) * (int(len2) / 100))
    part3 = round(int(pass_len) * (int(len3) / 100))
    part4 = round(int(pass_len) * (int(len4) / 100))
    password = []
    for i in range(part1):
        password.append(upper_chars[i])
    for i in range(part2):
        password.append(lower_chars[i])
    for i in range(part3):
        password.append(digits[i])
    for i in range(part4):
        password.append(special_chars[i])        
    random.shuffle(password) 
    the_password = "".join(password)   
    messagebox.showinfo("Sucess" , f"Password Is {the_password}")
    clear()


# button to show the password
show = Button(input , text = "Show Password" , command = generate, font = ("Calibri" , 11) , bg = "white" , fg = "black" , bd = 0)
show.place(x = 80 , y = 455)

main.mainloop()

