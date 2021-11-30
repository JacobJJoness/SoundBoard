from soundBoard import*





# Main Window GUI
def soundGUI():
    window = Tk()
    window.title("SoundBoard")
    window.geometry("1400x700")
    window.bind("<Key>",aNote)
    window.configure(bg="black")
  #The following line overrides the screen and does an odd sort of takeover  
    #window.overrideredirect(1)

    print("Testing")
    label = Label(window,text="Sound Files must be .wav format.",font=("Helvetica",35))
    label.pack()

#------Buttons for changing the sound-------------------
    OneButton = Button(window, text="Change Sound One")
    OneButton.bind('<Button-1>',soundOne)
    OneButton.pack()
    TwoButton = Button(window, text="Change Sound Two")
    TwoButton.bind('<Button-1>',soundTwo)
    TwoButton.pack()
    ThreeButton = Button(window, text="Change Sound Three")
    ThreeButton.bind('<Button-1>',soundThree)
    ThreeButton.pack()
    FourButton = Button(window, text="Change Sound Four")
    FourButton.bind('<Button-1>',soundFour)
    FourButton.pack()
    FiveButton = Button(window, text="Change Sound Five")
    FiveButton.bind('<Button-1>',soundFour)
    FiveButton.pack()

    
    window.mainloop()