# # Створіть два порожніх списки first_list та second_list.

list1 = []
list2 = []


# # 2. Заповніть перший список введеними з клавіатури значеннями 
# # за допомогою циклу, що запитує користувача ввести числа, 
# # доки користувач не введе слово "stop".

while True:
    inp = input('> ')
    if inp == 'stop':
        break
    else:
      list1.append(int(inp))  

# # 3. Після цього виведіть список на екран.
print(list1)

# # 4. Далі скопіюйте всі парні числа з first_list у second_list.

list2 = [num for num in list1 if num % 2 == 0]
copy_list = list2.copy()
# print(copy_list)
# for num in list1:
#     if num % 2 == 0:
#         list2.append(num)


# # 5. Наприкінці виведіть обидва списки.
print(list2)
print(copy_list)


# Написати to-do програму, що дає можливість 
# користувачеві вводити нові завдання на сьогодні, допоки користувач не введе “q”.

todo = []

print('Що робимо?: ')

while True:
   inp = input('> ')
   if inp == 'q':
      break
   else:
      todo.append(inp)

for i in range(len(todo)):
    print(f'{i + 1}. {todo[i]}')
# count = 1
# for i in todo:
#    print(f'{count}. {i}')
#    count+=1

print('видалення завдання: ')


while True:
   taskn = input('>Введіть номер таски: ')
   if taskn == 'q':
      break
   else:
      taskn = int(taskn)
      if taskn > len(todo) or taskn <= 0:
         print("Out of range")
      else:
         todo.pop(taskn - 1)
         print('deleted')
todo.sort()


for i in range(len(todo)):
    print(f'{i + 1}. {todo[i]}')
        
