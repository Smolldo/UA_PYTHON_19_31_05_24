a = [1,2,3,4,5]
# .append() - додає в кінець списку елемент
a.append(6)
print(a)

b = ['sdfs', 'asdad' ]
b.append('dfjgdfiu')
print(b)

#  .clear() - очищає повністю список

a.clear()
print(a)

# .remove() - видалити один елемент списку

a.remove(3)
a.remove(a[2])

# a.remove(0) - поверне помилку, бо 0 нема в списку
b = ['lol', 'omg','omg','omg','omg', 'kekw']

print(b)
b.remove('omg')
print(b)

c = [12,34,54323,76,-121,5454]
d = ['app', 'dfdf', 'cvv', 'sdf', 'bsda', ]

# .sort() - сортує список
c.sort()
print(c)
d.sort()
print(d)


# f = [1, 'dsfdf', -3, 'aaa']  сортування з різними типами неможливе
# f.sort()
# print(f)
c.sort(reverse=True) # зворотнє сортування
print(c)

a = [1,2,4,3,5]
a.reverse() # виведення списку в зворотньому напрямку БЕЗ сортування
print(a)

# .pop() - повертає і видаляє по замовчуванню останній елемент. або за індексом

a = [1,2,3,4,5]
d = ['app', 'dfdf', 'cvv', 'sdf', 'bsda', ]
elem = a.pop()
a.pop(3)
print(elem)
d.pop(0)
# print(a)
print(d)

d = ['app', 'dfdf', 'cvv', 'sdf', 'bsda', ]

del d[0] # del видаляє елемент
print(d)

a = [1,2,3,4,5]
d = ['app', 'dfdf', 'cvv', 'sdf', 'bsda', ]

a.extend(d) # розширення списку а списком b
print(a)

a = [1,2,3,4,5]
print(a.index(2)) # повертає індекс конкретного елемента
a.insert(1, 'c') # вставляє новий елемент на вказаний індекс
print(a.index(2))
print(a.index('c'))
print(a)

# .count() - підрахунок однакових елементів

lt = ['s', 'y', 'b','s', 'y', 'b','s', 'y', 'b']
amount = lt.count('s')
print(amount)