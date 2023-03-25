import tkinter 
from tkinter import *
def encryption():
    exec(open('user_interface.py').read())

window = tkinter.Tk()
window.geometry("1000x700")
window.config(bg="black")
window.title("S2DG-CIPHERS")
frame = Frame(window, bg="black")
frame.pack()
background_image = tkinter.PhotoImage(file="S2DG-CIPHERS.png")
background_label = tkinter.Label(frame, image=background_image)
background_label.pack()
button = tkinter.Button(frame, text="ENCRYPTION", bg="white", command=encryption)
button.pack(side="left")
button = tkinter.Button(frame, text="DECRYPTION", bg="white", command= encryption)
button.pack(side="right")
window.mainloop()
