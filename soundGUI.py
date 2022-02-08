from soundBoard import*


def createNote(event):
    test = Label( text="Press the key that you want to bind", font =( "Heleveltica", 15))
    test.pack()
    keyTracker = Tk()
    keyTracker.bind("<Key>", keyPressed)
    


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
    label.pack()


#------Buttons for changing the sound-------------------
   

    #----button-for new keybind-----in progress
    #
    newBindButton = Button(window, text = "New Sound Bind")
    newBindButton.bind('<Button-1>', createNote)
    newBindButton.pack()

    #----button for deleting binds----unfinished
    #deleteBind = Button(window, text = "Delete Sound Bind")

    
    window.mainloop()