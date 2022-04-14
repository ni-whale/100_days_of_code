from tkinter import *
import pandas
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
# # ---------------------------- LOGIC SETUP ------------------------------- #
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/Words_eng+rus.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=front_card_img)
    canvas.itemconfig(c_lang_of_the_word, text="English", fill="Black")
    canvas.itemconfig(c_word, text=current_card['Word'], fill="Black")
    flip_timer = window.after(1500, func=flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(c_lang_of_the_word, text="Russian", fill="white")
    canvas.itemconfig(c_word, text=current_card['Translation'], fill="white")
    canvas.itemconfig(canvas_image, image=back_card_img)


def is_known():
    global current_card
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(1500, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_card_img)
c_lang_of_the_word = canvas.create_text(400, 150, text="Title", font=("Arial", 30, "italic"))
c_word = canvas.create_text(400, 263, text="Word", font=("Arial", 50, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
check_mark_img = PhotoImage(file="images/right.png")
b_right = Button(image=check_mark_img, highlightthickness=0, command=is_known)
b_right.grid(column=1, row=1)

crisscross_img = PhotoImage(file="images/wrong.png")
b_wrong = Button(image=crisscross_img, highlightthickness=0, command=next_card)

b_wrong.grid(column=0, row=1)

next_card()

window.mainloop()

# # make messagebox available
# from tkinter import messagebox
#
# # set callback for window close
# window.protocol("WM_DELETE_WINDOW", save_files)
#
#
# # window close callback function
#
# def save_files():
#     # Prompt user for confirmation
#     if messagebox.askokcancel(title="Goodbye", message="Update dictionary based on this session?"):
#
#     # File saving logic goes here.
#     # Dict updating is in a separate function
#
#     window.destroy()