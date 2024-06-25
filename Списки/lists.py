a = 5
l2 = [1,2,3,4,'a','f', 'foo', 'bar', [1,2,3,4], a, True, (1,2,3), {"name": "name"}]
l1 = list()
print(l1)

l = ['moloko', 'sir', 'kovbasa']

print(l[0]) 
print(l[2])

l3 = ['a', 'b', ['aaa', 'bim bom', ['fff', 'bum']], 'c', 'd']
print(l3[1])
print(l3[2])
print(l3[2][1])
print(l3[2][2][1])

# Створити список, який буде містити послідовність символів.
str = list('sjkfsdfhgfjiukdgdfgod')
print(str)

# Створити список, який буде містити числові значення.
str1 = list((1,2,3))
print(str1)

# Створити список, який буде містити ім’я, прізвище і кількість повних років учня.

l5 = list(('Misha', 'Honyk', 25))
print(l5)


print(arr[0])
print(arr[-1])
print(arr[-3])


# Написати програму, що рахує суму всіх елеметів у списку.
arr = [1,2,3,4,5]
sum = 0

for i in arr:
    sum += i # sum = sum + i
print(sum)

# Написати програму, що рахує добуток всіх елементів у списку.
sum = 1
for i in arr:
    sum *= i # sum = sum * i
print(sum)


# Написати програму, що перевірить порожній список чи ні.
a = []

if a:
    print('заповнений')
else:
    print('не заповнений')

# Написати програму, що дістає максимальне число зі списку.
q = [22,11,2,999,65,-6,45]

max_num = q[0]
min_num = q[0]
for i in q:
    if i > max_num:
        max_num = i
    if i < min_num:
        min_num = i    
print(max_num)
print(min_num)