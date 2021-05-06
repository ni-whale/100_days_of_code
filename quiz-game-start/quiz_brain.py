class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.showed_questions = []

    def still_has_questions(self):
        for element in self.question_list:
            if self.question_list[element] == self.showed_questions[element]:
                print("Found the question which appeared already")
                return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.showed_questions.append(self.question_list[self.question_number])
        input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
