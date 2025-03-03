import tkinter as tk
import customtkinter as ctk
from sound_manager import SoundManager

# Setting Color Mode: The color scheme of the application
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Creating Window
rootWindow = ctk.CTk()
rootWindow.geometry("450x500")
rootWindow.title("DigiB-")



#Main Frame of application currently.
scrollable_frame = ctk.CTkScrollableFrame(master=rootWindow, width=300, height=400)
scrollable_frame.pack(pady=20, padx=60)

#Sound data declared and given a frame and the rootWindow of the app.
sound_manager = SoundManager(scrollable_frame,rootWindow)

# Title of scroll window
label = ctk.CTkLabel(master=scrollable_frame, text="Editor", font=("Cascadia Code SemiBold", 24))
label.pack(pady=12, padx=10)

addButton = ctk.CTkButton(master=scrollable_frame, text="Add Sound", width=200, font=("Cascadia Code SemiBold", 17),
                          command=sound_manager.add_sound)
addButton.pack(pady=10)

# Loading and packing data from sound_manager
rootWindow.after(0, sound_manager.create_frames)

rootWindow.mainloop()






