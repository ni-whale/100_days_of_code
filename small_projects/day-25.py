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

data = pandas.read_csv("weather_data.csv")

# temp_list = data["temp"].to_list()

# print(data["temp"].max())

# print(data.loc[data.temp.max()])

# print(data[data.temp == data.temp.max()])

day = data[data.day == "Monday"]

print(int(day.temp) * 1.8 + 32)