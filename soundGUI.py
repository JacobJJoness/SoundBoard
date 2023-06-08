from soundBoard import*


def createNote(event):
    test = Label( text="Press the key that you want to bind", font =( "Heleveltica", 15))
    test.pack()
    key= ""
    keyTracker = Tk()
    keyTracker.bind("<Key>", keyPressed)


# Main Window GUI
def soundGUI():
    window = Tk()
    window.title("SoundBoard")
    #window.geometry("500x300+200+200")
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
    
    def quitter(e):
        window.quit()
        #root.destroy()

# Creating the fake title bar
    title_bar = Frame(window, bg="darkGrey", relief="raised", bd=0)
    title_bar.pack(expand=1, fill=X)

    title_label = Label(title_bar, text="Soundboard", bg="darkGrey", fg="white")
    title_label.pack(side=LEFT, pady=0)

# Title bar buttons
    close_label = Button(title_bar, text="X", font=("Helvetica, 10"), command=window.quit, fg="white",bg="red", relief="sunken", bd=0,height= 1, width=5)
    close_label.pack(side=RIGHT, pady=1)
    close_label.bind("<B1-Motion>", quitter)

# Bind the title bar
    title_bar.bind("<B1-Motion>", move_app)



    

    label = Label(window,text="Sound Files must be .wav format.",font=("Helvetica",35))
    label.configure(bg='gray')
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