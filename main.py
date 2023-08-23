import customtkinter as ctk
from tkinter import filedialog
import shutil
import json


#Setting Color Mode
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("theme.json")


#Creating Window
root = ctk.CTk()
root.geometry("800x600")
root.title("DigiB-")


#Globals
soundData = []

#Button Call for changing sound
def changeSound(frame):
    newName = copy_audio_file()

    # Update the label text with the new sound name
    frame_label = frame.winfo_children()[0]
    frame_label.configure(text=newName)


#Button Call for playing sound
def playSound():
    print("Test")

#Button call for deleting sound
def deleteSound():
    print("test")

#Function for copying sound file into folder
def copy_audio_file():
    # Ask the user to select an audio file
    nameCapture = ctk.CTkInputDialog(text="Enter Sound Name:", title="Name your sound save")
    newName = nameCapture.get_input()

    
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3 *.ogg")])

    if file_path:
        # Set the destination folder path where you want to copy the file
        destination_folder = "sounds"
        
        # Copy the selected file to the destination folder
        shutil.copy(file_path, destination_folder)
        print("File copied successfully.")
    
    return newName



#Import Create and load json data

def loadSounds(soundData, parent):
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)

    for item in data:
        print(f"Name: {item['name']}, bindID: {item['bindID']}, bindName: {item['bindName']}")
        frame = ctk.CTkFrame(master = parent, width=300, height=50,fg_color='#1A1A1A')
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(4, weight=1)
        frame_label = ctk.CTkLabel(frame, text=item['name'],width=30)
        frame_label.grid(row =0, column=0, padx=10)
        
        bindButton = ctk.CTkButton(master=frame, command=playSound, text=item['bindID'],width=30,height=30)
        bindButton.grid(row=0, column=1,padx=10)

        changeButton = ctk.CTkButton(master=frame, command=lambda f=frame: changeSound(f), text='Change', width=25, height=30)
        changeButton.grid(row =0, column=2, padx=20)

        deleteButton = ctk.CTkButton(master = frame, command=deleteSound,text='x',width=15,height=30,fg_color='red',hover_color='#A00000')
        deleteButton.grid(row = 0, column = 3,padx=60, )
        
        soundData.append(frame)


#GUI shapes
scrollable_frame = ctk.CTkScrollableFrame(master = root, width=300, height=400)
scrollable_frame.pack(pady=20,padx=60)

#Title of scroll window
label = ctk.CTkLabel(master=scrollable_frame, text="Editor", font=("Copperplate Gothic Light",24))
label.pack(pady=12, padx=10)

addButton = ctk.CTkButton(master = scrollable_frame, text="+",width=25,font=("Copperplate Gothic Light",20))
addButton.pack(pady=10,padx=120)

#loading and packing data from soundData folder
loadSounds(soundData, scrollable_frame)
for item in soundData:
    item.pack(pady=3)



root.mainloop()