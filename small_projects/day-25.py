# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")

# temp_list = data["temp"].to_list()

# print(data["temp"].max())

# print(data.loc[data.temp.max()])

# print(data[data.temp == data.temp.max()])

# day = data[data.day == "Monday"]
#
# print(int(day.temp) * 1.8 + 32)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

i = 0

# gray = data["Primary Fur Color"] == "Cinnamon"
# print(gray.count())


# data_set = data["Primary Fur Color"].to_list()
# data_dict = {
#     "Fur Color": ["Gray", "Red", "Black"],
#     "Count": [0, 0, 0]
# }
#
# for value in data_set:
#     if value == "Gray":
#         data_dict["Count"][0] += 1
#     elif value == "Cinnamon":
#         data_dict["Count"][1] += 1
#     elif value == "Black":
#         data_dict["Count"][2] += 1
#
# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv("squirrel_count")

# grey_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrel = len(data[data["Primary Fur Color"] == "Black"])
