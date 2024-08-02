a = 'hello world'

print(a[0:3:1])
print(a[:3])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers[:10:2])
print(numbers[::2])

#  Використовуючи зрізи, вивести на екран всі парні числа.
print(numbers[1:9+1:2])
print(numbers[1::2])

# Використовуючи зрізи, вивести на екран числа: 3,6,9.
print(numbers[2::3])

# a[start:stop] # items start through stop-1
# a[start:] # items start through the rest of the array
# a[:stop] # items from the beginning through stop-1
# a[:] # a copy of the whole array

# a[-1] # last item in the array
# a[-2:] # last two items in the array
# a[:-2] # everything except the last two items



# Заданий рядок, який містить ім’я
#  та прізвище користувача, що розділені пробілом:
# pip = 'Ivan Ivanov' delimiter = ' ' 
# Написати програму з використанням зрізів, 
# яка виокремить ім’я та прізвище.

pip = 'Ivan Ivanov' 
delimiter = ' ' 

indx = pip.find(delimiter)
print(indx)

first_name = pip[:indx]
# print(first_name)
last_name = pip[indx:]

print(f'fn: {first_name}, ln = {last_name}')

# порахувати кількість номерів київстару
phones = [
    '+38(067) 999-99-99', 
    '+38(063) 999-99-99',
    '+38(098) 888-88-88', 
    '+38(068) 777-77-77'
    ]

codes = [
    '067',
    '068',
    '098'
]
count = 0
for item in phones:
    code = item[4:7]
    if code in codes:
        count += 1

print(f'amount of ks = {count}')


#Множини  set()

# a = set()

a = set('HELLO')
# print(a)

b = {1,2,3,4,3,4,3,4,3,4,3,4,3,42,2,2,2,1,}
# print(b)

# add(elem):

c = {1,2,3}
c.add(4)
print(c)


# remove(elem):
c.remove(1)
print(c)

# discard(elem):
c.discard(7)
print(c)

s1 = set('hello')
s2 = set('hi there!')

s3 = s1.symmetric_difference(s2)
print(s3)
print(s1 ^ s2) #XOR


# & - i
print(s1 & s2)

# | - OR  s1.union(s2)
print(s1 | s2)

print(s1.difference(s2))

cus1 = {'Abobus', "Amogus", "Doom Guy"}
cus2 = {'Arthur', "Amogus", "Ezio"}

# клієнтів, які купили обидва товари А і B
intrsctn = cus1 & cus2
print(intrsctn)


# створити один список клієнтів, шляхом операції об’єднання
all_clients = cus1 | cus2 # cus1.union(cus2)
print(all_clients)