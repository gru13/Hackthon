import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from Encryption import *

# Create a Tkinter window


root = tk.Tk()

background = Image.open("bg.png")
background = background.resize((1440,720))
background = ImageTk.PhotoImage(background)

tk.Label(root,image=background).place(x=0,y=0,relwidth=1,relheight=1)#background image

root.geometry("1440x720")
root.title("Encryption")
root.maxsize(height=720,width=1440)
root.minsize(height=720,width=1440)
file_path = None
canvas = None
canvas = tk.Canvas(root, width=1100, height=500)
canvas.pack()


def handle_number():
    global number_entry
    global submit_button
    global root
    global fr
    number = int(number_entry.get())
    number_entry.destroy()
    submit_button.destroy()
    fr.destroy()

    Exit = tk.Button(root,text="exit",command=lambda:root.destroy())
    Exit.pack()
    if(number>1000):
        number = str(number)
        pa = int(number[0:2])
        pb = int(number[2:4])
    else:
        pa = 13
        pb = 17
    enc_file  = Encryption(file_path,pa,pb)
    resultImage = Image.open(enc_file)
    resultImage = resultImage.resize((500, 500))
    tk_image1 = ImageTk.PhotoImage(resultImage)
    canvas.create_image(600,0,anchor=tk.NW,image=tk_image1)
    canvas.image1 = tk_image1




# Create a function to open a file dialog and select an image
def open_image():
    global file_path
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)
    image = image.resize((500, 500))
    tk_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
    canvas.image = tk_image 
    button.destroy()


button = tk.Button(root, text="Select Image", command=open_image)
button.pack(anchor="s")

fr=tk.Label(root,text="Enter four digit passcode")
fr.pack()

number_entry = tk.Entry(root)
number_entry.pack(anchor="s")


submit_button = tk.Button(root, text="Encrypt", command=handle_number)
submit_button.pack(anchor="s")


root.mainloop()



