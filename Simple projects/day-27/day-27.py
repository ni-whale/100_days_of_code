from tkinter import *


def button_cliked():
    my_label.config(text=input.get())


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I'm a label", font=("Courier", 18, "normal"))
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click me", command=button_cliked)
button.grid(column=1, row=1)

button = Button(text="Click me", command=button_cliked)
button.grid(column=2, row=0)

# Entry(input)
input = Entry(width=10)
input.grid(column=3, row=3)

window.mainloop()




