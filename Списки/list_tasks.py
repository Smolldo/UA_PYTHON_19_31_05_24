# Написати програму, що рахує суму всіх елеметів у списку.
a = [1,2,3,4,5]
suma = 0
for i in a:
    suma += i
print(suma)

# Написати програму, що рахує добуток всіх елементів у списку.
dob = 1
for i in a:
    dob *= i
print(dob)

# Написати програму, що перевірить порожній список чи ні.
b = []

if not b:
    print('spisok porozhniy')
else:
    print('spisok ne porozhniy')

# Написати програму, яка видалить зі списку 0-й, 5-й і 7-й елементи зі списку
c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
del c[7]
del c[5]
del c[0]
print(c)

# Написати програму, що дістає максимальне число зі списку.
print(f'max num from {a}\n is {max(a)}')

# Піднести кожен із елементів списку до кубу

cubed = [i**3 for i in a]
print(cubed)

# Видалити пусті строки зі списку.
d = ['a', ' ', 'sd', '']
new_d = []
for i in d:
    item = i.strip()
    if item:
        new_d.append(item)
print(new_d)

# Написати програму, що дістає мінімальне число зі списку.
print(f'min num from {a}\n is {min(a)}')

# Написати програму, що прибере дублікати зі списку.

f = [1,2,3,1,1,2,3,6,8,7]
# f_n = []
# for i in f:
#     if i not in f_n:
#         f_n.append(i)
# print(f_n)
f_n = list(set(f))
print(f_n)

# Написати програму, що порахує кількість додатніх елементів і списку та кількість від’ємних
numbers = [3, -1, 7, -4, 2, -8, 5, -6, 9, -3]
pos = 0
neg = 0

for i in numbers:
    if i > 0:
        pos+=1
    else:
        neg +=1
print(f' pos = {pos}. neg = {neg}')


# Якщо число в списку парне — додайте до нього 1. Якщо непарне — відніміть 2.
new_list = []
# [3, -1, 7, -4, 2, -8, 5, -6, 9, -3]
for i in numbers:
    if i % 2 == 0:
        i = i +1
    else:
        i = i - 2
    new_list.append(i)
print(new_list)

# Написати програму, що порахує кількість унікальних елементів у списку.
f = [1,2,3,1,1,2,3,6,8,7]

uniq = set(f)
print(f'uniq elems in f = {len(uniq)}')

# Написати програму, що виведе список, після видалення із нього непарних елементів
f = [1,2,3,1,1,2,3,6,8,7]

n = [i for i in f if i % 2 == 0]
print(n)

# Створіть програму, яка приймає список чисел та виводить на екран кожне друге число у списку.
for i in range(1, len(numbers), 2):
    print(numbers[i])


# Написати програму, що виведе список, після видалення із нього парних елементів
f = [1,2,3,1,1,2,3,6,8,7]

n = [i for i in f if i % 2 != 0]
print(n)

# Створити програму, яка приймає список слів та повертає список слів у зворотньому порядку.
c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(c)
c.reverse()
print(c)

# Створити програму, яка приймає список чисел та повертає список елементів, які є менші за середнє значення списку.
f = [1,2,3,1,1,2,3,6,8,7]

ser = sum(f) / len(f)
nl = []
for i in f:
    if i < ser:
        nl.append(i)
print(nl)

# Написати програму, яка знайде список слів, які довші за N(довільне) у заданому списку (список з будь-яких слів)
l1 = ['Hello', 'my', 'hobby', 'is', 'coding']
N = 3

l1n = [i for i in l1 if len(i) > N]
print(l1n)

# робити новий список на основі двох початкових (конкатенація). 
l2 = [1,2,3]
l3 = [4,5,6]
l4 = l2 + l3
print(l4)


students = [
    ["Andriy", "NJNK"], 
    ["sdgfsdf", "dfgdfg"], 
    ["strsdf", "sdfsd"]
    ]

for name in students:
    name[0] == 'Andriy'


# Завдання теми 6

goods =[
    "хліб",
    "молоко",
    "яйця",
    "яблука",
    "картопля",
    "сир",
    "куряче м'ясо",
    "рис",
    "паста",
    "помідори"
]

new_goods = []

solds = []

# Показ усіх наявних товарів (виведення елементів списку),
print('Список товарів: ')
iterator = 1
for i in goods:
    print(f'{iterator}. {i}')
    iterator += 1

# Постачання нових товарів (додавання елементів, об’єднання списків),
print('Додавання нових товарів: ')
print('Напишіть назву нового товару або 0 для виходу')

while True:
    product = input('> ')

    if product == '0':
        break
    else:
        new_goods.append(product)
goods.extend(new_goods)
print(goods)

# Продаж товарів (пошук елемента списку і видалення його),
print('Що купуємо?')

while True:
    print('Товари в наявностфі', goods)
    product = input('> ')

    if product == '0':
        print('Дякуємо за покупки)))))')
        break
    else:
        if product in goods:
            goods.remove(product)
            solds.append(product)
            print(f'Товар {product} куплено. Залишилося в наявності: {goods.count(product)}')
        else:
            print('Товару нема. бери шось інкше')

# Заміна проданих продуктів на нові (вставка елемента),
prindex = goods.index('сир')  
goods.insert(prindex, 'творожок')

# Виведення списку проданих продуктів за день,
# Показати історію продажів (виведення списку в зворотному порядку).
print('продані товари за день: ')
solds.reverse()

for i in solds:
    print(f'- {i}')