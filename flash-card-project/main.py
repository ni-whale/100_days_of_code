from tkinter import *
import pandas
import random
# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

# # ---------------------------- LOGIC SETUP ------------------------------- #
# df = pandas.read_csv("data/Words_eng+rus.csv")
# data = df.to_dict()
#
# def generate_word():
#     random_position = random.randint(0, 1112)
#     random_word = data['Word'][random_position]
#     translation = data['Translation'][random_position]
#     canvas.itemconfig(c_lang_of_the_word, text="English")
#     canvas.itemconfig(c_word, text=random_word)

df = pandas.read_csv("data/Words_eng+rus.csv")
data = df.to_dict(orient="records")


def next_card():
    current_card = random.choice(data)
    canvas.itemconfig(c_lang_of_the_word, text="English")
    canvas.itemconfig(c_word, text=current_card['Word'])


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_img)
c_lang_of_the_word = canvas.create_text(400, 150, text="Title", font=("Arial", 30, "italic"))
c_word = canvas.create_text(400, 263, text="Word", font=("Arial", 50, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
check_mark_img = PhotoImage(file="images/right.png")
b_right = Button(image=check_mark_img, highlightthickness=0, command=next_card)
b_right.grid(column=1, row=1)

crisscross_img = PhotoImage(file="images/wrong.png")
b_wrong = Button(image=crisscross_img, highlightthickness=0, command=next_card)
b_wrong.grid(column=0, row=1)

next_card()

window.mainloop()
