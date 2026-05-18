# # with open("weather_data.csv") as file:
# #     data = file.readlines()
# # print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #         print(temperatures)
#
# import pandas
# # from pandas.core.internals.construction import dataclasses_to_dicts
# #
# data = pandas.read_csv("weather_data.csv")
# # # print(type(data))
# # # print(type(data["temp"]))
# #
# # temp_list = data["temp"].to_list()
# #
# # maximum = data["temp"].max()
# # print(maximum)
#
#
# #Get Data in Rows
#
# # print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# fahrenheit = (monday.temp * 9 / 5) + 32
#
# print(fahrenheit)
#
#
# #Create a dataframe from scratch
#
# data_dict = {
#     "students": ["Amy", " James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
#
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260518.csv")

squirrels_gray_count = len(data[data["Primary Fur Color"] == "Gray"])
squirrels_red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
squirrels_black_count = len(data[data["Primary Fur Color"] == "Black"])
print(squirrels_gray_count)
print(squirrels_red_count)
print(squirrels_black_count)


data_dict = {
    "Primary Fur Color": ["Gray", "Cinnamon", "Black"],
    "Counts": [squirrels_gray_count, squirrels_red_count,squirrels_black_count],
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")