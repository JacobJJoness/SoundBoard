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
        temp_Win.destroy()
    return
    
    

# Function to return what key was pressed
def keyPressed(event,tracker):
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
                    temp_Win.destroy()
                    tracker = True
                    return
    f.close()
    File = open("SoundPaths.txt","a")
    dirname = filedialog.askopenfilename(parent = temp_Win,initialdir = "/",title = 'Please select a file')
    if dirname != "":
        File.write(event.keysym + " " + dirname+ "\n")
        File.close()
        tracker = True
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
                    print("Playing sound " + event.keysym)
                    sound = pygame.mixer.Sound(word_array[1])
                    sound.play()
            except:
                pass
     