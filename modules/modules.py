# import fibo
# import fibo as f
# import random as r
# from fibo import fib as f
# from fibo import *

# fibo.fib(500)
# import sys

# sys.path.append('/')

# f(500)
# fibo.fib(1000)

# fib = fibo.fib

# fib(50)

# import matplotlib.pyplot as plt
# import numpy as np

# fig, ax = plt.subplots()             # Create a figure containing a single Axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
# plt.show()                           # Show the figure.

# import turtle
# t = turtle.Turtle()

# screen = turtle.Screen()

# for _ in range(4):
#     t.forward(100)
#     t.right(90)

# screen.mainloop()

# Створити власний модуль my_module.py, який містить функцію print_message(msg), що 
# риймає один аргумент msg та виводить його на екран. Потім імпортувати функцію print_message() в 
# головний файл програми та викликати її.

from my_module import prr_msg as p

# print(p('AAAAAAAAAAA'))

# Створити власний модуль my_math.py, який містить функції add(x, y) та subtract(x, y). 
# Імпортувати модуль та використати ці функції для додавання та віднімання чисел.

import my_math

a = my_math.add
s = my_math.substract

# print(a(4,5))
# print(s(7,5))

# Створити власний модуль my_geometry.py, який містить функції circle_area(radius) та 
# rectangle_area(width, height). Імпортувати модуль та використати ці функції для обчислення площі кола та прямокутника.
from area import circ as c
from area import rect as r

# print(c(4))
# print(r(4,5))

# .Створити власний модуль my_data.py, який містить список даних (наприклад, список чисел). 
# Імпортувати модуль та вивести список даних на екран. 
# import my_data 
from my_data import *

# print(lst)

# Створити власний модуль my_statistics.py, який містить функції для 
# обчислення статистичних показників (наприклад, середнього значення, медіани, 
# дисперсії) для списку даних. Імпортувати модуль та використати ці функції 
# для обробки списку даних.

import my_stats

# print(f'seredne znach: {my_stats.mean(lst)}')
# print(f'mediana: {my_stats.mediana(lst)}')
# print(f'dispersiya: {my_stats.veriance(lst)}')

import matplotlib.pyplot as plt
import numpy as np

# Створити графік лінійної функції y = 2x + 1 за допомогою бібліотеки matplotlib.

# x = np.linspace(-10,10, 100)

# y = 2 * x + 1

# plt.plot(x,y, label = 'y = 2x + 1')

# plt.title('Графік функції')
# plt.xlabel('x')
# plt.ylabel('y')

# plt.grid(True)

# plt.show()

# Створити графік функції sin(x) за допомогою бібліотеки matplotlib.

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sin(x)


plt.plot(x,y, label = 'y = sin(x)')

plt.title('sin(x)')
plt.xlabel('x')
plt.ylabel('y')

plt.grid(True)

plt.show()