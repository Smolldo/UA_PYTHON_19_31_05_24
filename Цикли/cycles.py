fruit = 'apple'

for char in fruit:
     print(char)

colors = ['red', 'green', 'blue', 'black']

for color in colors:
    print(color)
else:
    print('end)))')


# range()  1. початок діапазону. 2. кінець діапазону 3. крок діапазону

sum = 0  
for i in range(1,11 + 1):  
    sum += i
print(sum)

# вкладені цикли - цикл в циклі

# Порахувати середнє арифметичне всіх чисел кратних 3 з певного інтервалу

sum = 0
count = 0

for num in range(1,12 + 1):
    if num % 3 == 0:
        sum += num
        count += 1
print(sum / count)

a = 0

while True:
    print(a)
    if a > 20:
        break
    a +=1


while True:
    name = input('Enter name: ')
    if name == 'stop' : break
    print(f'Hello {name}')
    continue
a = 0

while a < 5:
    a += 1
    if not a % 2:
        continue
    print(a)