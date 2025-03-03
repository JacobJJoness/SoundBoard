import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
import shutil
import json
import os
import pygame
import threading

class SoundManager:
    def __init__(self,parent,root):
        self.parentFrame = parent
        self.sound_data = self.load_sounds()
        self.appRoot = root
        pygame.mixer.init()
        self.key_to_sound = {}  # Dictionary to map keys to corresponding sound paths
        self.init_key_listeners()  # Initialize key listeners
        self.appRoot.bind("<Key>", self.key_pressed)  # Bind key event
    
    def init_key_listeners(self):
        for user_sound_input in self.sound_data:
            bind_key = user_sound_input.get("bindKey")
            sound_path = user_sound_input.get("path")
            if bind_key and sound_path:
                sound = pygame.mixer.Sound(sound_path)
                self.key_to_sound[bind_key] = sound

    def key_pressed(self, event):
        print("entered")
        key = event.char  # Get the pressed key
        self.play_sound(key)

    def add_sound(self):
        #Getting User Input
        #---could be split into its own function
        nameCapture = ctk.CTkInputDialog(text="Enter Sound Name:", title="Name your sound save")
        newName = nameCapture.get_input()

        keyBinder = ctk.CTkInputDialog(text="Enter a Key to bind to:", title="Name your sound save")
        newBind = keyBinder.get_input()

        copiedFilePath = self.copy_audio_file()

        #Updating the sound_data list and JSON
        #---could be split into its own function
        user_sound_input = {
            "name": newName,
            "bindKey": newBind,
            "path": copiedFilePath
        }
       
           
        self.sound_data.append(user_sound_input)  # Append sound info to sound_data list

        # Save updated sound_data to JSON file
        self.save_sounds()
        # Create the new frame
        self.create_frame(newName,newBind,copiedFilePath)
        
        self.init_key_listeners()  # Reinitialize key listeners

        #Refreshing app to account for data changes.
        self.appRoot.update()
        



    def copy_audio_file(self):
        # Ask the user to select an audio file
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3 *.ogg")])

        if file_path:
            destination_folder = "sounds"
            shutil.copy(file_path, destination_folder)
            print("File copied successfully.")
         # Construct the path where the file is being saved
            saved_file_name = os.path.basename(file_path)
            saved_file_path = os.path.join(destination_folder, saved_file_name)

            return saved_file_path
    
        
        

    def play_sound(self, key):
        if key in self.key_to_sound:
            sound = self.key_to_sound[key]
            sound.play()

    def button_play_sound(self, frame):
        def play_thread():
            sound = self.key_to_sound[frame.id]
            sound.play()

        play_thread = threading.Thread(target=play_thread)
        play_thread.start()
   

    def delete_sound(self, frame):
        # Find the bind key associated with the frame
        frameID = frame.id
        
        if frameID is not None:
            # Remove the corresponding dictionary from sound_data
            self.sound_data = [item for item in self.sound_data if item.get('bindKey') != frameID]
        
        # Remove the frame from the UI
        frame.destroy()
        
        # Update the JSON file after deleting
        self.save_sounds()
      
        del self.key_to_sound[frameID]  # Remove key binding

        self.init_key_listeners()  # Reinitialize key listeners

        #Refreshing app to account for data changes.
        self.appRoot.update()

    def save_sounds(self):
        with open('data.json', 'w') as json_file:
            json.dump(self.sound_data, json_file, indent=4)

    def load_sounds(self):
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)
        return data

    def create_frame(self,name, bind, filePath):
        # Create and configure the frame
        frame = ctk.CTkFrame(master=self.parentFrame, width=300, height=50, fg_color='#1A1A1A')
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        frame.grid_columnconfigure(3, weight=1)
        #Frame Variables

        #creating a unique ID based on the item bindKey allowing for a frame to trace back to its data source.
        frame.id = bind

        #Frame Path
        frame.path = filePath


        frame_label = ctk.CTkLabel(frame, text=name, width=90)
        frame_label.grid(row=0, column=0, padx=10)

        bindButton = ctk.CTkButton(master=frame, command=lambda f=frame: self.button_play_sound(f), text=bind, width=50, height=20)
        bindButton.grid(row=0, column=1, padx=20)

        

        deleteButton = ctk.CTkButton(master=frame, command=lambda f=frame: self.delete_sound(f), text='x',
                                     width=30, height=20, fg_color='red', hover_color='#A00000')
        deleteButton.grid(row=0, column=3,padx=20)
        
        frame.pack(pady=3)

    def create_frames(self):
        for item in self.sound_data:
           self.create_frame(item.get('name', ''),item.get('bindKey', ''),item.get('path', ''))