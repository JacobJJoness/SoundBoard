import tkinter as tk
import customtkinter as ctk
from sound_manager import SoundManager

# Setting Color Mode
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Creating Window
root = ctk.CTk()
root.geometry("800x600")
root.title("DigiB-")



# GUI shapes
scrollable_frame = ctk.CTkScrollableFrame(master=root, width=300, height=400)
scrollable_frame.pack(pady=20, padx=60)

#Calling Sound_manager(Master Frame Here)
sound_manager = SoundManager(scrollable_frame)

# Title of scroll window
label = ctk.CTkLabel(master=scrollable_frame, text="Editor", font=("Copperplate Gothic Light", 24))
label.pack(pady=12, padx=10)

addButton = ctk.CTkButton(master=scrollable_frame, text="+", width=25, font=("Copperplate Gothic Light", 20),
                          command=sound_manager.add_sound)
addButton.pack(pady=10, padx=120)

# Loading and packing data from sound_manager
root.after(0, sound_manager.create_frames)

root.mainloop()






