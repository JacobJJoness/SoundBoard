from soundBoard import*


def createNote(event):
    print("This should not be printing")
    test = Label( text="Press the key that you want to bind", font =( "Heleveltica", 15))
    test.pack()

# Main Window GUI
def soundGUI():
    window = Tk()
    window.title("SoundBoard")
    window.geometry("1000x600")
    #this line might be the key to having a "generalized keybind" inside and outside of the program
    window.bind("<Key>",aNote)
    #window.configure(bg="black")
  #The following line overrides the screen and does an odd sort of takeover  
    #window.overrideredirect(1)
    #window.wm_attributes('-fullscreen', 'True')
    #window.attributes('-type', 'dock')

    #remove title bar
    window.overrideredirect(1)

    def move_app(e):
        window.geometry(f'+{e.x_root}+{e.y_root}')

    # Creating the fake title bar
    title_bar = Frame(window, bg="darkgreen", relief="raised", bd=0)
    title_bar.pack(expand=1, fill=X)

    title_label = Label(title_bar, text="My Awesome App!!", bg="darkGreen", fg="white")
    title_label.pack(side=LEFT, pady=0)


    # Bind the title bar
    title_bar.bind("<B1-Motion>", move_app)



    # Title bar buttons
    my_button = Button(window, text="X", font=("Helvetica, 32"), command=window.quit)
    my_button.pack(pady=100)


    
    label = Label(window,text="Sound Files must be .wav format.",font=("Helvetica",35))
    label.configure(bg='gray')
    label.pack()


    


#------Buttons for changing the sound-------------------
    OneButton = Button(window, text="Change Sound One")
    OneButton.configure(bg='gray')
    OneButton.bind('<Button-1>',soundOne)
    OneButton.pack()
    TwoButton = Button(window, text="Change Sound Two")
    TwoButton.configure(bg='gray')
    TwoButton.bind('<Button-1>',soundTwo)
    TwoButton.pack()
    ThreeButton = Button(window, text="Change Sound Three")
    ThreeButton.configure(bg='gray')
    ThreeButton.bind('<Button-1>',soundThree)
    ThreeButton.pack()
    FourButton = Button(window, text="Change Sound Four")
    FourButton.configure(bg='gray')
    FourButton.bind('<Button-1>',soundFour)
    FourButton.pack()
    FiveButton = Button(window, text="Change Sound Five")
    FiveButton.configure(bg='gray')
    FiveButton.bind('<Button-1>',soundFour)
    FiveButton.pack()

    #----button-for new keybind-----in progress
    #
    newBindButton = Button(window, text = "New Sound Bind")
    newBindButton.bind('<Button-1>', createNote(window))
    newBindButton.pack()

    #----button for deleting binds----unfinished
    #deleteBind = Button(window, text = "Delete Sound Bind")

    
    window.mainloop()