from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for record in question_data:
    question_bank.append(Question(record["text"], record["answer"]))

quiz_brain = QuizBrain(question_bank)

in_game = True

while quiz_brain.still_has_questions():
    quiz_brain.next_question()


