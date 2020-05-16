import random
import sqlite3
from tkinter import *

# __________________________________________________________________________________
#Define variables

Random_list = []                    # it will store all 10 random value
ID_list = []                        # it will store top 4 value of random variable
Total_score = 0
ID_get = []                         # it will store value given by checkbutton
Names = []                          # it will storegiven
play=True
counter = 10                        # for timer in image module
counter_option=20                   # for timer in option module

# ___________________________________________________________________________________
# ranfom function to genarate 10 random number and store in variable list


def random_generate():
    i = 0
    while i < 10:
        random_number = random.randrange(1, 40)       # generating random number (max value 40)
        if random_number in Random_list:              # this will remove duplicate number
            pass
        else:
            Random_list.append(random_number)
            i=i+1

#______________________________________________________________________________________
# access sqlite database to take input from database


def database():
    local = sqlite3.connect('DATABASE.db')
    temp = local.execute('select * from s2')
    for j in temp:
        local.commit()
        if j[0] in Random_list:
            Names.append(j[1])
    print(Names)

#------------------------------------------------------------------------------------------


def show_option():
    root=Tk()
    root.title("Project")
    root.geometry('1500x1000')

    label = Label(root, text="Welcome!", fg="black", font="Verdana 35 bold")
    label.place(x=1200, y=100)
# ------------------------------------------------
# this function is for timer of 20 second
    def count(): 
        global counter_option
        # To manage the intial delay. 
        if counter_option==-1:
            counter_option=20           
            root.destroy()
        else: 
            display=str(counter_option) 
        label['text']=display
        label.after(1000, count)  
        counter_option -= 1
    count()

# below function is to exit from current  window
# and it will also set value of counter for next time so that it starts fron 10
    def eliminate():
        global counter_option
        counter_option=20
        root.destroy()


#----------------------------------------------
#function to set variable into list chosen by user

    setVar = IntVar()                   #variable for buttons
    def get_value():
        if setVar.get() in ID_get:
             pass
        else:
            ID_get.append(int(setVar.get())-1)
            print(ID_get)

#--------------------------------------------
#function to clear all selection
    def refresh():
        while ID_get:
            ID_get.pop()
        setVar.set(0)

# --------------------------------------------
    checkButton0 = Checkbutton(root,text = Names[0],variable = setVar,onvalue = 1, offvalue = 0,height = 3,width = 18,
        font='KacstOffice 25 bold',bd=5,justify=LEFT,command = get_value)
    checkButton0.grid(row=0, sticky=W) 

    checkButton1 = Checkbutton(root,text = Names[1],variable = setVar,onvalue = 2, offvalue = 0,height = 3,width = 18,
        font='KacstOffice 25 bold',bd=5,justify=LEFT,command = get_value)
    checkButton1.grid(row=1, sticky=W) 

    checkButton2 = Checkbutton(root,text = Names[2],variable = setVar,onvalue = 3, offvalue = 0,height = 3,width = 18,
        font='KacstOffice 25 bold',bd=5,justify=LEFT,command = get_value)
    checkButton2.grid(row=2, sticky=W) 

    checkButton3 = Checkbutton(root,text = Names[3],variable = setVar,onvalue = 4, offvalue = 0,height = 3,width = 18,
        font='KacstOffice 25 bold',bd=5,justify=LEFT,command = get_value)
    checkButton3.grid(row=3, sticky=W)

    checkButton4 = Checkbutton(root,text = Names[4],variable = setVar,onvalue = 5, offvalue = 0,height = 3,width = 20,
        font='KacstOffice 25 bold',bd=5,justify=LEFT,command = get_value)
    checkButton4.grid(row=4, sticky=W)  

    checkButton5 = Checkbutton(root,text = Names[5],variable = setVar,onvalue = 6, offvalue = 0,height = 3,width = 18,
        font='KacstOffice 25 bold',bd=5,justify=LEFT,command = get_value)
    checkButton5.grid(row=0, column=1, sticky=W)  

    checkButton6 = Checkbutton(root,text = Names[6],variable = setVar,onvalue = 7, offvalue = 0,height = 3,width = 18,
        font='KacstOffice 25 bold',bd=5,justify=LEFT,command = get_value)
    checkButton6.grid(row=1, column=1, sticky=W)  
    
    checkButton7 = Checkbutton(root,text = Names[7],variable = setVar,onvalue = 8, offvalue = 0,height = 3,width = 20,
        font='KacstOffice 25 bold',bd=5,justify=LEFT,command = get_value)
    checkButton7.grid(row=2, column=1, sticky=W)

    checkButton8 = Checkbutton(root,text = Names[8],variable = setVar,onvalue = 9, offvalue = 0,height = 3,width = 20,
        font='KacstOffice 25 bold',bd=5,justify=LEFT,command = get_value)
    checkButton8.grid(row=3, column=1, sticky=W)

    checkButton9 = Checkbutton(root,text = Names[9],variable = setVar,onvalue =10, offvalue = 0,height = 3,width = 20,
        font='KacstOffice 25 bold',bd=5,justify=LEFT,command = get_value)
    checkButton9.grid(row=4, column=1, sticky=W)

    Button(root,text = "OK", command=eliminate, padx=20, pady=3,font='Caladea 15 bold').place(x=1200,y=200)
    #Button(root,text = "OK",command = check_value).pack()
    Button(root,text = "Refresh",command = refresh, padx=20, pady=3,font='Caladea 15 bold').place(x=1200, y=300)
    root.mainloop()

