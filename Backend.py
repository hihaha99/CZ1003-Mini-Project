############### Module Importing and Setting Up of Wallpaper, Pickle ###############
from tkinter import Entry, Tk, Canvas, Label, Button, Frame, StringVar, Toplevel 
from tkinter import ttk, font, messagebox
import tkinter.scrolledtext as tkst # Allows access to scrolledtext widget for displaying of stalls
from tkcalendar import Calendar
from PIL import Image, ImageTk #Allows access to PIL to display picture as wallpaper
import datetime
from time import strftime

import os 
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) #Allows opening of database and background 
import pickle
with open(os.path.join(__location__,"database.pickle"),"rb") as f: #
    allStalls_dict = pickle.load(f)

############### Backend of GUI ##############

#Initalise Shell
shell=Tk()
shell.geometry("700x680")
shell.resizable(0,0)
shell.title('North Spine Canteen Information System')
shell.columnconfigure(0, weight=1)
shell.rowconfigure(0, weight=1)

#Allows for dropdown menu configuration
fontDropDown = font.Font(family="Comics Sans MS",size=15)
shell.option_add("*TCombobox*Listbox*Font", fontDropDown)

#Initialise Frames
frame1 = Frame(shell)
frame2 = Frame(shell, bg='gray22')
for j in range(0,4):
    frame2.columnconfigure(j, weight = 1)
frame3 = Frame(shell)
frame4 = Frame(shell)
frame5 = Frame(shell)
frame6 = Frame(shell)
screen1 = Canvas(frame1)
def clock(): 
    currentDateTime = "Current date and time: "+strftime('%Y-%m-%d %H:%M:%S')
    clockLabel.config(text = currentDateTime, font=("Comic Sans MS", 15)) 
    clockLabel.after(10, clock)

#Build frames using Grid Geometry Manager, allow content to fit window size using "sticky"
for frame in (frame1, frame2, frame3, frame5):
    frame.grid(row=0, column=0, sticky="nsew")

#Format Background Photo
bgPhoto = Image.open(os.path.join(__location__, 'Background.jpg'))
bgPhoto = bgPhoto.resize((700,680), Image.ANTIALIAS)
wallpaper = ImageTk.PhotoImage(bgPhoto)

############### Global Variables and Calendar ###############
# Set default global variables for the entries of stall waiting time and number of people. 
# This is so that both functions showStalls() and showWaitingTime() can refer to it.
# Set calendar for getCustomStalls()
VarPeople = StringVar()
VarStall = StringVar()
VarH = StringVar() # Hours for User Defined Time
VarM = StringVar() # Minutes for User Defined Time
timeListHours = [x for x in range(0,24)]
timeListMinutes = [y for y in range(0,60)]

calendar = Calendar(frame2,
                   font="Arial 15", selectmode='day',
                   cursor="hand1", year=2019, month=11, day=1)

############### Functions Definitions ###############

def checkDatabase(inputDate, inputTime):
    stallsInfo = [] #Creates empty list for stall info to print
    openStalls = [] #Creates empty list for names of stalls
    for item in allStalls_dict: #Reiterate through each stall
        if inputDate in item["Operating Days"]:
            if item["Operating Hours"][0] <= inputTime < item["Operating Hours"][1]: #Check if stalls are open during specified hours
                openStalls.append(item["Name"]) #Appends names of stalls only to list
                stallsInfo.append("\nStall : "+item["Name"]) #Appends name of stalls to list for stall info
                for key in item["Food available"]: #Reiterate through foods available for each stall
                    if inputDate in item["Food available"][key][1]: #Check if food is available during specified date
                        if item["Food available"][key][2] <= inputTime < item["Food available"][key][3]: #Check food availability during specified time
                            stallsInfo.append(key + " " +"-"*(35-(len(key)+len(item["Food available"][key][0]))) \
                                + " " + item["Food available"][key][0]) #Appends food items and prices to list
    stallsInfo.append(" ")
    return (stallsInfo, openStalls) #Returns both lists for printing in getCustomStalls() and getCurrentStalls()

#Checks database against custom date/time and checks for available foods
def getCustomStalls():
    Hour = int(VarH.get())
    Minute = int(VarM.get())
    Second = 0
    date = calendar.selection_get() #Gets date selected on calendar
    customDate = date.weekday()# Converts date to weekday, from 0 to 6
    customTime = datetime.time(Hour,Minute,Second)
    customStalls = checkDatabase(customDate, customTime)
    return customStalls

#Checks database against current date/time and checks for available foods
def getCurrentStalls():
    currentTime = datetime.datetime.now().time()
    currentDate = datetime.datetime.now().weekday()
    currentStalls = checkDatabase(currentDate, currentTime)
    return currentStalls

