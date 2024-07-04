# Using csv module
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for row in data:
#         if row[1] == 'temp':
#             pass
#         else:
#             temp.append(int(row[1]))
#
#     print (temp)
#
# Using pandas module

import pandas
# data = pandas.read_csv("weather_data.csv")
# # temp_list = data["temp"]
# # average = sum(temp_list)/len(temp_list)
# # print(round(average, 2))
#
# # Using pandas series
# average = data["temp"].mean()
# print(average)
# maximum = data["temp"].max()
# print(maximum)
#
#
# # Get data in columns
# print(data.condition)

# Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# Create a data frame from scratch
# data_dict = {
#     "students":["Amy", "Ash", "Ace"],
#     "score":[76,56,54]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
#
# # converting to csv file
# data.to_csv("new_data.csv")

with open("Squirrel_data.csv") as data_file:
    data = pandas.read_csv(data_file)
    grey_color = data[data["Primary Fur Color"] == "Gray"]
    red_color = data[data["Primary Fur Color"] == "Cinnamon"]
    black_color = data[data["Primary Fur Color"] == "Black"]
    number = [len(grey_color), len(red_color), len(black_color)]
    data_dict = {
        "Color": ["Gray", "Cinnamon", "Black"],
        "Count": number
    }
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv("Fur_count.csv")
