import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Create a Tkinter window
root = tk.Tk()

# Set the title of the window
root.title("Image Input via File Dialog")

# Create a canvas to display the image
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Create a function to open a file dialog and select an image
def open_image():
    # Open a file dialog to select an image file
    file_path = filedialog.askopenfilename()

    # Load the selected image using PIL
    image = Image.open(file_path)

    # Resize the image to fit in the canvas
    image = image.resize((300, 300))

    # Convert the image to a Tkinter-compatible format
    tk_image = ImageTk.PhotoImage(image)

    # Update the canvas with the new image
    canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
    canvas.image = tk_image  # Keep a reference to the image to prevent garbage collection

# Create a button to open the file dialog and select an image
button = tk.Button(root, text="Select Image", command=open_image)
button.pack()

# Create an Entry widget to get a number from the user
number_entry = tk.Entry(root)
number_entry.pack()

# Create a function to handle the number input
def handle_number():
    number = int(number_entry.get())
    print("The user entered the number:", number)

# Create a button to submit the form
submit_button = tk.Button(root, text="Submit", command=handle_number)
submit_button.pack()

# Start the Tkinter event loop
root.mainloop()
