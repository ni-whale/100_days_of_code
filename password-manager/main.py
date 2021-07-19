from tkinter import *
from tkinter import messagebox
import secrets
import pyperclip

# ---------------------------- CONSTANTS ------------------------------- #
NAVY = "#334257"
LIGHT_NAVY = "#476072"
DARK_BLUE = "#548CA8"
GRAY = "#EEEEEE"
FONT = ("Courier", 12, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password = secrets.token_urlsafe(9)
    pyperclip.copy(password)
    e_password.delete(0, END)
    e_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def password_saving():
    website = e_website.get()
    email = e_email.get()
    password = e_password.get()
    info = [website, email, password]
    if "" in info:
        messagebox.showerror("Oops", message="Please make sure you haven't left any fields empty.")
    else:
        result = f"{website} | {email} | {password}"
        with open("password.txt", mode="a") as file:
            file.write(f"{result}\n")
        messagebox.showinfo(title="Record adding", message="The password was successfully added.")
        data_deleting()


def data_deleting():
    e_website.delete(0, END)
    e_email.delete(0, END)
    e_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass")
window.config(padx=20, pady=20, bg=NAVY)

# Canvas
canvas = Canvas(width=250, height=250, bg=NAVY, highlightthickness=0)
mypass_logo = PhotoImage(file="Logo 250x250/Blue and White Hexagon Mountain Peaks Adventure Logo.png")
canvas.create_image(115, 125, image=mypass_logo)
canvas.grid(column=1, row=0)

# Labels
l_website = Label(text="Website:", font=FONT, bg=NAVY, fg=GRAY)
l_website.grid(column=0, row=1)

l_email = Label(text="Email/Username:", font=FONT, bg=NAVY, fg=GRAY)
l_email.grid(column=0, row=2)

l_password = Label(text="Password:", font=FONT, bg=NAVY, fg=GRAY)
l_password.grid(column=0, row=3)

# Entries
e_website = Entry(width=46, bg=GRAY)
e_website.focus()
e_website.grid(column=1, row=1, columnspan=2, pady=(5, 5))

e_email = Entry(width=46, bg=GRAY)
e_email.grid(column=1, row=2, columnspan=2, pady=(5, 5))

e_password = Entry(width=32, bg=GRAY)
e_password.grid(column=1, row=3, pady=(5, 5), padx=(0, 5))

# Buttons
b_generate_password = Button(text="Generate", font=FONT, bg=GRAY, activebackground=DARK_BLUE,
                             command=password_generator)
b_generate_password.grid(column=2, row=3, pady=(5, 5))

b_add = Button(text="Add", font=FONT, width=34, bg=GRAY, activebackground=DARK_BLUE,
               command=password_saving)
b_add.grid(column=1, row=4, columnspan=2, pady=(5, 5))

window.mainloop()
