import turtle as t
import random

# Damien Heist Color Pallete
# import colorgram
# num_of_colors = 100
# colors = colorgram.extract('spot.jpg', num_of_colors)
# colors_list = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     colors_list.append(new_color)
#
# print(colors_list)

color_list = [(192, 165, 115), (138, 166, 190), (56, 102, 140), (141, 91, 50), (12, 23, 55), (222, 207, 123), (182, 154, 42), (61, 22, 11), (182, 146, 165), (142, 177, 151), (72, 117, 81), (58, 15, 26), (126, 79, 102), (130, 30, 16), (15, 39, 23), (24, 53, 127), (177, 188, 215), (164, 104, 134), (115, 31, 46), (97, 150, 100), (98, 121, 172), (210, 178, 197), (174, 105, 93), (74, 150, 165), (25, 91, 65), (172, 205, 180), (86, 76, 17), (216, 181, 175), (163, 203, 213), (18, 86, 100), (231, 205, 16)]
tim = t.Turtle()
t.colormode(255)

# MY SOLUTION
# tim.penup()
# tim.setposition(-225, -200)
# y_cord = -200
#
# for _ in range(10):
#     for _ in range(10):
#         tim.pendown()
#         tim.color(random.choice(color_list))
#         tim.dot(20)
#         tim.penup()
#         tim.forward(50)
#
#     y_cord += 50
#     tim.setposition(-225, y_cord)

# ANGELA'S SOLUTION
# tim.speed(0)
# tim.penup()
# tim.hideturtle()
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
# for dot_count in range(1, number_of_dots+1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#
#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)
#

# MODIFYING MY CODE TO REMOVE THE TURTLE AND PENUP AS DOT DOESN'T NEED PENDOWN.
tim.penup()
tim.speed(0)
tim.hideturtle()
tim.setposition(-225, -200)
y_cord = -200

for _ in range(10):
    for _ in range(10):
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.forward(50)

    y_cord += 50
    tim.setposition(-225, y_cord)


screen = t.Screen()
screen.exitonclick()
