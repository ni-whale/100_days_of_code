from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for record in question_data:
    question_bank.append(Question(record["text"], record["answer"]))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()
print("You have complete the quiz.")
print(f"The final score was: {quiz_brain.score}/{quiz_brain.question_number}")
