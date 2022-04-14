from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=30, pady=30, bg=THEME_COLOR)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=(25, 30))

        # Labels
        self.label_score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 15, "normal"))
        self.label_score.grid(column=1, row=0)

        # Buttons
        true_icon = PhotoImage(file="images/true.png")
        self.button_true = Button(image=true_icon, highlightthickness=0, command=self.true_pressed)
        self.button_true.grid(column=0, row=2)

        false_icon = PhotoImage(file="images/false.png")
        self.button_false = Button(image=false_icon, highlightthickness=0, command=self.false_pressed)
        self.button_false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.label_score.configure(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)






