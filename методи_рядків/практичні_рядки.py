# Ввести рядок з клавіатури. Видалити з неї всі цифри.

nums = ['0', '1', '2','3','4','5','6','7','8','9']
inp = input('> ')

new_str = ''

for char in inp:
    if char not in '0123456789':
        new_str += char
print(new_str)


# Порахувати, яка літера найчастіше зустрічається у вашому прізвищі.

surname = input('>').lower()

uniq_w = set(surname)

max_freq = 0
common_letter = ''

for char in uniq_w:
    freq = surname.count(char)
    if freq > max_freq:
        max_freq = freq
        common_letter = char
print(f'найчастіше: {common_letter}. зустрічається {max_freq} разів')

# Напишіть програму, яка приймає рядок, та перевертає його за допомогою слайсингу

a = 'abcdef'

a1 = a[::-1]
print(a1)


# Напишіть програму, яка приймає рядок, та перевертає його 
# без використання слайсингу (1. Використання списків. 2. Використання циклу.)

a2 = 'abcdefsdіфвффівй42342342345цкцка'

lst = list(a2)


for i in range(len(lst) -1, -1, -1):
    print(a2[i], end='')


# Створіть програму, яка перевіряє чи рядок включає в собі лише цифри.

txt = input('>')

for char in txt:
    if char not in '0123456789':
        print('в рядку міститься літера')
        break

if txt.isdigit():
    print('рядок тільки числа')
else:
    print('є букви')

txt1 = 'рядок тільки числа' if txt.isdigit() else 'є букви'
print(txt1)


# Створіть програму, яка приймає
#  рядок, та повертає рядок, з якого було видалено всі пробіли.

inp = input('> ')

noSpaces = inp.replace(' ', '')
print(noSpaces)


# Створіть програму, яка приймає рядок, 
# та повертає рядок у якому кожне слово буде з великої букви.

strng = 'fdsjf gfsdhjfkg sdfsyudf sdfs'
strng = strng.title()
print(strng)