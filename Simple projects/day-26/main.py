# with open("file1.txt") as file:
#     file1 = file.readlines()
# with open("file2.txt") as file2:
#     file2 = file2.readlines()
#
# result = [int(num) for num in file1 if num in file2]
#
# print(result)

# with open("file1.txt") as file1:
#     list1 = file1.readlines()
#
# with open("file2.txt") as file2:
#     list2 = file2.readlines()
#
# result = [int(num) for num in list1 if num in list2]
#
# # Write your code above 👆
# print(result)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
# result = {word: len(word) for word in sentence.split()}
#
# print(result)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

# (temp_c * 9/5) + 32 = temp_f

# Write your code 👇 below:
weather_f = {day: temp_c * 1.8 + 32 for day, temp_c in weather_c.items()}


print(weather_f)
