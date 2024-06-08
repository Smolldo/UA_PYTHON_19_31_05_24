
# 1 завдання   s1... - string1 (рядок)
s1 = 'Hello '
s2 = 'World'
s3 = s1 + s2 # конкатенація
print(s3)

# 2  завдання a1 - age1 (число)
a1 = 23
print('I am ', a1)
print(f'I am {a1}') # форматування рядка
res = f'I am {a1} years old' # форматування рядка
print(res)


#Bool

a = True
b = False

age = 16
adult1 = age >= 16 #True
print(adult1)

age = 14
adult2 = age >= 16 #False
print(adult2)

#Завдання бул Місіс і Містер

first_name = 'Misha'
last_name = 'Honyk'
gender = 'man'

is_man = gender == 'man'

if is_man:
    sex = 'Mr'
else:
    sex = 'Ms'

grettings = f'Hello, {sex} {first_name} {last_name}'
print(grettings)

#ВБУДОВАНІ ФУНКЦІЇ
a = 2
a = 'dfsgdfg'
b = 'sdfsd'
print( a + b)


#Приведення типів даних
age = input('How old r u? ')
print(type(age))

age = int(input('How old r u? ')) #приведення типу string до int
print(type(age))


pi = float('3.14')
print(type(pi))

w = str(345)
print(type(w))



#Практичні завдання

#1 Оголосити дві змінні, одна з яких дорівнюватиме довільному числу. Інша — значення попередньої змінної збільшене на 10.
number1 = int(input('dai yakes chislo:'))
print(number1)
number2 = number1 + 10
print(number2)


#2 Оголосити змінні — радіус та число P (3.14). Визначити довжину кола та площу круга.
p = 3.14
r = 5
C = 2 * p * r
print(C)
S = p* r**2
print(S)

#3 Оголосити змінні — 3 кути трикутника (їхня градусна міра). Оголосити наступну змінну is_valid, аби отримати булеве значення (is_valid = angle1 + angle2 + angle3 == 180)
a1 = 12
a2 = 34
a3 = 99

is_valid = a1+a2+a3 == 180
print(is_valid)

#4 Створити програму звертання до користувача, використовуючи input(). Приймаємо поля “name”, “surname”, “gender” (Mam, Sir)
name = input('What is ur name')
surname = input('What is ur name')
gender = input('Choose ur gender male/female')

is_ma = gender == "male"

if is_man:
    sex = 'Sir'
else:
    sex = 'Mam'

gret = f'Hello, {sex} {name} {surname}'
print(gret)