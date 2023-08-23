import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
import shutil
import json

class SoundManager:
    def __init__(self,parent):
        self.parentFrame = parent
        self.sound_data = self.load_sounds()

    def add_sound(self):
        newName = self.copy_audio_file()

        # Create and configure the frame
        frame = ctk.CTkFrame(master=self.parentFrame, width=300, height=50, fg_color='#1A1A1A')
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(4, weight=1)
        
        frame_label = ctk.CTkLabel(frame, text=newName, width=30)
        frame_label.grid(row=0, column=0, padx=10)

        bindButton = ctk.CTkButton(master=frame, command=self.play_sound, text='Bind', width=30, height=30)
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
        nameCapture = ctk.CTkInputDialog(text="Enter Sound Name:", title="Name your sound save")
        newName = nameCapture.get_input()

        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3 *.ogg")])

        if file_path:
            destination_folder = "sounds"
            shutil.copy(file_path, destination_folder)
            print("File copied successfully.")
        
        return newName

    def play_sound(self):
        print("Play sound functionality")

    def change_sound(self, frame):
        print("Change sound functionality")

    def delete_sound(self, frame):
        frame.destroy()

    def load_sounds(self):
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)
        return data

    def create_frames(self):
        for item in self.sound_data:
            frame = ctk.CTkFrame(master=self.parentFrame, width=300, height=50, fg_color='#1A1A1A')
            frame.grid_rowconfigure(0, weight=1)
            frame.grid_columnconfigure(4, weight=1)
                
            frame_label = ctk.CTkLabel(frame,  text=item.get('name', ''), width=30)
            frame_label.grid(row=0, column=0, padx=10)

            bindButton = ctk.CTkButton(master=frame, command=self.play_sound, text= item.get('bindID', ''), width=30, height=30)
            bindButton.grid(row=0, column=1, padx=10)

            changeButton = ctk.CTkButton(master=frame, command=lambda f=frame: self.change_sound(f), text='Change',
                                        width=25, height=30)
            changeButton.grid(row=0, column=2, padx=20)

            deleteButton = ctk.CTkButton(master=frame, command=lambda f=frame: self.delete_sound(f), text='x',
                                        width=15, height=30, fg_color='red', hover_color='#A00000')
            deleteButton.grid(row=0, column=3, padx=60)
                
            frame.pack(pady=3)
