# Напишіть програму, яка приймає список чисел та повертає новий список, що містить лише унікальні елементи вхідного.
lst1 = [1,1,1,2,2,2,3,3,3,4,4,6,7,7,7,7,8,8,8,9]

lst2 = set(lst1)
lst3 = list(lst2)

lst4 = list(set(lst1))
# print(lst4)
# print(lst3)

# Напишіть програму, яка приймає словник, та змінює всі значення на їх квадрати.
dct1 = {
    'a': 2,
    'b': 3,
    'c': 4
}  # 4, 9, 16

for i, j in dct1.items():
    # j = j ** 2
    dct1[i] = j ** 2

# print(dct1)

# Створіть програму, яка приймає список рядків та повертає список унікальних слів, які зустрічаються в цих рядках.
groups = ['acdc', 'acdc', 'exodus', 'sodom', 'sodom']

uniqGroups = list(set(groups))
# print(uniqGroups)

# Напишіть програму, яка приймає список рядків та повертає список, в якому кожен елемент — 
# це рядок, який містить першу літеру кожного слова в вхідному рядку.
# strings = input('Enter words cherez probil: ').split()
# print(strings)

# strNew = []

# for i in strings:
#     strNew.append(i[0])
# print(strNew)

text = ['hello', 'lorem ipsum dolores', 'harry potter lala ohoho gggg lol', 'apple']

resultText = []

for rechennya in text:
    slovo = rechennya.split()

    pershaBukva = ''

    for bukva in slovo:
        pershaBukva += bukva[0]
    resultText.append(pershaBukva)
# print(resultText)


# Створіть програму, яка приймає список та 
# повертає рядок, який містить всі елементи вхідного списку, розділені комами.

ryadku = ['gysd', 'dsfsdfdfg', 'sfdsfigeyf', 'sdfsdfsdf']

rysd = ', '.join(ryadku)
# print(rysd)

# Напишіть програму, яка приймає два словника та повертає словник, 
# що містить ключі та значення обох вхідних словників.

d1 = {
    2:2,
    3:3
}
d2 = {
    4:4,
    5:5
}
d1.update(d2)
d3 = {}
d3.update(d1)
# print(d3)

d3 = d1 | d2
# print(d3)

# Створіть програму, яка приймає список та повертає словник, де ключі — це елементи списку, 
# а значення — це кількість входжень цих елементів в список.

a = [1,2,2,2,3,3,4,4,4,4,4,4,5,5,5,5,6,6]
slovnik = {}


for el in a:
    slovnik[el] = slovnik.get(el, 0) + 1
# print(slovnik)

from collections import Counter
slovnik1 = dict(Counter(a))
# print(slovnik1)

# Напишіть програму, яка приймає список чисел та повертає список, в якому кожен елемент — це 
# кількість входжень цього числа в вхідному списку.
a = [1,2,2,2,3,3,4,4,4,4,4,4,5,5,5,5,6,6]

rl = list(Counter(a).values())
# print(rl)

# Створіть програму, яка приймає список та повертає новий 
# список, в якому всі елементи вхідного списку випадковим чином перетасовані.
import random
b = [1,2,3,4,5,6,]

c = random.sample(b, len(b))
# print(c)

# Напишіть програму, яка приймає словник та повертає список ключів, значення яких є максимальними у словнику.
sl = {
    'a': 2,
    'b': 8,
    'c': 8,
    'd': 8,
}

maxVal = max(sl.values())

maxSpis = [i for i in sl if sl[i] == maxVal]
# print(maxSpis)

# Створіть програму, яка приймає список та повертає новий список, в якому кожен елемент — 
# це сума попередніх елементів вхідного списку (тобто, перший елемент нового списку — це 
# перший елемент вхідного списку, другий елемент нового списку — це сума першого та другого елементів 
# вхідного списку і т.д.).

aaaa = [2,9,3,5,6]

bbbb = []

cur_sum = 0

for i in aaaa:
    cur_sum += i
    bbbb.append(cur_sum)

# print(bbbb)


#кортежі tuple()

d = (1, 'a', aaaa, True)
print(type(d))

t = ()
t1 = (5)
print(t1)


tup1 = 2, 'sdfsdf', aaaa,'sdfsdf','sdfsdf','sdfsdf'
print(tup1[-1])

# tup1[0] = 8
# print(tup1)

print(tup1.index(2))
print(tup1.count('sdfsdf'))

lll = 'Lorem ipsum dolores'

cls = lll.replace(' ', '')

sc = Counter(cls)
top3 = sc.most_common(3)
print(top3)