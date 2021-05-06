from question_model import Question
from data import question_data

question_bank = []

for record in question_data:
    question_bank.append(Question(record["text"], record["answer"]))

print(question_bank[0].answer)