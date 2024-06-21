#1 Написати код який буде просити ім'я користувача до поки він його не напише
print("Task 1")
name = '' # задаємо порожній рядок

while not name: # коли змінна name не буде порожнім рядком, спрацює умова, яка необхідна для привітання
    name = input('Enter name: ')

print(f'hello {name} \n')

# Написати код який рахує суму всіх чисел в діапазоні який задав користувач
print("Task 2")
x = int(input('enter first num: '))
y = int(input('enter second num: ')) # х і у задають початок і кінець проміжку
sum = 0 # сума чисел

for i in range(x,y + 1): #ОБОВ'ЯЗКОВО пишемо у+1, інакше в проміжку ваше число буде на 1 менше від заданого.
    sum += i # почергове додавання усіх чисел з проміжку
print(f'сума чисел від {x} до {y} = {sum} \n')

# Написати програму, яка виведе таблицю множення числа, яке задав користувач. Приклад (2 4 6 8 10 12 14 16 18 20)
print("Task 3")
a = int(input('Enter ur num: '))

for i in range(1,10):
    print(f'{a} * {i} = {a*i} \n')

# Написати програму, яка виведе число від -10 до -1 використовуючи цикл
print("Task 4")
for i in range(-10,0): #Задаємо проміжок від -10 до  -1. 
    print(f'числа в зворотньому напрямку від -10 до -1: {i}')
    print('\n')

# Дано змінну a = 1. Виводити a, поки a <= 15.
print("Task 5")
a = 1

while True:
    print(a)
    if a >=15:
        break
    a+=1
print('\n')
# Написати програму, яка додасть “Hello” до кожного із імен в списку і виведе привітання на екран. lst=["Dima", "Yaroslav", "Zhenya", "Sasha", "Andrii", "Max"]. Приклад — Hello Dima!
print("Task 6")
lst=["Dima", "Yaroslav", "Zhenya", "Sasha", "Andrii", "Max"]

for i in lst:
    print(f'Hello, {i}')
print('\n')

# Дано слово “Цивілізація”. За допомогою циклу порахувати скільки літер “і” містить в собі це слово.
print("Task 7")
word = 'Цивілізація'
count = 0
for char in word:
    if char == 'і':
        count +=1
print(f'Кількість "{char}" в {word} = {count}')
print('\n')

# Зробити попередню програму більш універсальною — Запитувати у користувача слово та літеру для пошуку.
# Використати блок “else” щоб вивести повідомлення “Завершено” після успішного виходу з циклу (довільний)
print("Task 8 & 9")
word = input('Enter word:')
letter = input("Enter letter: ")
count = 0
for char in word.lower():
    if char == letter:
        count+=1
else: 
    print("Підрахунок завершено")
print(f'amount of "{letter}" in {word} = {count}')
print('\n')

# Написати програму, яка порахує і виведе куби всіх чисел від 1 до числа, яке задасть користувач
print("Task 10")
num = int(input("Enter num: "))

for i in range(1, num + 1):
    print(f'куб числа {i} = {i**3}')
print('\n')

# Дано дійсне число — ціна 1 кг цукерок. Вивести вартість 1, 2, ..., 10 кг цукерок.
print("Task 11")
price = 12.25

for i in range(1,11):
    print(f'ціна за {i}кілограм цукерок = {price*i} гривень')
print('\n')

# Дано дійсне число - ціна 1 кг цукерок. Вивести вартість 1.2, 1.4, ..., 2 кг цукерок.
print("Task 12")
price = 12
weight = 1.2

while weight <= 2:
    print(f'ціна за {weight:.2f} кілограм цукерок = {price*weight:.2f}')
    weight+= .2
print('\n')

# Дано діапазон чисел від 0 до 100. Вивести на екран лише парні числа
print("Task 13")
for i in range(101):
    if i % 2 != 0:
        continue
    print(i)
print('\n')

# Дано діапазон чисел (Користувач обирає сам (input)). Вивести на екран лише непарні числа і 0 (в кінці)
print("Task 14")
x = int(input("Enter 1 num: "))
y = int(input("enter 2 num: "))

for i in range(x,y+1):
    if i % 2 == 0:
        continue
    print(i)
else:
    print(0)
print('\n')

# Написати програму, яка виведе факторіал числа, яке задасть користувач (цикл while)
# 5! = 1*2*3*4*5
print("Task 15")
start = 1
a = int(input("ENter num: "))
factor = 1

while start <= a:
    factor *= start
    start+=1
print(f'факторіал числа {a} = {factor}')
print('\n')


# Написати програму, яка зчитає 3 числа (a, b, c) та порахує скільки чисел лежить між “a” i “b”, які діляться на “с”
print("Task 16")
a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))
sum = 0

for i in range(a,b+1):
    if i % c == 0:
        sum+=1
print(sum)