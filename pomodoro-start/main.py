from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✅"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
FONT = ("Courier", 40, "normal")
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
    elif reps % 2 == 0:
        count_down(short_break_sec)
    else:
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0 or count_sec < 10:
        count_sec = "0" + str(count_sec)
    # if count_min == 0 or count_min < 10:
    #     count_min = "0" + str(count_min)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(105, 135, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Labels
main_label = Label(text="Timer", font=FONT, bg=YELLOW, fg=GREEN)
main_label.grid(column=1, row=0)
check_mark_label = Label(text="✅", bg=YELLOW, fg=GREEN, font=("Courier", 14, "normal"))
check_mark_label.grid(column=1, row=4)

# Buttons
start_button = Button(text="Start", bg=PINK, activebackground=GREEN, fg="white",
                      width=5, height=2, font=("Courier", 13,"normal"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=PINK, activebackground=GREEN, fg="white", width=5, height=2, font=("Courier", 13,
                                                                                                          "normal"))
reset_button.grid(column=2, row=2)


window.mainloop()