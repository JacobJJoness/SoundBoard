from tkinter import * 
import tkinter as tk
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
        temp_Win.destroy()
    return
    
    





    
    #keyPrompt = Label(tempWin, text = "Press the Key for the new sound")
    

#This function handles the "playing" of notes.
# Function pulling the sounds from SoundPaths.txt and Binding the Sound to a specified key
# and playing the sound at the given path from SoundPaths.txt
def aNote(event):
    with open("SoundPaths.txt", 'r') as f: 
        for line in f: 
            #this splits the line string into an array of words.
            try:
                
                word_array = line.split()
                if(word_array[0] == event.keysym):
                    
                    sound = pygame.mixer.Sound(word_array[1:])
                    sound.play()
                    print("Playing sound " + event.keysym)
            except:
                pass
     