#Christians
from soundBoard import*


def createNote(event):
    print("This should not be printing")
    test = Label( text="Press the key that you want to bind", font =( "Heleveltica", 15))
    test.pack()

# Main Window GUI
def soundGUI():
    window = Tk()
    window.title("SoundBoard")
    window.geometry("1400x700")
    #this line might be the key to having a "generalized keybind" inside and outside of the program
    window.bind("<Key>",aNote)
    window.configure(bg="black")
  #The following line overrides the screen and does an odd sort of takeover  
    #window.overrideredirect(1)


    
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
    newBindButton.bind('<Button-1>', createNote)
    newBindButton.pack()

    #----button for deleting binds----unfinished
    #deleteBind = Button(window, text = "Delete Sound Bind")

    
    window.mainloop()