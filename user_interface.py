from tkinter import *


bg  = PhotoImage(file="leo.jpg")
Win = Tk()

x,y = bg.width,bg.height
Win.title("our project")
Win.maxsize(x,y)
Win.minsize(x,y)
Win.geometry(f"{x}x{y}")

can = Canvas(Win,width=x,height=y)
can.create_image(bg)
Win.mainloop()
