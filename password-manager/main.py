import json
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
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", mode="r") as file:
                # Reading old data
                data = json.load(file)
                # Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            messagebox.showinfo(title="Record adding", message="The password was successfully added.")
            data_deleting()


# ---------------------------- PASSWORD SEARCHING ------------------------------- #
def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Please save at least one password first before make a search.")
    else:
        for website in data:
            if website == e_website.get():
                messagebox.showinfo(title="Success", message=f'Email: {data[website]["email"]}]\n'
                                                             f'Password: {data[website]["password"]}')
                pyperclip.copy(data[website]["password"])
            else:
                messagebox.showerror(title="Error",
                                     message="Password for this site wasn't found. Please, try again")

# ---------------------------- DATA CLEAN UP ------------------------------- #

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
e_website = Entry(width=32, bg=GRAY)
e_website.focus()
e_website.grid(column=1, row=1, pady=(5, 5))

e_email = Entry(width=46, bg=GRAY)
e_email.grid(column=1, row=2, columnspan=2, pady=(5, 5))

e_password = Entry(width=32, bg=GRAY)
e_password.grid(column=1, row=3, pady=(5, 5), padx=(0, 5))

# Buttons
b_generate_password = Button(text="Generate", font=FONT, bg=GRAY, activebackground=DARK_BLUE,
                             command=password_generator)
b_generate_password.grid(column=2, row=3, pady=(5, 5))

b_add = Button(text="Add", font=FONT, width=35, bg=GRAY, activebackground=DARK_BLUE,
               command=password_saving)
b_add.grid(column=1, row=4, columnspan=2, pady=(5, 5))

b_search = Button(text="Search", font=FONT, bg=GRAY, activebackground=DARK_BLUE, width=8, command=find_password)
b_search.grid(column=2, row=1, pady=(5, 5))

window.mainloop()
