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


# Напишіть програму, яка приймає два списки та повертає список, який містить елементи, 
# які зустрічаються у обох вхідних списках.

s1 = [1,2,3,4,5]
s2 = [4,5,6,7,8]

s3 = [i for i in s1 if i in s2]
print(s3)