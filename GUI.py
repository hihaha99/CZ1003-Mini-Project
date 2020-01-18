from Backend import * #Import Backend module
import Backend
#Clock Function - added here for time to update real-time

############### Screen 1 : Welcome Screen ###############
screen1 = Canvas(frame1)
screen1.create_image(0, 0, image=wallpaper, anchor="nw")
screen1.pack(expand="true",fill="both")
clockLabel=Label(frame1,fg="white",bg='grey22')
Backend.clockLabel=clockLabel
screen1.create_window(145, 120, anchor="nw", window=clockLabel)

clock()
introText1 = "Welcome to North Spine Canteen Information System!"
introLabel=Label(screen1, text = introText1, font=("Comic Sans MS", 15), bg="grey22", fg="white")
screen1.create_window(100, 5, anchor="nw", window=introLabel)

CurrentStallsButton=Button(screen1,
                        text="Check Current Stalls",
                        command=lambda:raise_frame(frame3),
                        height = 1,
                        bg="grey22",
                        fg="white",
                        font=("Comic Sans MS", 15))
screen1.create_window(245, 220, anchor="nw", window=CurrentStallsButton)


CustomStallsButton=Button(screen1,
                        text="Check stalls by Custom Date/Time",
                        command=lambda: raise_frame(frame2),
                        height = 1,
                        bg="grey22",
                        fg="white",
                        font=("Comic Sans MS", 15))
screen1.create_window(185, 310, anchor="nw", window=CustomStallsButton)

OperatingHoursButton=Button(screen1,
                    text="Check Operating Hours of Stalls",
                    command=lambda: raise_frame(frame5),
                    height = 1,
                    bg="grey22",
                    fg="white",
                    font=("Comic Sans MS", 15))
screen1.create_window(192, 400, anchor="nw", window=OperatingHoursButton)

############### Screen 2: Choose Custom Date/Time ###############
introText2 = Label(frame2,
                    font=("Comic Sans MS", 15),
                    bg='gray22',
                    height=1,
                    fg="white",
                    text="Please enter desired date and time:")
introText2.grid(row = 0, column = 0, columnspan = 4, pady = 10, sticky = "we")

calendar.grid(row = 1, column = 0, columnspan = 4, sticky = "we")

Label(frame2,
    text="Select Hour (0-23):",
    bg='gray22',
    font=("Comic Sans MS", 15),
    fg = "white").grid(row=2,column=1, pady =20)
ttk.Combobox(frame2,
            textvariable = VarH,
            font=("Comic Sans MS", 15),
            state = "readonly",
            width = 10,
            values = timeListHours).grid(row=2,column=2,pady =20)
Label(frame2,
    text="Select Minute (0-59):",
    bg='gray22',
    font=("Comic Sans MS", 15),
    fg = "white").grid(row=3,column=1, pady = 20)                               
ttk.Combobox(frame2,
            textvariable = VarM,
            font=("Comic Sans MS", 15),
            state = "readonly",
            width = 10,
            values = timeListMinutes).grid(row=3,column=2,pady =20)

selectButton = Button(frame2,
            text="Select",
            bg='gray22',
            fg = "white",
            font=("Comic Sans MS", 15),
            command=lambda:(showStallsCustom())) #Screen 4: Stalls with Custom Timing is created here
selectButton.grid(row=5, column = 1, padx = 5, sticky = "e")
backButton2 = Button(frame2,
            text="Back",
            bg='gray22',
            fg = "white",
            font=("Comic Sans MS", 15),
            command=lambda:(raise_frame(frame1)))
backButton2.grid(row=5, column = 2, padx = 5, sticky  ="w")

############### Screen 3: Stalls with Current Timing ###############
screen3 = Canvas(frame3)
screen3.create_image(0, 0, image=wallpaper, anchor="nw")
screen3.pack(expand="true", fill="both")

intro2Label=Label(screen3,
                font=("Comic Sans MS", 15),
                bg='gray22',
                height=1,
                fg="white",
                text="Current Stalls and Food Available:")
intro2_label = screen3.create_window(190, 120, anchor="nw", window=intro2Label)

listOpenStallsCurrent = getCurrentStalls()[1]

