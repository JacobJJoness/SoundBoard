from tkinter import * 
from tkinter import filedialog
import pygame
from soundBoard import *

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.mixer.init()



## Function to change the preloaded sounds

def changeSound(num):
    File = open("SoundPaths.txt","r")
    contents = File.readlines()
    temp_Win = Tk()
    temp_Win.withdraw()
    dirname = filedialog.askopenfilename(parent = temp_Win,initialdir = "/",title = 'Please select a file')
    if dirname != "":
        File=open("SoundPaths.txt","w")
        contents[num]= dirname +"\n"
        File.writelines(contents)
        File.close()
        print(dirname)
        temp_Win.destroy()
    return

# Function to return what key was pressed
def keyPressed(event):
    return event.char
##Functions to determine which value to change
def soundOne(event):
    changeSound(0)

def soundTwo(event):
    changeSound(1)

def soundThree(event):
    changeSound(2)

def soundFour(event):
    changeSound(3)

def soundFive(event):
    changeSound(4)


    
    #keyPrompt = Label(tempWin, text = "Press the Key for the new sound")
    

#This function handles the "playing" of notes.
# Function pulling the sounds from SoundPaths.txt and Binding the Sound to a specified key
# and playing the sound at the given path from SoundPaths.txt
def aNote(event):
    
    pathFile = open("SoundPaths.txt")
    content = pathFile.readlines()
    pathFile.close()
    
    if (event.keysym == 'End'):
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

    elif (event.keysym == 'Down'):
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

    elif (event.keysym == 'Next'):
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
   