from tkinter import *

FONT = ("Courier", 10, "normal")


def button_cliked():
    my_label.config(text=input.get())


window = Tk()
window.title("Mike to Km converter")
window.minsize(width=300, height=100)
window.config(padx=10, pady=10)


# Entrie
entry = Entry(width=10)
# Add some text to begin with
entry.insert(END, string="0")
entry.grid(column=1, row=0)

# Labels
label = Label(text="is equal to", font=FONT)
label.grid(column=0, row=1)
label.config(pady=10)

label1 = Label(text="Miles", font=FONT)
label1.grid(column=2, row=0)
label1.config(padx=10)

label2 = Label(text="0", font=FONT)
label2.grid(column=1, row=1)
# label2.config(padx=10)

label3 = Label(text="Km", font=FONT)
label3.grid(column=3, row=1)
# label3.config(padx=10)

ba

window.mainloop()