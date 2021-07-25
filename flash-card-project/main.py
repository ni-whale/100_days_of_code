from tkinter import *
import pandas
import random
# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- LOGIC SETUP ------------------------------- #
# def generate_word():
#     df = pandas.read_csv("data/Words_eng+rus.csv")
#     data = df.to_dict()
#     temp = [item for item in data[random.randint(0, 1110)]]
#     print(temp)

df = pandas.read_csv("data/Words_eng+rus.csv")
data = df.to_dict()
word, translation = random.choice(list(data.items()))
print(f"{word}")
print(f"{translation}")

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
b_right = Button(image=check_mark_img,  highlightthickness=0)
b_right.grid(column=1, row=1)

crisscross_img = PhotoImage(file="images/wrong.png")
b_wrong = Button(image=crisscross_img,  highlightthickness=0)
b_wrong.grid(column=0, row=1)

window.mainloop()
