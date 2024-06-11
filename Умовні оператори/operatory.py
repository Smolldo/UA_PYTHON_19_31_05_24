# умовне виконання — виконання блоку інструкцій тільки, коли наступає певна умова;
# цикли — повторення виконання блоку інструкцій поки виконується деяка умова;
# винятки — виконання блоку інструкцій у разі помилки.


# УМОВНЕ РОЗГАЛУЖЕННЯ
a = int(input('Enter ur num: '))

if a > 0:
    print('a positive')
elif a < 0:
    print('a negative')
else:
    print(' a == 0')

# чому тут ніколи не виведе в консоль 'Число доівнює 1'
a = input('Введіть число')
a = int(a)
if a > 0:
    print('Число додатнє')
elif a == 1:
    print('Число доівнює 1')
else:
    print("a <= 0")

#  логічні вирази. неявне приведення до True / False
money = 0
if money: # money == False
 	print(f"You have {money} on your bank account")
else:
	print("You have no money and no debts")
	

result = None
if result:
    print(result)
else:
    print("Result is None, do something")


user_name = input("Enter your name: ")

if user_name:
    print(f"Hello {user_name}")
else:
    print("Hi Anonym!")

# У Python оператори булевої алгебри — це оператори not, and, or.

a = True and False
print(a)

a = True or False # False or True
print(a)

a = not 2 < 0
print(a)


# Визначення високосного року
year = int(input('Enter year: '))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print('visokosnyy')
else:
    print('ne visokosniy')

#Тернарний оператор
x = 8

is_odd = ' is odd' if x % 2 != 0 else 'is even'
print(is_odd)

grade = 60

is_good = 'u pass' if grade >=60 else 'u loose'
print(is_good)