#Generates screen for custom stalls after getting user input date and time
def showStallsCustom():
    try:
        listOpenStallsCustom = getCustomStalls()[1] #Will lead to exception if value not selected in getCustomStalls()

        if listOpenStallsCustom == []: #If no stalls available, prompt for different timing
            return messagebox.showerror('No Stores Available',"All stores are closed.\nPlease enter a different timing.")

        #Creates screen for custom stalls
        frame4 = Toplevel(frame2) #Pop up new frame
        frame4.geometry("700x680")
        screen4=Canvas(frame4)
        screen4.create_image(0,0,image=wallpaper,anchor="nw")
        screen4.pack(expand="true",fill="both")

        #Adds labels, menu info and buttons
        intro4Label=Label(screen4,
                font=("Comic Sans MS", 15),
                bg='gray22',
                height=1,
                fg="white",
                text="Current Stalls and Food Available:")
        screen4.create_window(190, 120, anchor="nw", window=intro4Label)

        menuInfoCustom="\n".join(getCustomStalls()[0]) #Use getCustomStalls() function and print out the menu details
        menuTextCustom = tkst.ScrolledText(screen4,
                        font=("Comic Sans MS", 15),
                        bg='gray22',
                        fg="white",
                        wrap = "word",
                        width = 35,
                        height = 13)
        menuTextCustom.pack(fill="both",expand=True,padx = 8, pady = 8)
        menuTextCustom.tag_config("justified", justify = "center")
        menuTextCustom.insert("insert", menuInfoCustom, "justified")
        menuTextCustom.config(state="disabled")
        screen4.create_window(130, 160, anchor="nw", window=menuTextCustom)

        Label_4A=Label(screen4,
            text=" Enter number of people waiting: ",
            font=("Comic Sans MS", 15),
            bg='gray22',
            fg="white")
        screen4.create_window(50, 550, anchor="nw", window=Label_4A)

        getPeopleCustom = Entry(screen4, font = ("Comic Sans MS", 15), width = 5, textvariable = VarPeople)
        screen4.create_window(380, 550, anchor="nw", window=getPeopleCustom)

        Label_4B=Label(screen4,
                    text="Choose stall: ",
                    font=("Comic Sans MS", 15),
                    bg='gray22',
                    fg="white")
        screen4.create_window(50, 600, anchor="nw", window=Label_4B)

        getWaitingCustom = ttk.Combobox(screen4,
                                        textvariable = VarStall,
                                        font=("Comic Sans MS", 15),
                                        state = "readonly",
                                        width = 10,
                                        values = listOpenStallsCustom)
        screen4.create_window(380, 600, anchor="nw", window=getWaitingCustom)

        calculateButton=Button(screen4,text='Calculate',
                    font=("Comic Sans MS", 15),
                    bg='gray22',
                    fg="white",
                    command=lambda:(showWaitingTime()))
        screen4.create_window(540, 550, anchor="nw", window=calculateButton)

        backButton4=Button(screen4,text='Back',
                    font=("Comic Sans MS", 15),
                    bg='gray22',
                    fg="white",
                    command=lambda:(frame4.destroy()))
        screen4.create_window(540, 600, anchor="nw", window=backButton4)
    except:
        return messagebox.showerror('No Stores Available',"No value selected.\nPlease choose a value.")


# Calculates waiting time based on user input of number of people
# Error Handling, ensures user input for number of people is valid            
def showWaitingTime():
    try:
        noOfPeople = VarPeople.get() #Get number of people entered in entry field
        stallChosen = VarStall.get() 
        if stallChosen == '':
            return messagebox.showerror('ERROR',"Stall not selected/no stall available. \nTry again.\n")

        swt=0 #Create variable for stall's waiting time

        for item in allStalls_dict:
            if stallChosen == item['Name']:
                swt = item['Waiting Time']
        answer = int(noOfPeople) * int(swt) 

        #Creates the frame for showing waiting time
        frame6 = Toplevel(frame2) #Pop up new frame    
        frame6.geometry("700x680")
        screen6=Canvas(frame6)
        screen6.create_image(0,0,image=wallpaper,anchor="nw")
        screen6.pack(expand="true",fill="both")
        waitingtimeLabel=Label(screen6,
                            text="Waiting Time for " + stallChosen + " will be: \n" + str(answer) + " minutes",
                            font=("Comic Sans MS", 15),
                            bg='gray22',
                            fg="white")
        waitingtimeLabel.place(relx=.5, rely=.5, anchor="center")

        destroyButton =Button(screen6,text='Back to Stall Info',
                font=("Comic Sans MS", 15),
                bg='gray22',
                fg="white",
                command=lambda:(frame6.destroy()))
        screen6.create_window(260, 550, anchor="nw", window=destroyButton)

    except:
        messagebox.showerror('Invalid number of people',"Invalid number of people entered.\nTry again.\n")

#Used with buttons, when clicked the respective frame will become active
def raise_frame(frame):
    frame.tkraise()


    


    