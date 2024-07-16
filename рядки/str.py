a1 = 'lorem'
a2 = "lorem"

print(a1 == a2)

s = """ lorem
ipsum"""
print(s)

one_line_text = "Textual data in Python is handled with str objects, "\
"or strings. Strings are immutable sequences of Unicode code points." \
"String literals are written in a variety of ways: single quotes, "\
"double quotes, triple quoted."

print(one_line_text)



# str() - функція для приведення даних до типу  string

q = str(12)
print(type(q))

w = str([1,2,3,4,54])
print(w)


s1 = 'Hello World'
print(s1[-2])

# Створити рядок, який складається з імені і прізвища учня (Ivanov Ivan).
# Порівняти, чи перша літера імені співпадає з першою літерою прізвища і вивести відповідне повідомлення.
# При отриманні літери прізвища використати від’ємний індекс.

pib = 'Ivan Ivanov'
# print(pib[4])
nl = pib[0]
sl = pib[-6]

if sl == nl:
    print(f'first name and last name start with same letter: {sl}')


# ЗРІЗИ
a = 'ABCDEFGHIJK'

# [n:m:s] n - початок(включаючи), m - кінець(не включається в зріз), s - step(крок)

print(a[:5]) # обирає символи від початку рядка до 4 індексу
print(a[-1]) # повертає останній символ рядка
print(a[5:]) # повертає рядок з 5 індексу і до кінця рядка
print(a[:]) # повертає точну копію рядка
print(a[::-1]) # відображає рядок в зворотньому порядку
print(a[-3:]) # повертає рядок від 3 символа з кінця і до кінця рядка


#Змінювання рядка - рядок НЕзмінний

# d = 'Hello'
# d[0] = 'P'
# print(d)

# Конкатенація та реплікація рядків

S = 'Hello, ' + 'Word' + '!!!!'
print(S)
# Реплікація
s = ' '
print(f'({s * 2})')

f = '-'
print(f * 20)

print('HELLO ' * 8)

# \n \t

g = 'lorem \n ipsum'
print(g)

gb = 'Jingle bells, jingle bells\nJingle all the way\nOh, what fun it is to ride\nIn a one horse open sleigh'
print(gb)

a = 'ABCDEF /$^#GHI@JK'
print(len(a))