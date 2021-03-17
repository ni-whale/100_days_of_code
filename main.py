# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
heights_sum = 0
i = 0
for student in student_heights:
  heights_sum += student
  i += 1

print(f'Heights sum: {heights_sum}\nQuantity of students: {i}\nAverage height is {round(heights_sum/i)}')

#Write your code below this row 👇




