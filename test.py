#Import the required Libraries
from tkinter import *
from tkinter import ttk
#Create an instance of Tkinter frame
win = Tk()
#Set the geometry of the Tkinter frame
win.geometry("750x250")

#Define a function to update the entry widget
def entry_update(text):
   entry.delete(0,END)
   entry.insert(0,text)

#Create an Entry Widget
entry= Entry(win, width= 30, bg= "white")
entry.pack(pady=10)

#Create Multiple Buttons with different commands
button_dict={}
option= ["Python", "Java", "Go", "C++"]

for i in option:
   def func(x=i):
        
        return entry_update(x)

   button_dict[i]=ttk.Button(win, text=i, command= func)
   button_dict[i].pack()

win.mainloop()