from tkinter import *



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("MyPass")
window.config(padx=20, pady=20)

# Canvas
canvas = Canvas(width=500, height=500)
mypass_logo = PhotoImage(file="Logo 500x500/1.png")
canvas.create_image(250, 250, image=mypass_logo)
canvas.pack()


window.mainloop()