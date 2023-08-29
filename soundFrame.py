import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
import shutil
import json

class soundFrame:
    def __init__(self,parent,newPath,newBindKey,newBindName):
        self.parentFrame = parent
        self.path = newPath
        self.bindKey = newBindKey
        self.bindName = newBindName
        self.itemFrame = ctk.CTkFrame(master=self.parentFrame, width=300, height=50, fg_color='#1A1A1A')

    def add_sound(self):
        nameCapture = ctk.CTkInputDialog(text="Enter Sound Name:", title="Name your sound save")
        self.bindName = nameCapture.get_input()

        keyBinder = ctk.CTkInputDialog(text="Enter a Key to bind to:", title="Name your sound save")
        self.bindKey = keyBinder.get_input()

        self.copy_audio_file()


        # Create and configure the frame
        frame = ctk.CTkFrame(master=self.parentFrame, width=300, height=50, fg_color='#1A1A1A')
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(4, weight=1)
        
        frame_label = ctk.CTkLabel(frame, text=self.bindName, width=30)
        frame_label.grid(row=0, column=0, padx=10)

        bindButton = ctk.CTkButton(master=frame, command=self.play_sound, text=self.bindKey, width=30, height=30)
        bindButton.grid(row=0, column=1, padx=10)

        changeButton = ctk.CTkButton(master=frame, command=lambda f=frame: self.change_sound(f), text='Change',
                                     width=25, height=30)
        changeButton.grid(row=0, column=2, padx=20)

        deleteButton = ctk.CTkButton(master=frame, command=lambda f=frame: self.delete_sound(f), text='x',
                                     width=15, height=30, fg_color='red', hover_color='#A00000')
        deleteButton.grid(row=0, column=3, padx=60)
        
        self.sound_data.append(frame)
        frame.pack(pady=3)

    def copy_audio_file(self):
        # Ask the user to select an audio file
        

        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3 *.ogg")])

        if file_path:
            destination_folder = "sounds"
            shutil.copy(file_path, destination_folder)
            print("File copied successfully.")
        
        

    def play_sound(self):
        print("Play sound functionality")

    def change_sound(self, frame):
        print("Change sound functionality")

    def delete_sound(self):
        self.itemFrame.destroy()

    def load_sounds(self):
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)
        return data

    def create_frame(self):
            
            self.itemFrame.grid_rowconfigure(0, weight=1)
            self.itemFrame.grid_columnconfigure(4, weight=1)
                
            frame_label = ctk.CTkLabel(self.itemFrame,  text=item.get('name', ''), width=30)
            frame_label.grid(row=0, column=0, padx=10)

            bindButton = ctk.CTkButton(master=self.itemFrame, command=self.play_sound, text= item.get('bindKey', ''), width=30, height=30)
            bindButton.grid(row=0, column=1, padx=10)

            changeButton = ctk.CTkButton(master=self.itemFrame, command=lambda f=frame: self.change_sound(f), text='Change',
                                        width=25, height=30)
            changeButton.grid(row=0, column=2, padx=20)

            deleteButton = ctk.CTkButton(master=self.itemFrame, command=delete_sound, text='x',
                                        width=15, height=30, fg_color='red', hover_color='#A00000')
            deleteButton.grid(row=0, column=3, padx=60)
                
            frame.pack(pady=3)
