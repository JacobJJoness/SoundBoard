import customtkinter
import json


#Setting Color Mode
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#Creating Window
root = customtkinter.CTk()
root.geometry("800x600")

#Import Create and load json data
soundData = []
def loadSounds(soundData):
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)

    for item in data:
        print(f"Name: {item['name']}, bindID: {item['bindID']}, bindName: {item['bindName']}")
        soundData.append(customtkinter.CTkFrame( master = scrollable_frame, width=300, height=50 ))
loadSounds()
#Button Call for changing sound
def changeSound():
    print("test")

#Button call for deleting sound
def deleteSound():
    print("test")

#GUI shapes
scrollable_frame = customtkinter.CTkScrollableFrame(master = root, width=300, height=200)
scrollable_frame.pack(pady=20,padx=60)

label = customtkinter.CTkLabel(master=scrollable_frame, text="Editor", font=("Copperplate Gothic Light",24))
label.pack(pady=12, padx=10)



root.mainloop()