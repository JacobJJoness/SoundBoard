from tkinter import * 
import tkinter as tk
from tkinter import filedialog
import pygame
from soundBoard import *

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.mixer.init()

class MainWindow:


    def __init__(self):
        # Main Window GUI
        self.window = Tk()
        self.window.title("SoundBoard")
        self.window.geometry("1400x700")
        #this line might be the key to having a "generalized keybind" inside and outside of the program
        self.window.bind("<Key>",self.aNote)
        self.window.configure(bg="black")
        #The following line overrides the screen and does an odd sort of takeover  
        #window.overrideredirect(1)
        self.varCheck = tk.IntVar(self.window,value = 0)
        
        #------Buttons for changing the sound-------------------
   

        #----button-for new keybind-----in progress
        #
        newBindButton = Button(self.window, text = "New Sound Bind")
        newBindButton.bind('<Button-1>', self.createNote)
        newBindButton.pack()

        #----button for deleting binds----unfinished
        #deleteBind = Button(window, text = "Delete Sound Bind")
        self.label = Label(self.window,text="Sound Files must be .wav format.",font=("Helvetica",35))
        self.label.pack()
        self.window.mainloop()

    


    def createNote(self,event):
        test = Label( self.window, text="Press the key that you want to bind", font =( "Heleveltica", 15))
        test.pack()
        keyTracker = Tk()
        keyTracker.bind("<Key>", self.keyPressed)
        #keyTracker.wait_variable(self.varCheck)
        #test.destroy()
        #keyTracker.destroy()



        # Function to return what key was pressed
    def keyPressed(self,event):
        temp_Win = Tk()
        temp_Win.withdraw()
        with open("SoundPaths.txt", 'r') as f: 
            for line in f: 
                #this splits the line string into an array of words.
                word_array = line.split()
                if(word_array[0] == event.keysym):
                    dirname = filedialog.askopenfilename(parent = temp_Win,initialdir = "/",title = 'Please select a file')
                    #The preceding line is acting as the file type checker.
                    if dirname != "" or dirname[len(dirname)-4:] == ".wav":
                        File=open("SoundPaths.txt","w")
                        File.write(word_array[0] + " " + dirname + "\n")
                        File.close()
                        #self.varCheck.set(value=1)
                        temp_Win.destroy()
                        return
        f.close()
        File = open("SoundPaths.txt","a")
        dirname = filedialog.askopenfilename(parent = temp_Win,initialdir = "/",title = 'Please select a file')
        if dirname != "":
            File.write(event.keysym + " " + dirname+ "\n")
            File.close()
            #self.varCheck.set(value =1)
        temp_Win.destroy()
        return

    def aNote(self, event):
        with open("SoundPaths.txt", 'r') as f: 
            for line in f: 
                #this splits the line string into an array of words.
                try:
                    if(line[0] == event.keysym):
                        print(line[2:])
                        sound = pygame.mixer.Sound(line[2:len(line)-1])
                        sound.play()
                        print("Playing sound " + event.keysym)
                except:
                    pass
        



if __name__ == "__main__":
    display = MainWindow()