if listOpenStallsCurrent == []: #If no stalls open, inform user
    Label_nostall=Label(screen3,
                text="No stalls currently open, \nplease choose custom \ndate/time instead.",
                font=("Comic Sans MS", 15),
                bg='gray22',
                fg="white")
    Label_nostall.place(relx=.5, rely=.5, anchor="center")

    backButton3_nostall=Button(screen3,text='Back',
            font=("Comic Sans MS", 15),
            bg='gray22',
            fg="white",
            command=lambda:(raise_frame(frame1)))
    screen3.create_window(540, 600, anchor="nw", window=backButton3_nostall)

else:
    menuInfoCurrent="\n".join(getCurrentStalls()[0]) #Use getCurrentStalls() function and print out the menu details
    menuTextCurrent = tkst.ScrolledText(screen3,
                    font=("Comic Sans MS", 15),
                    bg='gray22',
                    fg="white",
                    wrap ="word",
                    width = 35,
                    height = 13)
    menuTextCurrent.pack(fill="both",expand="true",padx = 8, pady = 8)
    menuTextCurrent.tag_config("justified", justify = "center")
    menuTextCurrent.insert("insert", menuInfoCurrent, "justified")
    menuTextCurrent.config(state="disabled")
    screen3.create_window(130, 160, anchor="nw", window=menuTextCurrent)

    Label_3A=Label(screen3,
                text=" Enter number of people waiting: ",
                font=("Comic Sans MS", 15),
                bg='gray22',
                fg="white")
    screen3.create_window(50, 550, anchor="nw", window=Label_3A)

    getPeopleCurrent = Entry(screen3, font = ("Comic Sans MS", 15), width = 5, textvariable = VarPeople)
    screen3.create_window(380, 550, anchor="nw", window=getPeopleCurrent)

    Label_3B=Label(screen3,
                text="Choose stall: ",
                font=("Comic Sans MS", 15),
                bg='gray22',
                fg="white")
    screen3.create_window(50, 600, anchor="nw", window=Label_3B)

    getWaitingCurrent = ttk.Combobox(screen3,
                                    textvariable = VarStall,
                                    font=("Comic Sans MS", 15),
                                    state = "readonly",
                                    width = 10,
                                    values = listOpenStallsCurrent)
    screen3.create_window(380, 600, anchor="nw", window=getWaitingCurrent)

    calculateButton =Button(screen3,text='Calculate',
                    font=("Comic Sans MS", 15),
                    bg='gray22',
                    fg="white",
                    command=lambda:(showWaitingTime()))
    screen3.create_window(540, 550, anchor="nw", window=calculateButton)

    backButton3=Button(screen3,text='Back',
            font=("Comic Sans MS", 15),
            bg='gray22',
            fg="white",
            command=lambda:(raise_frame(frame1)))
    screen3.create_window(540, 600, anchor="nw", window=backButton3)

################ Frame 5: Operating Hours of Stalls ###############
screen5=Canvas(frame5)
screen5.create_image(0,0,image=wallpaper,anchor="nw")
screen5.pack(expand="true", fill="both")

OpHrs = []
for stall in allStalls_dict: #Adds all stalls and operating hours to list
    OpHrs.append(stall["Name"] + " : " + str(stall["Operating Hours"][0]) + " to " + str(stall["Operating Hours"][1]))

intro5Label=Label(screen5,
                  font=("Comic Sans MS", 15),
                  bg='gray22',
                  height=1,
                  fg="white",
                  text="Operating Hours:")
screen5.create_window(275, 5, anchor="nw", window=intro5Label)

OpsHrsInfo="\n".join(OpHrs)
opsHrsLabel=Label(screen5,
                text = OpsHrsInfo,
                font=("Comic Sans MS", 15),
                bg='gray22',
                fg="white")
screen5.create_window(110, 200, anchor="nw", window=opsHrsLabel)

backButton5=Button(screen5,text='Back',
        font=("Comic Sans MS", 15),
        bg='gray22',
        fg="white",
        command=lambda:(raise_frame(frame1)))
screen5.create_window(320, 525, anchor="nw", window=backButton5)

#Set Welcome Screen as first Screen, initialise Clock
raise_frame(frame1)


shell.configure()
shell.mainloop()