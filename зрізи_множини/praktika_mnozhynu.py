sntc = input('>')

words = sntc.split()

longest_word = 'it'
length = 0 #5

for i in words:
    if len(i) > length:
        longest_word = i[:]
        length = len(i)

print(f'longest word - {longest_word} ')


# Створіть список з чисел від 1 до 10 та використайте зрізи для виводу елементів від другого до п'ятого включно.
numbers = list(range(1,11))

# print(numbers[1:5])


# Створіть рядок та використайте зрізи для виводу перших трьох та останніх трьох символів.
str1 = 'galaxy lamp'

# print(f'first 3 symbols: {str1[:3]}')
# print(f'last 3 symbols: {str1[-3:]}')



# Створіть список зі стрічок та використайте зрізи для виводу останніх трьох символів з кожної стрічки.
strings = ['apple', 'coffee', 'steak', 'xerox']

# for i in strings:
#     print(i[-3:])
a = [i[-3:] for i in strings ]
# print(a)


# Створіть список зі стрічок та використайте зрізи для виводу символів з кожної стрічки у зворотньому порядку.
a1 = [i[::-1] for i in strings]
# print(a1)


# Створіть множину та перевірте, чи є вона підмножиною іншої множини.

s1 = {1,2,3,4,5,6}
s2 = {2,5,6}

# subset - підмножина  issubset() - чи це підмножина?

# print(s2.issubset(s1))


# Створіть список, який містить у собі 10 стрічок, які 
# складаються з двох слів, розділених пробілом. Використовуючи зрізи,
#  виведіть на екран кожне слово з кожної стрічки у зворотньому порядку.

sentences = [
    "hello world", #dlorow olleh
    "good morning",
    "python programming",
    "open source",
    "data science",
    "machine learning",
    "artificial intelligence",
    "natural language",
    "deep learning",
    "neural networks"
]

# for elem in sentences:
#     print(elem[::-1], end=', ')



# Створіть множину, яка містить у собі числа від 1 до 20. Використовуючи методи множин, 
# створіть дві нові множини - одну з парними числами, іншу з непарними числами.

arr = list(range(1,21))
# sss = set(i for i in arr if i % 2 == 0)
set1 = {i for i in arr if i % 2 == 0}
# print(set1)
# print(sss)

set2 = {i for i in arr if i % 2 != 0}
# print(set2)


# Створіть список, який містить у собі 20 випадкових чисел від 1 до 50. 
# Використовуючи зрізи, виведіть на екран середнє арифметичне значення елементів з 
# першої половини списку та другої половини списку окремо.

import random

arr1 = [random.randint(1,51) for i in range(1,21)]   # random.randint(start, end)
print(arr1)

av1 = sum(arr1[:10]) / len(arr1[:10])
av2 = sum(arr1[10:]) / len(arr1[10:])
print(av1)
print(av2)

