from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✅"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
FONT = ("Courier", 40, "normal")

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(105, 135, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Labels
main_label = Label(text="Timer", font=FONT, bg=YELLOW, fg=GREEN)
main_label.grid(column=1, row=0)
check_mark_label = Label(text="✅", bg=YELLOW, fg=GREEN, font=("Courier", 14, "normal"))
check_mark_label.grid(column=1, row=4)

# Buttons
start_button = Button(text="Start", bg=PINK, activebackground=GREEN, fg="white", width=5, height=2, font=("Courier", 13,
                                                                                                          "normal"))
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=PINK, activebackground=GREEN, fg="white", width=5, height=2, font=("Courier", 13,
                                                                                                          "normal"))
reset_button.grid(column=2, row=2)


window.mainloop()