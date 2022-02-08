from soundBoard import*

class MainWindow:

    def __init__(self):
        # Main Window GUI
        self.window = Tk()
        self.window.title("SoundBoard")
        self.window.geometry("1400x700")
        #this line might be the key to having a "generalized keybind" inside and outside of the program
        self.window.bind("<Key>",aNote)
        self.window.configure(bg="black")
        #The following line overrides the screen and does an odd sort of takeover  
        #window.overrideredirect(1)
        #------Buttons for changing the sound-------------------
   

        #----button-for new keybind-----in progress
        #
        newBindButton = Button(self.window, text = "New Sound Bind")
        newBindButton.bind('<Button-1>', MainWindow.createNote)
        newBindButton.pack()

        #----button for deleting binds----unfinished
        #deleteBind = Button(window, text = "Delete Sound Bind")
        self.label = Label(self.window,text="Sound Files must be .wav format.",font=("Helvetica",35))
        self.label.pack()
        self.window.mainloop()

    


    def createNote(self,event):
        test = Label( text="Press the key that you want to bind", font =( "Heleveltica", 15))
        test.pack()
        keyTracker = Tk()
        keyTracker.bind("<Key>", keyPressed)



if __name__ == "__main__":
    display = MainWindow()