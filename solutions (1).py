# Problem 1


for i in range(100):
  print("Hello World")

# Problem 2

numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# Loop that prints each number in a new line
for num in numbers:
  print(num)

# Loop that prints each number and its square
for num in numbers:
  print(num, num ** 2)

# Problem 3

number_of_sides = int(input("Enter the number of sides: "))
length_of_sides = int(input("Enter the length of sides: "))
color_of_line = input("Enter the color of line: ")

angle = 360 / number_of_sides

from turtle import *

polygon_ = turtle.Turtle()
pencolor(color_of_line)

for i in range(number_of_sides):
        polygon_.forward(length_of_sides)
        ploygon_.left(angle)



# Program 4

for i in range(1, 51):
  if i % 3 and i % 5:
    print(f"i is divisible by both")
  if i % 3:
    print(f"{i} is divisible by three")
  if i % 5:
    print(f"{i} is divisible by five")

# Program 5

from turtle import *

t = turtle.Turtle()
 
for i in range(5):
  t.forward(100)
  t.right(144)
  t.forward(100)
  t.left(144)
  t.forward(100)
  t.right(144)

