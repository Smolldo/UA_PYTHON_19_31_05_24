# Напишіть програму, яка приймає від користувача рядок тексту і визначає всі слова, 
# що повторюються в цьому рядку. Програма повинна вивести ці слова у вигляді множини

string = input('Enter smth: ').split()

repeats = set(i for i in string if  string.count(i)>= 2)
# for i in string:
#     if string.count(i) >=2:
#         repeats.add(i)
print(repeats)



# Задано список чисел. Потрібно визначити, які числа з цього списку є паліндромами 
# (тобто, їх можна прочитати однаково зліва направо і справа наліво). Виконати тернарним оператором

arr = [123, 234 ,545, 666, 3232]

palindroms = [i for i in arr if str(i) == str(i)[::-1]]
print(palindroms)


# Написати програму генератор пароля, яка просить користувача надати довжину бажаного пароля.
import random

length =  int(input())

symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-+=*/%()[]{}<>.,;:"!?#$&@^|`'

password = ''

for i in range(length):
    password += random.choice(symbols)
print(password)

