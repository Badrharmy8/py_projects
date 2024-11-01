from tkinter import *
from tkinter import messagebox
# make the gui
base = Tk()
base.title("Guess Game")
base.geometry("500x580+0+0")
base.resizable(False , False)
base.configure(bg = "#795757")

title = Label(base , text = "Guess The Word" , font = ("Calibri" , 25) , bg = "#795757"  , fg  = "white")
title.place(x = 120 , y = 30)
                      

lbl_lang = Label(base , text = "Guess A Programming Language :" , font = ("Calibri" , 18) , fg = "black" , bg = "#795757")
lbl_lang.place(x = 20 , y = 115) 
lchar1 = Entry(base , width = 3 , font = ("Calibri" , 18),bd = 0 , bg = "white")
lchar1.place(x = 35 , y = 170)
lchar2 = Entry(base , width = 3 , font = ("Calibri" , 18),bd = 0 , bg = "white")
lchar2.place(x = 80 , y = 170)
lchar3 = Entry(base , width = 3 , font = ("Calibri" , 18),bd = 0 , bg = "white")
lchar3.place(x = 125 , y = 170)
lchar4 = Entry(base , width = 3 ,font = ("Calibri" , 18) ,bd = 0 , bg = "white")
lchar4.place(x = 170 , y = 170)
lchar5 = Entry(base , width = 3 ,font = ("Calibri" , 18), bd = 0 , bg = "white")
lchar5.place(x = 215 , y = 170)
lchar6 = Entry(base , width = 3, font = ("Calibri" , 18) , bd = 0 , bg = "white")
lchar6.place(x = 260 , y = 170)

# guess a programming language
p_tries = 5
p_count = 0
def p_language():
    global p_count
    language = "python"
    if p_count < p_tries:
        if lchar1.get().lower() == language[0] and lchar2.get().lower() == language[1] and lchar3.get().lower() == language[2] and lchar4.get().lower() == language[3] and lchar5.get().lower() == language[4] and lchar6.get().lower() == language[5]:
            messagebox.showinfo("Success" , "Well Guessed") 
            
            lbl_city = Label(base , text = "Guess A City Name :" , font = ("Calibri" , 18) , fg = "black" , bg = "#795757")
            lbl_city.place(x = 20 , y = 260)
            c_char1 = Entry(base , width = 3 , font = ("Calibri" , 18), bd = 0 , bg = "white")
            c_char1.place(x = 35 , y = 315)
            c_char2 = Entry(base , width = 3 , font = ("Calibri" , 18), bd = 0 , bg = "white")
            c_char2.place(x = 80 , y = 315)
            c_char3 = Entry(base , width = 3 , font = ("Calibri" , 18), bd = 0 , bg = "white")
            c_char3.place(x = 125 , y = 315)
            c_char4 = Entry(base , width = 3 , font = ("Calibri" , 18), bd = 0 , bg = "white")
            c_char4.place(x = 170 , y = 315)
            c_char5 = Entry(base , width = 3 , font = ("Calibri" , 18), bd = 0 , bg = "white")
            c_char5.place(x = 215 , y = 315)
            c_char6 = Entry(base , width = 3 , font = ("Calibri" , 18), bd = 0 , bg = "white")
            c_char6.place(x = 260 , y = 315)
            c_char7 = Entry(base , width = 3 , font = ("Calibri" , 18), bd = 0 , bg = "white")
            c_char7.place(x = 305 , y = 315)
            c_char8 = Entry(base , width = 3 , font = ("Calibri" , 18), bd = 0 , bg = "white")
            c_char8.place(x = 350 , y = 315)

            
            # guess a city
            c_tries = 5
            def city():
                global c_count
                c_count = 0
                city = "mansoura"
                if c_count < c_tries:
                    if c_char1.get().lower() == city[0] and c_char2.get().lower() == city[1] and c_char3.get().lower() == city[2] and c_char4.get().lower() == city[3] and c_char5.get().lower() == city[4] and c_char6.get().lower() == city[5] and c_char7.get().lower() == city[6] and c_char8.get().lower() == city[7]  :
                        messagebox.showinfo("Success" , "Well Guessed")
                        
                        lbl_name = Label(base , text = "Guess A Boy Name : " , font = ("Calibri" , 18) , fg = "black" , bg = "#795757")
                        lbl_name.place(x = 20 , y = 405)
                        nchar1 = Entry(base , width = 3 ,font = ("Calibri" , 18), bd = 0 , bg = "white")
                        nchar1.place(x = 35 , y = 450)
                        nchar2 = Entry(base , width = 3 ,font = ("Calibri" , 18), bd = 0 , bg = "white")
                        nchar2.place(x = 80 , y = 450)
                        nchar3 = Entry(base , width = 3 ,font = ("Calibri" , 18), bd = 0 , bg = "white")
                        nchar3.place(x = 125 , y = 450)
                        nchar4 = Entry(base , width = 3 ,font = ("Calibri" , 18), bd = 0 , bg = "white")
                        nchar4.place(x = 170 , y = 450)

                        n_tries = 5
                        def name():
                            boy = "omar"
                            global n_count
                            n_count = 0
                            if n_count < n_tries:
                                if nchar1.get().lower() == boy[0] and nchar2.get().lower() == boy[1] and nchar3.get().lower() == boy[2] and nchar4.get().lower() == boy[3]:
                                    messagebox.showinfo("Sucess" , "Well Gussed\nCongratulation.")
                                else:
                                    messagebox.showerror("Error" , "Try Again") 
                                    nchar1.delete(first = 0 ,last = END)
                                    nchar2.delete(first = 0 ,last = END)    
                                    nchar3.delete(first = 0 ,last = END)    
                                    nchar4.delete(first = 0 ,last = END)
                                    n_count += 1
                            else:
                                 messagebox.showerror("Error" , "You Take All Tries.\n Losing!!")           
                                
                        but = Button(base, command = name ,width = 7, text = "Guessed" , font = ("Calibri" , 15 ) ,bd = 0, bg = "#795757" , fg = "black")
                        but.place(x = 115 , y = 495)

                    else:
                        messagebox.showerror("Error" , "Try Again")
                        c_char1.delete(first = 0 , last = END)
                        c_char2.delete(first = 0 , last = END)    
                        c_char3.delete(first = 0 , last = END)    
                        c_char4.delete(first = 0 , last = END)    
                        c_char5.delete(first = 0 , last = END)    
                        c_char6.delete(first = 0 , last = END)    
                        c_char7.delete(first = 0 , last = END)    
                        c_char8.delete(first = 0 , last = END)   
                        c_count += 1
                else:
                    messagebox.showerror("Error" , "You Take All Tries.\n Losing!!")  
                
            but = Button(base ,command = city,width = 7, text = "Guessed" , font = ("Calibri" , 15 ) ,bd = 0, bg = "#795757" , fg = "black")
            but.place(x = 115 , y = 360)  

        else:
            messagebox.showerror("Error" , "Try Again")
            lchar1.delete(first = 0 , last = END)
            lchar2.delete(first = 0 , last = END)    
            lchar3.delete(first = 0 , last = END)    
            lchar4.delete(first = 0 , last = END)    
            lchar5.delete(first = 0 , last = END)    
            lchar6.delete(first = 0 , last = END) 
            p_count += 1
    else:
        messagebox.showerror("Error" , "You Take All Tries.\n Losing!!") 

but = Button(base ,command = p_language , width = 7, text = "Guessed" , font = ("Calibri" , 15 ) ,bd = 0, bg = "#795757" , fg = "black")
but.place(x = 115 , y = 215)

    
base.mainloop()
