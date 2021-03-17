student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# Scores
# 91 - 100: Grade = "Outstanding"
#
# Scores
# 81 - 90: Grade = "Exceeds Expectations"
#
# Scores
# 71 - 80: Grade = "Acceptable"
#
# Scores
# 70 or lower: Grade = "Fail"
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

for score in student_scores:
    if student_scores[score] <= 70:
        student_grades[score] = "Fail"
    elif 71 <= student_scores[score] <= 80:
        student_grades[score] = "Acceptable"
    elif 81 <= student_scores[score] <= 90:
        student_grades[score] = "Exceeds Expectations"
    else:
        student_grades[score] = "Outstanding"

# 🚨 Don't change the code below 👇
print(student_grades)