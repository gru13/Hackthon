import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from Encryption import *

# Create a Tkinter window

def main():
    root = tk.Tk()
    root.geometry("1440x720")
    root.title("Encryption")
    file_path = None
    canvas = tk.Canvas(root, width=1200, height=500)
    canvas.pack()

    def handle_number():
        global number_entry
        number = int(number_entry.get())
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

        number_entry.destroy()




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
    button.pack()


    number_entry = tk.Entry(root)
    number_entry.pack()


    submit_button = tk.Button(root, text="Encryption", command=handle_number)
    submit_button.pack()


    root.mainloop()

main()