# ________________________________________________________________________________________________________________________________________
# Function to show image on screen wiith timer 

def show_image():

    root=Tk()
    root.title("Project")
    root.geometry('1500x1000')
    label = Label(root, text="Welcome!", fg="black", font="Verdana 35 bold")
    label.place(x=1200, y=100)

# ---------------------------------------------
# below function is for  Timer of 10 second
    def count(): 
        global counter 
        # To manage the intial delay. 
        if counter==-1:
            counter=10           
            root.destroy()
        else: 
            display=str(counter) 
        label['text']=display
        label.after(1000, count)  
        counter -= 1
    count()

# ------------------------------------------------
# below function is to exit from current  window
# and it will also set value of counter for next time so that it starts fron 10
    def eliminate():
        global counter
        counter=10
        root.destroy()

# ----------------------------------------------------
# image_frame1=Frame(root,width = 1100, height = 600)
# image_frame1.pack()
    c = Canvas(width = 1000, height = 630, bg='grey')
    c.place(x=100,y=30)
    image_1 = PhotoImage(file = str(ID_list[0])+'.gif')        # ID_list = [0]
    image_2 = PhotoImage(file = str(ID_list[1])+'.gif')        # ID_list = [1]
    image_3 = PhotoImage(file = str(ID_list[2])+'.gif')        # ID_list = [2]
    image_4 = PhotoImage(file = str(ID_list[3])+'.gif')        # ID_list = [3]
    c.create_image(10+65, 0+50, image = image_1, anchor = NW)
    c.create_image(440+75,0+50, image = image_2, anchor = NW)
    c.create_image(10+65,350, image = image_3, anchor = NW)
    c.create_image(440+75,350, image = image_4, anchor = NW)
    #Button(root,text="OK", command=image_frame1.destroy).pack()
    Button(root,text="OK", command=eliminate, padx=20, pady=3,font='Caladea 15 bold').place(x=1200,y=200 )#grid(row=2, column=5, sticky=S)
    #image_frame1.mainloop()
    root.mainloop()

#____________________________________________________________________________________
# function to show the result 
def show_result():
    root=Tk()
    root.title("Project")
    root.geometry('1500x1000')   
    print(Total_score)

# ----------------------------------------
#function to replay game

    def replay():
        global Total_score
        global play
        Total_score=0
        play=True
        root.destroy()

    label = Label(root, text="Your Total score is :", fg="black", font="Verdana 45 bold")

    label2 = Label(root, text=Total_score, fg="black", font='Verdana 40 bold', )
    label.pack()
    Label(root).pack()
    label2.pack()
    Label(root).pack()
    Button(root,text = "exit", fg="black", font="Caladea 30 bold", command=root.destroy).pack()
    #Button(root,text = "OK",command = check_value).pack()
    Label(root).pack()
    Button(root,text = "replay", fg="black", font="Caladea 30 bold",command=replay).pack()
    root.mainloop()



#______________________________________________________________________________
# function to calculate the result
def check_result():
    for i in ID_get:
        global Total_score
        if i in ID_list:
            Total_score+=4
        else:
            Total_score-=1

# _____________________________________________________________
# function to clear/empty all the variable
def clear_all():
    while ID_get:
        ID_get.pop()
    while Random_list:
        Random_list.pop()
        Names.pop()


#----------------------------------------------------------------------
# Main function starts here

while play:
    play=False
    for j in range(5):
        print()
        random_generate()
        database()
        ID_list= Random_list[0:4]
        show_image()
        show_option()
        check_result()
        clear_all()
    show_result()
