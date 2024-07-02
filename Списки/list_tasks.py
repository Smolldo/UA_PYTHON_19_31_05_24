a = ['Misha', 'Kolya', 'Petya']

if 'Misha' in a:
    print('Yes')

if "John" not in a:
    print('John is not on the list')


for item in a:
    print(f'Hello {item}, u just won 300$')


# Написати програму, що рахує суму всіх елеметів у списку.
a = [1,2,3,4,5]
suma = 0
for i in a:
    suma += i
print(suma)
print(sum(a))

# Написати програму, що рахує добуток всіх елементів у списку.
a = [1,2,3,4,5]
dob = 1

for i in a:
    dob *= i
print(dob)


# Написати програму, яка видалить зі списку 0-й, 5-й і 7-й елементи зі списку
c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] #a,f,h

c.pop(7) #del c[7]
c.pop(5) #del c[5]
c.pop(0) #del c[0]
print(c)

# Написати програму, що дістає максимальне число зі списку.
a = [1,2,3,4,5]
max_num = a[0]

for i in a:
    if i > max_num:
        max_num = i
print(max_num)
print(max(a))

# Піднести кожен із елементів списку до кубу
a = [1,2,3,4,5]
# a1 = []
# for i in a:
#     a1.append(i**3)
# print(a1)
a1 = [i ** 3 for i in a]
print(a1)

# Видалити пусті строки зі списку.
f = ['a', '', 'sfsdfs', " "]
f1 = []

for i in f:
    item = i.strip() # прибирає пробіли
    if item:
        f1.append(item)
print(f1)

# Написати програму, що прибере дублікати зі списку.
b = [1,2,33,3,3,3,3,3,1,1,1,4,4,5,6,7,10,4,4,4]
b1 = list(set(b)) # .set() - прибирає дублікати
print(b1)


# Написати програму, що порахує кількість додатніх елементів і списку та кількість від’ємних
lst = [1,2,3,-4,-5,-6,7,8,-9]

pos_n = 0
neg_n = 0

for i in lst:
    if i > 0:
        pos_n +=1
    else:
        neg_n += 1
print(f'pos nums = {pos_n}. neg nums = {neg_n}')