from tkinter import * 
from tkinter import filedialog
import pygame
from soundBoard import *

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.mixer.init()

# Function pulling the sounds from SoundPaths.txt and Binding the Sound to a specified key
# and playing the sound at the given path from SoundPaths.txt
def aNote(event):
    
    pathFile = open("SoundPaths.txt")
    content = pathFile.readlines()
    pathFile.close()
    
    if (event.keysym == 'Home'):
        Stringy = content[0]
        length = len(Stringy)
        if(Stringy[length-2:length-1] == "v"):
            sound = pygame.mixer.Sound(Stringy[:length-1])
            sound.play()
            return
        else:
            sound = pygame.mixer.Sound(Stringy)
            sound.play()
            return

    elif (event.keysym == 'Up'):
        Stringy = content[1]
        length = len(Stringy)
        if(Stringy[length-2:length-1] == "v"):
            sound = pygame.mixer.Sound(Stringy[:length-1])
            sound.play()
            return
        else:
            sound = pygame.mixer.Sound(Stringy)
            sound.play()
            return

    elif (event.keysym == 'Prior'):
        Stringy = content[2]
        length = len(Stringy)
        if(Stringy[length-2:length-1] == "v"):
            sound = pygame.mixer.Sound(Stringy[:length-1])
            sound.play()
            return
        else:
            sound = pygame.mixer.Sound(Stringy)
            sound.play()
            return

    elif (event.keysym == 'Left'):
        Stringy = content[3]
        length = len(Stringy)
        if(Stringy[length-2:length-1] == "v"):
            sound = pygame.mixer.Sound(Stringy[:length-1])
            sound.play()
            return
        else:
            sound = pygame.mixer.Sound(Stringy)
            sound.play()
            return

    elif (event.keysym == 'Clear'):
        Stringy = content[4]
        length = len(Stringy)
        if(Stringy[length-2:length-1] == "v"):
            sound = pygame.mixer.Sound(Stringy[:length-1])
            sound.play()
            return
        else:
            sound = pygame.mixer.Sound(Stringy)
            sound.play()
            return

    elif (event.keysym == 'Right'):
        Stringy = content[5]
        length = len(Stringy)
        if(Stringy[length-2:length-1] == "v"):
            sound = pygame.mixer.Sound(Stringy[:length-1])
            sound.play()
            return
        else:
            sound = pygame.mixer.Sound(Stringy)
            sound.play()
            return
   

## Function to change the preloaded sounds
def key_Checker(event):
    pass
def changeSound(event):
    File = open("SoundPaths.txt","r")
    contents = File.readlines()
    temp_Win = Tk()
    label = Label(temp_Win,text="Press the key to rebind.",font=("Helvetica",20))
    label.pack()
    temp_Win.bind("<Key>")
    temp_Win.withdraw()
    dirname = filedialog.askdirectory(parent = temp_Win,initialdir = "/",title = 'Please select a directory')
    #File=open("SoundPaths.txt","w")
    #contents[selectedNum]= dirname
    #File.writelines(contents)
    #File.close()
    print(dirname)
    temp_Win.destroy()
    
# Main Window GUI
def soundGUI():
    window = Tk()
    window.title("SoundBoard")
    window.geometry("1400x700")
    window.bind("<Key>",aNote)


    label = Label(window,text="Sound Files must be .wav format.",font=("Helvetica",35))
    label.pack()

    myButton = Button(window, text="Load New Sounds")
    myButton.bind('<Button-1>',changeSound)
    myButton.pack()
    window.mainloop()